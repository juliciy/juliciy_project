import requests
import json

# 修改成自己的api key和secret key
API_KEY = "bL0QoFohNelJ86EICzI8KfZw"
SECRET_KEY = "q2JRDSONuoxH2T8DpXCY76GDvuS1KXRp"


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


def save_messages(file_path, messages, response_text):
    """
    将最后一次用户和助手的对话追加保存到文本文件中。
    """
    with open(file_path, "a", encoding="utf-8") as file:  # 使用 "a" 模式，它会追加到文件末尾
        # 找到最后一条用户消息
        last_user_message = next((m for m in reversed(messages) if m["role"] == "user"), None)
        if last_user_message:
            file.write(f'user: {last_user_message["content"]}\n')
        file.write(f'assistant: {response_text}\n')  # 保存助手的最后一次响应


def read_and_append_messages(file_path, new_message):
    """
    读取文本文件中的对话并添加新的对话。
    """
    messages = []
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            for line in file:
                role, content = line.strip().split(': ', 1)
                messages.append({"role": role, "content": content})
    except FileNotFoundError:
        print("文件不存在，将创建一个新文件。")
    # 在读取旧对话后追加新的用户对话
    messages.append({"role": "user", "content": new_message})
    return messages


def AIGC_main(context):
    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/eb-instant?access_token=" + get_access_token()
    messages = read_and_append_messages("对话.txt", context)
    print("messages :", messages)

    payload = json.dumps({"messages": messages})
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)


    # 将服务器响应解析为JSON，并提取回复文本
    response_data = json.loads(response.text)
    assistant_response = response_data.get("result", "")
    print("response.text :", assistant_response)
    # 保存用户和助手的对话
    save_messages("对话.txt", messages, assistant_response)

    return assistant_response




if __name__ == '__main__':

    while True:  # 添加循环以持续接收用户输入
        user_input = input("请输入您的对话（输入'q'结束对话）：")
        if user_input.lower() == 'q':
            print("对话结束。")
            break
        if user_input == "":
            print("输入内容为空。")
            continue
        assistant_response = AIGC_main(user_input)
        print("assistant_response : ", assistant_response)