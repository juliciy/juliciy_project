import soundfile as sf
import numpy as np

def load_and_check_audio(audio_path):
    audio, samplerate = sf.read(audio_path)
    print(f"Audio shape: {audio.shape}")
    print(f"Sample rate: {samplerate}")
    print(f"Data type: {audio.dtype}")

    # 转换为 float32 如果需要
    audio = np.array(audio, dtype=np.float32)
    print(f"Converted data type: {audio.dtype}")
    print(f"Memory size: {audio.nbytes} bytes")  # 查看音频数据占用的内存大小

    return audio, samplerate

# 调用该函数来检查音频文件
load_and_check_audio("audio.mp3")