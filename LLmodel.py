import json
import requests
try:
    with open("setting.json", "r", encoding= "utf-8") as file:
        setting_data = json.load(file)
    system_message = setting_data["prompt"]["sys"]
    model_url = setting_data["model"]["url"]
    user_api_key = setting_data["model"]["apikey"]
    model_name = setting_data["model"]["name"]
except FileNotFoundError as e:
    print(f"file \"setting.json\" not found: {e} ")
except json.JSONDecodeError as e:
    print(f"setting.json format is wrong: {e}")
def communicate(message: str)-> str:
    AllMessages = [
        {
            "role": "system",
            "content": system_message
        }
    ]
    AllMessages.append(
        {
            "role": "user",
            "content": message
        }
    )
    req_header = {
        "Content-Type": "application/json",
        'Authorization': f'Bearer {user_api_key}'
    }
    req_data = {
        "model": model_name,
        "messages": AllMessages
    }
    response = requests.post(url= model_url, headers=req_header, data=json.dumps(req_data))
    if response.status_code == 200:
        print(response.json())
    else:
        print("error")

communicate("你是谁")