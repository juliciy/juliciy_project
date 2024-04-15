import pyaudio
import numpy as np
from test_project_1.voice_dialogue_system.src.wake_word.utils.functions import generate_wake_words_dict
from test_project_1.voice_dialogue_system.src.wake_word.utils.wake_word_utils import is_wake_word

def listen_for_wake_word(sample_duration=3, sample_rate=16000, base_path="./user_wake_words_temp/"):
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
    three_seconds_frames = one_second_frames * 3  # 每三秒所需的帧数
    frames_recorded = 0

    try:
        base_path = "./user_wake_words/"
        users_wake_words_dict = generate_wake_words_dict(base_path)
        print("users_wake_words_dict : ", users_wake_words_dict)
        while True:
            data = stream.read(1024)
            audio_frames.append(data)
            frames_recorded += 1

            # 当积累到足够的帧以覆盖三秒钟时
            if len(audio_frames) == three_seconds_frames:
                # 连接并处理当前的三秒钟音频数据
                audio_data = b''.join(audio_frames)
                audio_data_np = np.frombuffer(audio_data, dtype=np.int16)

                similarity_results = is_wake_word(audio_data_np, sample_rate, users_wake_words_dict)

                print("similarity_results : ", similarity_results)
                for i in similarity_results.items():
                    print(i)


                break

                # if username:
                #     verified_filename = f"{base_path}{username}_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
                #     save_wake_word_audio(verified_filename, audio_data, sample_rate)
                #     print(f"Wake word detected for {username}! Audio saved as {verified_filename}")
                #     return username

                # 移除最早的一秒数据，保留后两秒数据
                audio_frames = audio_frames[one_second_frames:]
            # 等待下一帧数据，不需要sleep(1)因为read操作会阻塞直到缓冲区填满
    finally:
        stream.stop_stream()
        stream.close()
        p.terminate()
        print("Stream closed.")

if __name__ == '__main__':
    base_path = "./user_wake_words_temp/"
    user = listen_for_wake_word(base_path=base_path)
    if user:
        print(f"Wake word detected! Welcome, {user}.")
    else:
        print("No wake word detected.")
