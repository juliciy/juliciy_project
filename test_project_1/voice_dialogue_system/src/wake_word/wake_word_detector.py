import os

import pyaudio
import numpy as np
import datetime
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

def listen_for_wake_word(sample_duration=3, sample_rate=16000, base_path="./user_wake_words/", temp_base_path="./user_wake_words_temp/"):
    """监听环境音并检测唤醒词，一旦检测到唤醒词，保存相关音频文件。

    参数:
    sample_duration : int
        音频样本的持续时间，单位为秒。
    sample_rate : int
        音频的采样率。
    base_path : str
        保存音频文件的基本路径。
    """

    # 初始化麦克风输入流
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=1,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=1024)

    print("Listening for wake word...")
    audio_frames = []
    one_second_frames = int(sample_rate / 1024)  # 每秒所需的帧数

    try:
        users_wake_words_dict = generate_wake_words_dict(base_path)
        print("Loaded wake words dictionary:")
        for i in users_wake_words_dict.items():
            print(i)
        print("\n")

        while True:
            data = stream.read(1024)
            audio_frames.append(data)

            # 当积累到足够的帧以覆盖三秒钟时
            if len(audio_frames) == one_second_frames * sample_duration:
                # 连接并处理当前的三秒钟音频数据
                audio_data = b''.join(audio_frames)
                audio_data_np = np.frombuffer(audio_data, dtype=np.int16)

                # 检测唤醒词并计算相似度
                similarity_results = is_wake_word(audio_data_np, sample_rate, users_wake_words_dict)
                print("similarity_results:")
                for i in similarity_results.items():
                    print(i)
                print("\n")

                # 处理检测结果
                for filepath, result in similarity_results.items():
                    if result['similarity'] > 70:  # 可以调整阈值(0到100)
                        user = result['user']  # 从结果中获取用户名
                        verified_filename = f"{temp_base_path}{user}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
                        save_wake_word_audio(verified_filename, audio_data, sample_rate)
                        print(
                            f"Wake word detected for {user}! Audio saved as {verified_filename}, Similarity: {result['similarity']:.2f}%")
                        return user

                # 移除最早的一秒数据，保留后两秒数据
                audio_frames = audio_frames[one_second_frames:]

                # break
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Stream closed.")

if __name__ == '__main__':

    base_path = "./user_wake_words/"
    transcriptions_dict = load_transcriptions_dict(base_path)

    for i in transcriptions_dict.items():
        print(i)

    # user = listen_for_wake_word(base_path=base_path)
    # if user:
    #     print(f"Wake word detected! Welcome, {user}.")
    # else:
    #     print("No wake word detected.")
