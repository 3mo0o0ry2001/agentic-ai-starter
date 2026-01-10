import os
import json
import re
from dotenv import load_dotenv
import aisuite as ai
from tools import get_weather, write_file, web_search

load_dotenv()

client = ai.Client()
model = "openai:gpt-4o-mini"

# برومبت "أمر عسكري" مشدد
system_prompt = """
You are a TECHNICAL EXECUTION AGENT. 
STRICT PROTOCOL:
1. If you need info, you MUST call 'web_search'.
2. If you have info, you MUST call 'write_file' to save it.
3. NEVER write the function name as a text response.
4. If you fail to use the technical 'tool_calls' feature, you MUST write the call as: web_search("query")
"""

tools = [get_weather, write_file, web_search]

def main():
    print("🤖 Agent is ready! (Type 'quit' to exit)")
    messages = [{"role": "system", "content": system_prompt}]

    while True:
        user_input = input("\nUser: ")
        if user_input.lower() in ["quit", "exit"]: break
        messages.append({"role": "user", "content": user_input})

        while True:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                tools=tools,
                max_tokens=1000
            )
            
            message = response.choices[0].message
            content = (message.content or "").strip()
            
            # 1. التنفيذ الرسمي (Native Tool Call)
            if message.tool_calls:
                print(f"\n⚙️ Executing Tools...")
                messages.append(message)
                for tool_call in message.tool_calls:
                    function_name = tool_call.function.name
                    arguments = json.loads(tool_call.function.arguments)
                    print(f"   > Action: {function_name}({arguments})")
                    
                    result = None
                    if function_name == "get_weather": result = get_weather(**arguments)
                    elif function_name == "write_file": result = write_file(**arguments)
                    elif function_name == "web_search": result = web_search(**arguments)
                    
                    messages.append({"role": "tool", "tool_call_id": tool_call.id, "content": str(result)})
                continue

            # 2. المصيدة الذكية (حتى لو كتب الاسم بس بدون أقواس)
            elif any(tool in content.lower() for tool in ["web_search", "write_file", "search"]):
                print("   > ⚠️ Model is being lazy! Forcing Tool execution...")
                
                # لو كتب "web_search" بس، هنطلب منه يحدد الـ Query
                if content.lower() == "web_search" or content.lower() == "search":
                    messages.append({"role": "assistant", "content": content})
                    messages.append({"role": "user", "content": "SYSTEM: You must provide the search query inside parentheses, e.g., web_search('query'). ACT NOW."})
                    continue
                
                # محاولة صيد الأقواس لو موجودة
                s_match = re.search(r'(?:web_)?search\s*\(\s*["\']?(.*?)["\']?\s*\)', content, re.IGNORECASE)
                w_match = re.search(r'write_file\s*\(\s*["\']?(.*?)["\']?\s*,\s*["\']?(.*?)["\']?\s*\)', content, re.IGNORECASE | re.DOTALL)
                
                if s_match:
                    res = web_search(s_match.group(1))
                    messages.append({"role": "user", "content": f"Search Results: {res}. Now save to results.txt using write_file."})
                    continue
                elif w_match:
                    res = write_file(w_match.group(1), w_match.group(2))
                    messages.append({"role": "user", "content": f"File saved: {res}. Task complete."})
                    continue
                
                # لو كتب كلام كتير وفيه كلمة search، هنجبره يستخدم التول
                messages.append({"role": "assistant", "content": content})
                messages.append({"role": "user", "content": "SYSTEM: Use the tool NATIVELY. Do not just talk about it."})
                continue
            
            else:
                print(f"\n✅ Final Answer:\n{content}")
                break

if __name__ == "__main__":
    main()