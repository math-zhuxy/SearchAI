import json
import pprint
import WebCrawler
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
                        "type": "string",
                        "description": func_parameter_description
                    }
                },
                "required": ["query"]
            }
        }
    }
]

def model_communicate(user_message: str)-> str:
    AllMessages = [
        {
            "role": "system",
            "content": system_message
        },
        {
            "role": "user",
            "content": user_message
        }
    ]
    req_header = {
        "Content-Type": "application/json",
        'Authorization': f'Bearer {user_api_key}'
    }
    req_data = {
        "model": model_name,
        "messages": AllMessages,
        "tools": function_tools
    }

    model_response = requests.post(url= model_url, headers=req_header, data=json.dumps(req_data))

    if model_response.status_code == 200:
        print("Successfully obtained large language model information")
        model_response_data = model_response.json()

        if "tool_calls" in model_response_data["choices"][0]["message"]:
            # AllMessages.append(model_response_data["choices"][0]["message"])
            print("start calling the function")

            model_tool_call = model_response_data["choices"][0]["message"]["tool_calls"][0]

            if model_tool_call["function"]["name"] == "search":
                func_args = json.loads(model_tool_call["function"]["arguments"])
                print(f"model query key word: {func_args["query"]}")
                func_result = WebCrawler.get_search_result(func_args["query"])
                while func_result == "网络有问题" or func_result == "解析网络数据失败":
                    if func_result == "网络有问题":
                        print("There is a problem with the network")
                        print("try again")
                        func_result = WebCrawler.get_search_result(func_args["query"])
                    elif func_result == "解析网络数据失败":
                        print("Failed to parse network data")
                        print("try again")
                        func_result = WebCrawler.get_search_result(func_args["query"])
                    
                print("Network query successful")
                # print(func_result)
                AllMessages.append(
                    {
                        "role": "tool",
                        "content": func_result,
                        "tool_call_id": model_tool_call["id"]
                    }
                )
                # print(AllMessages)
                final_req_data = {
                    "model": model_name,
                    "messages": AllMessages
                }
                final_model_response = requests.post(url= model_url, headers=req_header, data=json.dumps(final_req_data))
                if final_model_response.status_code == 200:
                    print("Successfully obtained model final reply")
                    # print(final_model_response.json())
                    final_model_response_data = final_model_response.json()

                    return final_model_response_data["choices"][0]["message"]["content"]
                else:
                    print("error: can not obtain large language model")
            else:
                print("unknown function call")
        else:
            print("no need for network search")
            return model_response_data["choices"][0]["message"]["content"]
    else:
        print("error: can not obtain large language model")

    return "模型交互环节出现问题，无法成功获取模型信息，请检查API，模型接口地址和模型名称是否正确"

