import pyttsx3
import os
# import pygame
import subprocess

def text_to_speech(text, output_file_path):
    engine = pyttsx3.init()
    engine.save_to_file(text, output_file_path)
    engine.runAndWait()

def play_audio(audio_file_path):
    # 使用 subprocess 在后台播放音频文件
    if os.name == 'nt':  # Windows 系统
        subprocess.Popen(['start', '', audio_file_path], shell=True)
        # 使用 Windows 的默认音频播放器在后台播放音频文件
        # os.startfile(audio_file_path)
    else:  # 非 Windows 系统
        subprocess.Popen(['xdg-open', audio_file_path])
# def play_audio_in_pygame(audio_file_path):
#     # 初始化 pygame
#     pygame.init()
#
#     # 隐藏播放器界面
#     os.environ['SDL_VIDEODRIVER'] = 'dummy'
#
#     # 播放音频文件
#     pygame.mixer.music.load(audio_file_path)
#     pygame.mixer.music.play()
#
#     # 等待音频播放完毕
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

def text_to_speech_and_play(text_file_path, output_file_path):
    # 从文本文件中读取文本
    with open(text_file_path, "r", encoding="utf-8") as file:
        text = file.read()

    # 将文本转换为语音并保存
    text_to_speech(text, output_file_path)

    print("语音已保存至:", output_file_path)

    # 播放语音文件
    play_audio(output_file_path)

if __name__ == "__main__":
    text_file_path = "../input/transcript.txt"
    output_file_path = "../output/recorded_audio.mp3"
    text_to_speech_and_play(text_file_path, output_file_path)
