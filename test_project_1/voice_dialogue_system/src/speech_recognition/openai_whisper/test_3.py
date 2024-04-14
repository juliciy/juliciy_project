import whisper


def transcribe_audio_foe_test3(path):
    """
    将指定路径的音频文件转录成文本。

    参数:
        path (str): 要转录的音频文件的文件路径。

    返回:
        str: 转录得到的文本。
    """
    model = whisper.load_model("base")
    # models = ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large']
    # 假设 `model` 是一个已经加载的模型实例，能够执行语音到文本的转换
    result = model.transcribe(path, fp16=False, language="Chinese")
    return result["text"]


if __name__ == '__main__':
    model = whisper.load_model("tiny")

    path = "./recorded_audio.wav"
    result = transcribe_audio_foe_test3(path)
    print(result)
