import whisper

def transcribe_audio_to_text(path):
    """
    将指定路径的音频文件转录成文本。

    参数:
    ----------
    path : str
        要转录的音频文件的文件路径。

    返回值:
    -------
    str
        转录得到的文本。
    """
    model = whisper.load_model("base")
    # models = ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large']
    result = model.transcribe(path, fp16=False, language="Chinese")
    return result["text"]

# 本文件主要用于演示如何使用 Whisper 模型将音频文件转换为文本。
if __name__ == '__main__':

    path = "./recorded_audio.wav"
    # path = "./recorded_audio.wav"
    transcription = transcribe_audio_to_text(path)
    print("Transcribed Text:", transcription)
