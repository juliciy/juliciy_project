import pyttsx3
import os
# import pygame
import subprocess

def text_to_speech(text, output_file_path):
    """将文本转换为语音并保存到指定的文件路径.

    使用 pyttsx3 库，这个函数将给定的文本转换为语音并保存到指定路径的文件中。

    参数
    ----------
    text : str
        要转换为语音的文本内容。
    output_file_path : str
        语音文件的保存路径。

    返回值
    -------
    None
        此函数没有返回值。

    示例
    --------
    text_to_speech("你好，世界", "./hello_world.mp3")  # 将文本转换为语音并保存为 hello_world.mp3
    """
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file_path)
    engine.runAndWait()


def play_audio(audio_file_path):
    """在后台播放指定路径的音频文件.

    根据操作系统，使用适当的命令在后台播放音频文件。

    参数
    ----------
    audio_file_path : str
        音频文件的路径。

    返回值
    -------
    None
        此函数没有返回值。

    示例
    --------
    play_audio("./hello_world.mp3")  # 在后台播放 hello_world.mp3 音频文件
    """
    if os.name == 'nt':  # Windows 系统
        subprocess.Popen(['start', '', audio_file_path], shell=True)
    else:  # 非 Windows 系统
        subprocess.Popen(['xdg-open', audio_file_path])


def text_to_speech_and_play(text_file_path, output_file_path):
    """从文本文件读取文本，转换为语音，并播放.

    这个函数读取指定文本文件的内容，将其转换为语音，保存到指定路径，然后播放这个语音文件。

    参数
    ----------
    text_file_path : str
        文本文件的路径。
    output_file_path : str
        生成的语音文件的保存路径。

    返回值
    -------
    None
        此函数没有返回值。

    示例
    --------
    text_to_speech_and_play("./example.txt", "./output.mp3")  # 读取 example.txt，转换并播放为 output.mp3
    """
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    text_to_speech(text, output_file_path)

    print("语音已保存至:", output_file_path)

    play_audio(output_file_path)


if __name__ == "__main__":
    text_file_path = "../input/transcript.txt"
    output_file_path = "../output/recorded_audio.mp3"
    text_to_speech_and_play(text_file_path, output_file_path)
