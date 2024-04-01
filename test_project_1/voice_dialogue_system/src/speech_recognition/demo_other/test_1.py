import deepspeech
import wave
import numpy as np

# 加载预训练模型
model_file_path = './deepspeech-0.9.3-models.pbmm'  # 更新为你的模型文件路径
model = deepspeech.Model(model_file_path)

# 如果有一个语言模型（.scorer文件），可以加载以提高准确率
# scorer_file_path = 'deepspeech-0.9.3-models.scorer'  # 更新为你的语言模型文件路径
# model.enableExternalScorer(scorer_file_path)

# 读取音频文件
audio_file = './audio_nihao.wav'  # 更新为你的音频文件路径
w = wave.open(audio_file, 'r')
frames = w.readframes(w.getnframes())
audio = np.frombuffer(frames, np.int16)

# 运行语音识别
text = model.stt(audio)
print("输出结果：")
print(text)
