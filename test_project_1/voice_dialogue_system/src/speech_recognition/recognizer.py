# 引入科大讯飞的语音识别库
from xfyun import SpeechRecognizer
import json

# 初始化语音识别类
# 替换下面的'appid'和'apikey'为你的应用信息
recognizer = SpeechRecognizer(appid="你的APPID", api_key="你的API Key")


def recognize_audio(file_path):
    """
    使用科大讯飞进行语音识别。

    参数:
        file_path (str): 音频文件的路径。

    返回:
        str: 转换得到的文本。
    """
    # 执行语音识别
    result = recognizer.recognize_audio(file_path=file_path, language="zh_cn")

    # 解析结果
    if result["code"] == "0":
        # 识别成功，打印并返回结果
        print("识别结果：", result["data"])
        return result["data"]
    else:
        # 识别失败，打印错误信息
        print("识别失败：", result["message"])
        return ""


# 示例用法
if __name__ == "__main__":
    audio_path = "path_to_your_audio_file.wav"  # 替换为你的音频文件路径
    text = recognize_audio(audio_path)
    print("转换文本：", text)