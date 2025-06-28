import requests

# 👇 你的 API Key（替换成自己的）
api_key = "sk-MqXgpDC8UrMqHjguc9azWLrwSXJCYcX2ou6K8LBjG8s0AYVK"

# 发送的消息内容
payload = {
    "model": "moonshot-v1-8k",  # Kimi 默认模型，可处理 8k 字符上下文
    "messages": [
        {"role": "user", "content": "请"}
    ]
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# Kimi Chat API 地址
url = "https://api.moonshot.cn/v1/chat/completions"

# 发送请求
response = requests.post(url, json=payload, headers=headers)

# 处理结果
if response.status_code == 200:
    reply = response.json()['choices'][0]['message']['content']
    print("Kimi 回复：", reply)
else:
    print("请求失败：", response.status_code)
    print("错误信息：", response.text)