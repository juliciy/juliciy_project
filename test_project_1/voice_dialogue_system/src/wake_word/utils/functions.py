import os
import wave

def generate_wake_words_dict(base_path='user_wake_words'):
    users_wake_words = {}

    # 遍历 base_path 下的所有目录和文件
    for user_dir in os.listdir(base_path):
        user_dir_path = os.path.join(base_path, user_dir)
        if os.path.isdir(user_dir_path):  # 确保是目录
            # 在每个用户的目录中找到 wav 文件
            for file in os.listdir(user_dir_path):
                if file.endswith('.wav'):
                    # 假设目录名即为用户名
                    username = user_dir
                    # 生成完整的文件路径
                    filepath = os.path.join(user_dir_path, file)
                    # 将其添加到字典中
                    users_wake_words[username] = filepath
                    break  # 假设每个用户只有一个唤醒词文件

    return users_wake_words

def save_wake_word_audio(filename, audio_data, sample_rate):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(1)  # 单声道
        wf.setsampwidth(2)  # 采样宽度为2字节，因为使用的格式是pyaudio.paInt16
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data)



if __name__ == '__main__':
    # 使用函数并打印结果
    base_path = "../user_wake_words"
    wake_words_dict = generate_wake_words_dict(base_path)
    for user, path in wake_words_dict.items():
        print(f"{user}: {path}")
