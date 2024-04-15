from test_project_1.voice_dialogue_system.src.AIGC.AIGC_main import AIGC_main
from test_project_1.voice_dialogue_system.src.speech_recognition.recognizer import record_and_transcribe_audio, \
    record_and_transcribe_audio_for_openai_whisper
from test_project_1.voice_dialogue_system.src.tts.library_function.text_to_speech_test import text_to_speech_and_play


def process_audio_to_text() -> str:
    """
    录制音频，将其转录为文本，并保存到指定的文件路径，然后读取并返回这个文本。

    :return: str 转录后的文本内容。
    """
    # 录音转文本的路径
    output_file_path = "./speech_recognition/output/transcript.txt"  # 指定保存文本的路径
    tts_input_file_path = "./tts/input/transcript.txt"  # 指定保存文本的路径

    # 调用录音转文本函数
    record_and_transcribe_audio_for_openai_whisper(output_file_path, tts_input_file_path)

    # 读取转录的文本
    with open(tts_input_file_path, "r", encoding="utf-8") as file:
        transcript = file.read()
    return transcript

def process_text_to_speech_and_play(text_file_path):
    """
    读取文本文件，将文本转换为语音，并播放生成的音频文件。
    """
    # 文本到语音并播放
    text_file_path = "./tts/input/transcript.txt"
    output_file_path = "./tts/output/recorded_audio.mp3"
    text_to_speech_and_play(text_file_path, output_file_path)


def main():
    """
    主函数，循环接收用户的音频输入，处理对话，转换文本到语音，并播放响应。
    """
    while True:  # 持续接收用户输入
        print("请说话（'q' 结束对话）：")

        # 第一步： 进行唤醒词模块，

        # 录音并转录为文本
        user = process_audio_to_text()
        print("user : ", user)

        # 检查是否结束对话或输入为空
        if user.lower().strip() == 'q':
            print("对话结束。")
            break
        if not user.strip():
            print("输入内容为空，请重新说话。")
            continue

        # 使用AIGC模型进行对话处理，这里假设AIGC_main函数调用模型并返回生成的文本
        assistant_response = AIGC_main(user)  # 调整AIGC_main函数以返回文本而不是打印
        print("assistant_response : ", assistant_response)

        # 保存助手的回应到指定的文件
        text_file_path = "./tts/input/assistant_response.txt"
        with open(text_file_path, "w", encoding="utf-8") as file:
            file.write(assistant_response)

        # 将文本转换为语音并播放响应
        output_file_path = "./tts/output/assistant_response.mp3"
        text_to_speech_and_play(text_file_path, output_file_path)


if __name__ == "__main__":

    main()

    pass


