
from aip import AipSpeech

# 设置 APPID、API Key 和 Secret Key
APP_ID = '61285720'
API_KEY = '2C5QC7Q8m4Q60jg3riFa9SbX'
SECRET_KEY = '0lUoGA5hH1VvPyADgKf36FLUfsb6C30m '

# 初始化 AipSpeech 对象
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 设置音频文件的位置
audio_file = '../audio.mp3'

# 读取音频文件
with open(audio_file, 'rb') as fp:
    audio_data = fp.read()

# 识别音频文件
res = client.asr(audio_data, 'wav', 16000, {
    'dev_pid': 1536,
})

print("res : ", res)

if res['err_no'] == 0:
    print(res['result'][0])