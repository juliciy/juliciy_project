import os
import pyaudio
import wave
import datetime

def record_wake_word(username, record_seconds=3):

    # 获取当前日期和时间，格式化为 YYYYMMDD_HHMMSS
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

    # 设置音频参数
    chunk = 1024  # 每次读取的音频数据量
    format = pyaudio.paInt16  # 16位采样
    channels = 1  # 单声道
    sample_rate = 16000  # 采样率

    output_directory = '../user_wake_words'  # 唤醒词文件存储的目录
    output_file = f"{username}_wake_word_{timestamp}.wav"  # 文件名包含用户名和时间戳

    # 创建用户目录（如果不存在）
    user_dir = os.path.join(output_directory, username)
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)

    output_file_path = os.path.join(user_dir, output_file)  # 完整的文件路径

    p = pyaudio.PyAudio()

    # 打开音频输入流
    stream = p.open(format=format,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk)

    print(f"Recording for {record_seconds} seconds...")

    frames = []
    # 录制指定时间的音频
    for i in range(0, int(sample_rate / chunk * record_seconds)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # 停止并关闭流
    stream.stop_stream()
    stream.close()
    p.terminate()

    # 保存录音数据到文件
    wf = wave.open(output_file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(format))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Recording saved to {output_file_path}")

if __name__ == '__main__':
    username = input("Enter your username: ")

    record_wake_word(username)
