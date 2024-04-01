import requests
import json

API_KEY = "Ic6RADU7IfsVZOpLGNOY3PTv"
SECRET_KEY = "4xVVhnynzm4cryXrPwT0jHIzIrG4SswU"


def main():
    url = "https://vop.baidu.com/server_api"

    payload = json.dumps({
        "format": "pcm",
        "rate": 16000,
        "channel": 1,
        "cuid": "waYG5vpFlfiO32LJPSSreDpxcWp913IM",
        "token": get_access_token()
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_access_token():
    """
    使用 AK，SK 生成鉴权签名（Access Token）
    :return: access_token，或是None(如果错误)
    """
    url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {"grant_type": "client_credentials", "client_id": API_KEY, "client_secret": SECRET_KEY}
    return str(requests.post(url, params=params).json().get("access_token"))


if __name__ == '__main__':
    main()
