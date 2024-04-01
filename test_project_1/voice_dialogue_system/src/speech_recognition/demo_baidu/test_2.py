from aip import AipSpeech


def transcribe_audio(audio_file_path):
    """将语音文件转换为文本"""
    # 设置百度语音识别 API 的应用信息
    APP_ID = 'your_app_id'
    API_KEY = 'your_api_key'
    SECRET_KEY = 'your_secret_key'

    # 初始化 AipSpeech 客户端
    client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

    # 读取语音文件
    with open(audio_file_path, 'rb') as f:
        audio_data = f.read()

    # 调用语音识别 API 进行转换
    result = client.asr(audio_data, 'wav', 16000, {
        'dev_pid': 1537,  # 普通话识别模型，默认即可
    })

    # 解析识别结果
    if result['err_no'] == 0:
        return result['result'][0]
    else:
        print("语音识别出错：{}".format(result['err_msg']))
        return None


if __name__ == "__main__":
    audio_file_path = "./audio_nihao.wav"
    transcript = transcribe_audio(audio_file_path)
    if transcript:
        print("Transcript:", transcript)
