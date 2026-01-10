from tavily import TavilyClient

# ⚠️ حط المفتاح اللي جبته هنا بين علامات التنصيص
tavily = TavilyClient(api_key="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")

def get_weather(location):
    return f"The weather in {location} is 28°C, Sunny (Mock Data)."

def write_file(filename, content):
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        return f"Successfully wrote to {filename}."
    except Exception as e:
        return f"Error writing file: {e}"

def web_search(query):
    """
    Searches the web using Tavily API (Professional & Reliable).
    """
    print(f"   🔎 Tavily Search: {query}...")
    try:
        # بحث حقيقي ومخصص للذكاء الاصطناعي
        response = tavily.search(query=query, search_depth="basic", max_results=3)
        
        # تنسيق النتائج عشان الموديل يفهمها
        context = []
        if 'results' in response:
            for res in response['results']:
                context.append(f"Title: {res['title']}\nLink: {res['url']}\nContent: {res['content']}\n")
            return "\n---\n".join(context)
        else:
            return "No results found."
            
    except Exception as e:
        return f"Error searching with Tavily: {e}"