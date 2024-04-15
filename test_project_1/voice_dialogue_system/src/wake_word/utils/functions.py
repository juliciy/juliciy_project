import wave
import os
import whisper

from test_project_1.voice_dialogue_system.src.speech_recognition.openai_whisper.audio_transcription import \
    transcribe_audio_to_text


def generate_wake_words_dict(base_path='user_wake_words'):
    """
    遍历指定目录，为每个用户的每个唤醒词文件生成转写文本，并保存在用户名命名的文本文件中。

    参数:
    base_path : str
        存放用户唤醒词文件的根目录。

    返回值:
    dict
        键为唤醒词文件路径，值为对应的用户名的字典。
    """
    file_to_user = {}

    # 遍历 base_path 下的所有目录和文件
    for user_dir in os.listdir(base_path):
        user_dir_path = os.path.join(base_path, user_dir)
        if os.path.isdir(user_dir_path):  # 确保是目录
            transcription_file_path = os.path.join(user_dir_path, f"{user_dir}.txt")
            # 打开用户的文本文件，准备写入转写文本
            with open(transcription_file_path, 'w', encoding='utf-8') as transcript_file:
                # 在每个用户的目录中找到 wav 文件
                for file in os.listdir(user_dir_path):
                    if file.endswith('.wav'):
                        # 假设目录名即为用户名
                        username = user_dir
                        # 生成完整的文件路径
                        filepath = os.path.join(user_dir_path, file)
                        # 转写音频到文本
                        wav_to_text = transcribe_audio_to_text(filepath)
                        # 将文件路径作为键，用户名作为值添加到字典中
                        file_to_user[filepath] = username
                        # 将转写结果写入文件，每条记录占一行
                        transcript_file.write(f"{wav_to_text}\n")
                        print("Transcribed text saved to:", wav_to_text," : ", transcription_file_path)

    return file_to_user

def save_wake_word_audio(filename, audio_data, sample_rate):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # 单声道
        wf.setsampwidth(2)  # 采样宽度为2字节，因为使用的格式是pyaudio.paInt16
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data)

if __name__ == '__main__':

    # 将user_wake_words下面的音频转成文本。

    # 使用函数并打印结果
    base_path = "../user_wake_words"
    wake_words_dict = generate_wake_words_dict(base_path)
    for filepath, username in wake_words_dict.items():
        print(f"File: {filepath} is associated with user: {username}")