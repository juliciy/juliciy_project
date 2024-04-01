
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
        print("无法理解音频内容，请重新尝试。")  # Google 语音识别无法理解音频内容
    except sr.RequestError as e:
        print("无法从 Google 语音识别服务请求结果；{0}".format(e))  # 无法从 Google 语音识别服务获取结果

if __name__ == "__main__":
    audio_file_path = "./audio_nihao.wav"
    transcript = transcribe_audio(audio_file_path)
    print("Transcript:", transcript)
