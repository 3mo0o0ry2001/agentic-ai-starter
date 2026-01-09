import os
import aisuite as ai
from dotenv import load_dotenv
import tools  # بننادي على الملف اللي عملناه فوق

# تحميل المفاتيح
load_dotenv()

# تجهيز العميل
client = ai.Client()

# تعريف قائمة الأدوات المتاحة للعميل
available_tools = [
    tools.get_current_time,
    tools.get_weather,
    tools.write_file
]

def run_agent(user_prompt):
    print(f"🤖 Agent is thinking about: '{user_prompt}'...")
    
    messages = [
        {"role": "system", "content": "You are a helpful AI assistant with access to tools."},
        {"role": "user", "content": user_prompt}
    ]

    # السحر كله هنا: aisuite هتهندل الـ Tool Calling لوحدها
    response = client.chat.completions.create(
        model="openai:openai/gpt-4o",          
        messages=messages,
        tools=available_tools,
        max_turns=5,
        max_tokens=1000
    )

    # طباعة الرد النهائي
    final_answer = response.choices[0].message.content
    print("\n✅ Final Answer:")
    print(final_answer)

if __name__ == "__main__":
    # تجربة عملية
    prompt = "What is the weather in Dubai right now? create a file named weather_report.txt and save the weather info in it."
    run_agent(prompt)