import whisper
import numpy as np
from io import BytesIO
import soundfile as sf

def load_audio_into_memory(audio_path):
    # 读取音频文件到内存
    with open(audio_path, "rb") as f:
        audio_data = f.read()
    return BytesIO(audio_data)

def stereo_to_mono(audio_data):
    # 如果音频是双声道，计算两个声道的平均值转换为单声道
    if audio_data.ndim > 1:
        audio_data = np.mean(audio_data, axis=1)
    return audio_data

def transcribe_audio_from_memory(path):

    # 读取音频文件到内存
    audio_buffer = load_audio_into_memory(path)

    # 使用 Whisper 模型从内存中的音频数据进行转录
    model = whisper.load_model("small")

    # RuntimeError: Model medium-v2 not found; available models = ['tiny.en', 'tiny', 'base.en', 'base', 'small.en', 'small', 'medium.en', 'medium', 'large-v1', 'large-v2', 'large-v3', 'large']

    # 读取音频数据并转换为模型需要的格式
    audio, samplerate = sf.read(audio_buffer, dtype='float32', always_2d=True)
    audio = stereo_to_mono(audio)  # 确保音频是单声道

    # Whisper 模型的 transcribe 方法不需要 sample_rate 参数
    result = model.transcribe(audio, fp16=False, language="Chinese")
    return result["text"]


if __name__ == '__main__':

    # path = "./audio.mp3"
    path = "./recorded_audio.wav"
    # 从内存中的音频数据进行识别
    transcription = transcribe_audio_from_memory(path)
    print(transcription)
