
import speech_recognition as sr

def transcribe_audio(audio_file_path, language="zh-CN"):
    recognizer = sr.Recognizer()

    with sr.AudioFile(audio_file_path) as source:
        audio_data = recognizer.record(source)  # 读取音频文件

    try:
        # 使用 Google 语音识别引擎识别音频
        transcript = recognizer.recognize_google(audio_data, language=language)
        return transcript
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

if __name__ == "__main__":
    audio_file_path = "./audio_nihao.wav"
    transcript = transcribe_audio(audio_file_path)
    print("Transcript:", transcript)
