from test_project_1.voice_dialogue_system.src.tts.library_function.text_to_speech_test import text_to_speech_and_play



if __name__ == "__main__":
    text_file_path = "./input/transcript.txt"
    output_file_path = "./output/recorded_audio.mp3"
    text_to_speech_and_play(text_file_path, output_file_path)