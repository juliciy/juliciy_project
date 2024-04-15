import os
import pyaudio
import numpy as np
import datetime

from test_project_1.voice_dialogue_system.src.speech_recognition.openai_whisper.audio_transcription import \
    transcribe_audio_to_text
from test_project_1.voice_dialogue_system.src.wake_word.utils.functions import generate_wake_words_dict, save_wake_word_audio
from test_project_1.voice_dialogue_system.src.wake_word.utils.wake_word_utils import is_wake_word

def load_transcriptions_dict(base_path='user_wake_words'):
    """
    读取base_path下每个用户目录中的第一个.txt文件，将每行文本作为键，用户名作为值。

    参数:
    base_path : str
        存放用户唤醒词文本的根目录。

    返回值:
    dict
        键为唤醒词文本，值为对应的用户名的字典。
    """
    transcriptions_dict = {}

    # 遍历base_path下的所有目录
    for user_dir in os.listdir(base_path):
        user_dir_path = os.path.join(base_path, user_dir)
        if os.path.isdir(user_dir_path):  # 确保是目录
            txt_files = [file for file in os.listdir(user_dir_path) if file.endswith('.txt')]
            if txt_files:
                txt_file_path = os.path.join(user_dir_path, txt_files[0])
                # 读取第一个txt文件的每行文本
                with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
                    for line in txt_file:
                        transcriptions_dict[line.strip()] = user_dir  # 使用strip()去除可能的空白字符
                        print("load_transcriptions_dict : ", line.strip(), user_dir)

    return transcriptions_dict

def transcribe_audio(audio_data_np, sample_rate, temp_audio_path = './user_wake_words_temp/temp_audio.wav'):
    """
    使用 Whisper 模型将 NumPy 形式的音频数据转换为文本。

    参数:
    audio_data_np : np.array
        包含音频数据的 NumPy 数组。
    sample_rate : int
        音频的采样率。

    返回值:
    str
        转换得到的文本。
    """
    # 将 NumPy 数组转换为音频文件并保存，因为 Whisper 目前需要文件输入
    save_wake_word_audio(temp_audio_path, audio_data_np.tobytes(), sample_rate)

    # 使用 Whisper 模型进行转写
    result = transcribe_audio_to_text(temp_audio_path)
    return result


def listen_for_wake_word(sample_duration=3, sample_rate=16000, base_path="./user_wake_words/", temp_audio_path = './user_wake_words_temp/temp_audio.wav'):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=1024)

    print("Listening for wake word...")
    audio_frames = []
    one_second_frames = int(sample_rate / 1024)
    wake_words_dict = load_transcriptions_dict(base_path)

    try:
        while True:
            data = stream.read(1024, exception_on_overflow=False)
            audio_frames.append(data)
            if len(audio_frames) >= one_second_frames * sample_duration:
                # 获取最近三秒的音频数据
                recent_audio_data = b''.join(audio_frames[-(one_second_frames * sample_duration):])
                audio_data_np = np.frombuffer(recent_audio_data, dtype=np.int16)

                # 转换为文本
                transcribed_text = transcribe_audio(audio_data_np, sample_rate, temp_audio_path)
                print("transcribed_text : ", transcribed_text)

                # 匹配文本与唤醒词
                for wake_word, file_path in wake_words_dict.items():
                    if wake_word in transcribed_text:
                        user = wake_words_dict[wake_word]  # 获取用户名
                        verified_filename = f"{base_path}{user}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
                        save_wake_word_audio(verified_filename, recent_audio_data, sample_rate)
                        print(f"Wake word detected for {user}! Audio saved as {verified_filename}")
                        return user
                # 如果没有检测到唤醒词，继续监听
                audio_frames = audio_frames[one_second_frames:]
                # break
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Stream closed.")


if __name__ == '__main__':

    base_path = "./user_wake_words/"
    # transcriptions_dict = load_transcriptions_dict(base_path)

    # for i in transcriptions_dict.items():
    #     print(i)

    user = listen_for_wake_word(base_path=base_path)
    if user:
        print(f"Wake word detected! Welcome, {user}.")
    else:
        print("No wake word detected.")
