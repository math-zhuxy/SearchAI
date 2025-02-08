import json
import WebCrawler
import requests
import set

function_tools = [
    {
        "type": "function",
        "function": {
            "name": "search",
            "description": set.function_description,
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": set.func_parameter_description
                    }
                },
                "required": ["query"]
            }
        }
    }
]

AllMessages = [
    {
        "role": "system",
        "content": set.system_message
    }
]

def model_communicate(user_message: str)-> str:
    print("start communicate with LLM")

    AllMessages.append(
        {
            "role": "user",
            "content": user_message
        }
    )

    req_header = {
        "Content-Type": "application/json",
        'Authorization': f'Bearer {set.user_api_key}'
    }
    if set.func_call_choice == "force":
        req_data = {
            "model": set.model_name,
            "messages": AllMessages,
            "tools": function_tools,
            "tool_choice": {"type": "function", "function": {"name": "search"}}
        }
    elif set.func_call_choice == "auto":
        req_data = {
            "model": set.model_name,
            "messages": AllMessages,
            "tools": function_tools
        }
    elif set.func_call_choice == "none":
        req_data = {
            "model": set.model_name,
            "messages": AllMessages
        }
    else:
        return "模型参数设置错误"

    model_response = requests.post(url= set.model_url, headers=req_header, data=json.dumps(req_data))

    if model_response.status_code != 200:
        print("error: can not obtain large language model")
        return "模型交互环节出现问题，无法成功获取模型信息，请检查API，模型接口地址和模型名称是否正确"
    
    print("Successfully obtained large language model information")

    model_response_data = model_response.json()

    if "tool_calls" not in model_response_data["choices"][0]["message"]:
        print("no need for network search")
        AllMessages.append(
            {
                "role": "assistant",
                "content": model_response_data["choices"][0]["message"]["content"]
            }
        )
        return model_response_data["choices"][0]["message"]["content"]

    print("start calling the function")

    model_tool_call = model_response_data["choices"][0]["message"]["tool_calls"][0]

    if model_tool_call["function"]["name"] != "search":
        print("unknown function call")
        return "模型返回函数出现问题"
    
    func_args = json.loads(model_tool_call["function"]["arguments"])
    print(f"model query key word: {func_args["query"]}")
    func_result = WebCrawler.get_search_result(func_args["query"])

    AllMessages.append(
        {
            "role": "tool",
            "content": func_result,
            "tool_call_id": model_tool_call["id"]
        }
    )

    final_req_data = {
        "model": set.model_name,
        "messages": AllMessages
    }

    print("send final request to LLM")

    final_model_response = requests.post(url= set.model_url, headers=req_header, data=json.dumps(final_req_data))
    if final_model_response.status_code == 200:
        print("Successfully obtained model final reply")
        final_model_response_data = final_model_response.json()

        AllMessages.append(
            {
                "role": "assistant",
                "content": final_model_response_data["choices"][0]["message"]["content"]
            }
        )
        return final_model_response_data["choices"][0]["message"]["content"]
    
    else:
        print("error: can not obtain large language model")        
        return "模型交互环节出现问题，无法成功获取模型信息，请检查API，模型接口地址和模型名称是否正确"

