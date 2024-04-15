
import os

from test_project_1.voice_dialogue_system.src.speech_recognition.demo_other.google import transcribe_audio
from test_project_1.voice_dialogue_system.src.speech_recognition.openai_whisper.test_1 import \
    transcribe_audio_from_memory
from test_project_1.voice_dialogue_system.src.speech_recognition.openai_whisper.audio_transcription import transcribe_audio_to_text
from test_project_1.voice_dialogue_system.src.speech_recognition.record_audio_dir.record_audio import recode_audio_test,record_audio

def save_transcript(transcript, output_file_path):
    """将转录的文本保存到指定的文件路径.

    这个函数打开指定的文件，如果不存在则创建，存在则覆盖，并将字符串写入文件。

    参数
    ----------
    transcript : str
        要保存的文本内容，应为字符串格式。
    output_file_path : str
        文本文件的保存路径，为字符串表示的文件路径。

    返回值
    -------
    None
        此函数没有返回值，它的作用是输出到文件。

    示例
    --------
    save_transcript("这是一个例子", "./example.txt")  # 将字符串保存到example.txt文件中
    """
    with open(output_file_path, "w", encoding="utf-8") as file:
        file.write(transcript)


def record_and_transcribe_audio(output_file_path, tts_input_file_path):
    """录制音频，将音频转换为文本，并保存到指定文件路径.

    这个函数首先录制音频，然后将录制的音频文件转换为文本，最后将文本保存到两个不同的文件路径。

    参数
    ----------
    output_file_path : str
        转录文本的输出文件路径，为字符串表示的文件路径。
    tts_input_file_path : str
        文本到语音转换的输入文件路径，为字符串表示的文件路径。

    返回值
    -------
    None
        此函数没有返回值。

    参看
    --------
    save_transcript : 用于将文本保存到文件的函数。
    record_audio : 用于录制音频的函数。
    transcribe_audio : 用于将音频转换为文本的函数。

    示例
    --------
    record_and_transcribe_audio("./output.txt", "./tts_input.txt")
    # 录制音频，并将转录的文本保存到 output.txt 和 tts_input.txt
    """
    audio_save_file_path = "./record_audio_dir/wav_dir/"
    record_audio(audio_save_file_path)

    audio_file_path = "./record_audio_dir/wav_dir/recorded_audio.wav"
    transcript = transcribe_audio(audio_file_path)
    print("Transcript:", transcript)

    save_transcript(transcript, output_file_path)
    save_transcript(transcript, tts_input_file_path)
    print("Transcript saved to:", output_file_path)


def record_and_transcribe_audio_for_openai_whisper(output_file_path, tts_input_file_path):
    """录制音频，将音频转换为文本，并保存到指定文件路径.

    这个函数首先录制音频，然后将录制的音频文件转换为文本，最后将文本保存到两个不同的文件路径。

    参数
    ----------
    output_file_path : str
        转录文本的输出文件路径，为字符串表示的文件路径。
    tts_input_file_path : str
        文本到语音转换的输入文件路径，为字符串表示的文件路径。

    返回值
    -------
    None
        此函数没有返回值。

    参看
    --------
    save_transcript : 用于将文本保存到文件的函数。
    record_audio : 用于录制音频的函数。
    transcribe_audio : 用于将音频转换为文本的函数。

    示例
    --------
    record_and_transcribe_audio("./output.txt", "./tts_input.txt")
    # 录制音频，并将转录的文本保存到 output.txt 和 tts_input.txt
    """
    audio_save_file_path = "./record_audio_dir/wav_dir/"
    record_audio(audio_save_file_path)

    audio_file_path = "./record_audio_dir/wav_dir/recorded_audio.wav"
    transcript = transcribe_audio_to_text(audio_file_path)
    print("Transcript:", transcript)

    save_transcript(transcript, output_file_path)
    save_transcript(transcript, tts_input_file_path)
    print("Transcript saved to:", output_file_path)





if __name__ == "__main__":

    #  这个函数首先录制音频，然后将录制的音频文件转换为文本，最后将文本保存到两个不同的文件路径。

    output_file_path = "./output/transcript.txt"  # 指定保存文本的路径
    tts_input_file_path = "../tts/input/transcript.txt"  # 指定保存文本的路径
    record_and_transcribe_audio_for_openai_whisper(output_file_path, tts_input_file_path)