import LLMmodel
if __name__ == '__main__':
    while True:
        message = input("输入你的问题：")
        print(LLMmodel.model_communicate(message))