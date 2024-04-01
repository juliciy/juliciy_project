from pydub import AudioSegment

# 加载MP3文件
audio = AudioSegment.from_mp3("./audio.mp3")

# 设置转换后的参数：采样率16000Hz，声道为单声道，采样宽度16位
audio = audio.set_frame_rate(16000).set_channels(1).set_sample_width(2)

# 导出为WAV格式
audio.export("output.wav", format="wav")
