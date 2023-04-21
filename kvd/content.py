import json

def assume_file_content_type(path: str) -> str:
    if path.endswith(".json"):
        return "application/json"
    elif path.endswith(".txt"):
        return "text/plain"
    else:
        return "application/octet-stream"

def assume_text_content_type(text: str) -> str:
    try:
        json.loads(text)
        return "application/json"
    except:
        return "text/plain"
