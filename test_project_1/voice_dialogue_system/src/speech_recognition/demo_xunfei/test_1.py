from iflytek import const, ws, tpy
import uuid
import time
import json


def transcribe_audio(audio_file_path):
    # 讯飞开放平台账号信息，需替换为您自己的账号信息
    appid = "your_appid"
    api_key = "your_api_key"
    secret_key = "your_secret_key"

    # 设置语音识别参数
    frame_size = 6400  # 默认每个音频帧的大小
    status = 0  # 初始状态值
    url = "wss://iat-api.xfyun.cn/v2/iat"  # 语音识别地址

    # 获取当前时间
    ts = str(int(time.time()))
    # 随机数
    nonce = str(uuid.uuid1())

    # 设置请求头参数
    header = {
        'app_id': appid,
        'authorization': tpy.calcAuthorization(appid, api_key, ts, nonce),
        'url': url,
        'method': 'POST',
        'content-type': 'application/json',
        'path': '/v2/iat',
        'host': 'iat-api.xfyun.cn',
        'date': ts,
        'nonce': nonce
    }

    # 打开音频文件
    with open(audio_file_path, 'rb') as f:
        audio_data = f.read()

    # 发送请求
    with ws.get_connection(header) as ws_obj:
        send_data = tpy.build_send_data(const.APPID, status, ts, nonce, audio_data, frame_size)
        ws_obj.send(send_data)
        recv_data = ws_obj.recv()
        result_json = json.loads(recv_data)
        if result_json["code"] == 0:
            return result_json["data"]["result"]["ws"][0]["cw"][0]["w"]
        else:
            print("识别失败：", result_json["message"])
            return None


if __name__ == "__main__":
    audio_file_path = "./audio_nihao.wav"
    transcript = transcribe_audio(audio_file_path)
    if transcript:
        print("Transcript:", transcript)
