import pyaudio
import wave
import os

def record_audio(output_folder, duration=5, filename="recorded_audio.wav", channels=1, sample_rate=44100, chunk_size=1024, format=pyaudio.paInt16):
    audio = pyaudio.PyAudio()

    # 打开音频流
    stream = audio.open(format=format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk_size)

    print("开始录音...")
    frames = []
    for i in range(0, int(sample_rate / chunk_size * duration)):
        data = stream.read(chunk_size)
        frames.append(data)
    print("录音结束.")

    # 停止音频流
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 保存录音文件
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    file_path = os.path.join(output_folder, filename)
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    print("录音已保存至:", file_path)

def recode_audio_test():
    output_folder = "./wav_dir/"
    record_audio(output_folder)

if __name__ == "__main__":
    output_folder = "./wav_dir/"
    record_audio(output_folder)