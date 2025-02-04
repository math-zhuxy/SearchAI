import WebCrawler
import json
import requests
AllMessages = []
with open("setting.json", "r", encoding= "utf-8") as file:
    setting_data = json.load(file)
if "api_key" not in setting_data or "url" not in setting_data or "prompt" not in setting_data:
    print("setting.json file format error")
AllMessages.append(
    {
        "role": "system",
        "content": setting_data["prompt"]
    }
)
def communicate(message: str)-> str:
    AllMessages.append(
        {
            "role": "user",
            "content": message
        }
    )
    req_header = {
        "Content-Type": "application/json",
        'Authorization': f'Bearer {setting_data["api_key"]}'
    }
    req_data = {
        "model": "glm-4-flash",
        "messages": AllMessages
    }
    response = requests.post(url= setting_data["url"], headers=req_header, data=json.dumps(req_data))
    print(response.json())

communicate("你是谁")