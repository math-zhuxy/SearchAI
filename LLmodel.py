import json
import requests
try:
    with open("setting.json", "r", encoding= "utf-8") as file:
        setting_data = json.load(file)
    system_message = setting_data["prompt"]["sys"]
    model_url = setting_data["model"]["url"]
    user_api_key = setting_data["model"]["apikey"]
    model_name = setting_data["model"]["name"]
    function_description = setting_data["prompt"]["func"]["desp"]
    func_parameter_description = setting_data["prompt"]["func"]["para"]
except FileNotFoundError as e:
    print(f"file \"setting.json\" not found: {e} ")
except json.JSONDecodeError as e:
    print(f"setting.json format is wrong: {e}")

function_tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": function_description,
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "description": func_parameter_description,
                        "type": "string"
                    }
                },
                "required": ["query"]
            }
        }
    }
]

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
        "messages": AllMessages,
        "tools": function_tools
    }
    response = requests.post(url= model_url, headers=req_header, data=json.dumps(req_data))
    if response.status_code == 200:
        print(response.json())
    else:
        print("error")

communicate("你知道及你太美是什么意思吗")