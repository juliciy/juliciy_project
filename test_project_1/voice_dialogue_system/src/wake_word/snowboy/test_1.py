import snowboy.snowboydecoder as snowboydecoder

import sys

# 定义唤醒回调函数
def detected_callback():
    print("Hotword detected!")
    # 这里可以添加你的处理逻辑，例如启动语音识别或其他操作

# 设置唤醒词模型文件路径
model = "path_to_your_model.pmdl"  # 替换为你下载的唤醒词模型文件路径

# 设置灵敏度（可选，默认0.5）
sensitivity = 0.5

# 初始化Snowboy Detector
detector = snowboydecoder.HotwordDetector(model, sensitivity=sensitivity)

print('Listening... Press Ctrl+C to exit')

# 开始监听唤醒词
detector.start(detected_callback=detected_callback,
               interrupt_check=lambda: False,
               sleep_time=0.03)

# 持续监听，直到Ctrl+C被按下
detector.terminate()
