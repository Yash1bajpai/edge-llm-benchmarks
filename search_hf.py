import requests

def search_hf(query):
    response = requests.get(f"https://huggingface.co/api/models?search={query}")
    if response.status_code == 200:
        models = response.json()
        for m in models[:5]:
            print(m['id'])
    else:
        print("Error", response.status_code)

if __name__ == "__main__":
    search_hf("Gemma")
