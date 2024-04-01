
# 示例用法
import os

from test_project_1.voice_dialogue_system.src.speech_recognition.demo_other.google import transcribe_audio
from test_project_1.voice_dialogue_system.src.speech_recognition.record_audio_dir.record_audio import recode_audio_test,record_audio

def save_transcript(transcript, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(transcript)


def record_and_transcribe_audio():
    # 开始录音
    audio_save_file_path = "./record_audio_dir/wav_dir/"
    record_audio(audio_save_file_path)

    # 语音转文本
    audio_file_path = "./record_audio_dir/wav_dir/recorded_audio.wav"
    transcript = transcribe_audio(audio_file_path)
    print("Transcript:", transcript)

    # 文本储存到指定目录
    output_file_path = "./output/transcript.txt"  # 指定保存文本的路径
    tts_input_file_path = "../tts/input/transcript.txt"  # 指定保存文本的路径
    save_transcript(transcript, output_file_path)
    save_transcript(transcript, tts_input_file_path)
    print("Transcript saved to:", output_file_path)

if __name__ == "__main__":
    record_and_transcribe_audio()