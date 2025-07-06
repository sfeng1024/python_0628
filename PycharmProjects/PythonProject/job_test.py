import requests

def test_wechat_push():
    sckey = "你的Server酱SCKEY"
    url = f"https://sctapi.ftqq.com/{sckey}.send"
    data = {
        "title": "测试推送",
        "desp": "如果你收到这条消息，说明推送成功！"
    }
    resp = requests.post(url, data=data)
    print("状态码:", resp.status_code)
    print("返回内容:", resp.text)

if __name__ == "__main__":
    test_wechat_push()