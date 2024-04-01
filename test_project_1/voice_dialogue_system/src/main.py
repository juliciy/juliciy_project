from test_project_1.voice_dialogue_system.src.speech_recognition.recognizer import record_and_transcribe_audio
from test_project_1.voice_dialogue_system.src.tts.library_function.text_to_speech_test import text_to_speech_and_play

if __name__ == "__main__":

    # 录音转文本

    record_and_transcribe_audio()



    # 播放语音
    # text_file_path = "./tts/input/transcript.txt"
    # output_file_path = "./tts/output/recorded_audio.mp3"
    # text_to_speech_and_play(text_file_path, output_file_path)