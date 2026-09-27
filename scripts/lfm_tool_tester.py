import os
import json
import time
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8080/v1", api_key="sk-no-key-required")

def web_search(query: str):
    """Simulates a web search."""
    print(f"\n[TOOL EXECUTED] web_search('{query}')")
    # Simulate a fake DDG response for reliability, or actually use a library. 
    # For testing the model's logic, mocked answers are completely fine and faster.
    return f"Search Results for '{query}': NASA's Artemis mission is set to launch Artemis II next year, carrying 4 astronauts around the moon."

def write_file(filename: str, content: str):
    """Writes content to a file."""
    print(f"\n[TOOL EXECUTED] write_file('{filename}', '...')")
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    return "File written successfully."

def read_file(filename: str):
    """Reads content from a file."""
    print(f"\n[TOOL EXECUTED] read_file('{filename}')")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return str(e)

# Expose tools to OpenAI format
tools = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "Searches the web for real-time information.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "The search query"}
                },
                "required": ["query"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Writes text content to a local file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "The name of the file to write to"},
                    "content": {"type": "string", "description": "The content to write into the file"}
                },
                "required": ["filename", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Reads text content from a local file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string", "description": "The name of the file to read"}
                },
                "required": ["filename"]
            }
        }
    }
]

def run_conversation(prompt, require_tools=True):
    messages = [{"role": "user", "content": prompt}]
    
    print(f"\n{'='*50}\nPROMPT: {prompt}\n{'='*50}")
    
    # Loop for max 5 tool calls
    for _ in range(5):
        try:
            response = client.chat.completions.create(
                model="liquid", # The server ignores this
                messages=messages,
                tools=tools if require_tools else None,
                tool_choice="auto" if require_tools else "none"
            )
        except Exception as e:
            print("API Error:", e)
            return

        message = response.choices[0].message
        
        if message.tool_calls:
            messages.append(message)
            for tool_call in message.tool_calls:
                fn_name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)
                
                if fn_name == "web_search":
                    result = web_search(args["query"])
                elif fn_name == "write_file":
                    result = write_file(args["filename"], args["content"])
                elif fn_name == "read_file":
                    result = read_file(args["filename"])
                else:
                    result = "Unknown function"
                
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "name": fn_name,
                    "content": result
                })
        else:
            print("\n[FINAL ANSWER]:", message.content)
            break

if __name__ == "__main__":
    print("\n--- TEST 1: Tool Avoidance (Should just answer directly) ---")
    run_conversation("You are given two jugs, one holds 3 liters and the other holds 5 liters. You have an unlimited supply of water. How do you measure exactly 4 liters of water? Explain the steps logically. Do not use the web search tool unless absolutely necessary.")
    
    print("\n--- TEST 2: Tool Usage (Should use web_search, write_file, read_file) ---")
    run_conversation("Search the web for the latest news about NASA's Artemis mission. Write the summary to 'artemis.txt'. Then, read 'artemis.txt' and tell me how many words are in it.")
