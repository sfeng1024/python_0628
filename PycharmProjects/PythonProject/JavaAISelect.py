import requests
from bs4 import BeautifulSoup
from datetime import datetime

SERVER_CHAN_KEY = "SCT288094TJQ7P9OXW07zN8PmqLl3iClKE"
TARGET_URL = "https://www.shixiseng.com/interns?type=intern&city=全国"

def fetch_jobs():
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(TARGET_URL, headers=headers, timeout=10)
        response.raise_for_status()
    except Exception as e:
        print(f"❌ 抓取失败：{e}")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    job_tags = soup.find_all("a", class_="title")

    matched_jobs = []
    for tag in job_tags:
        job_title = tag.get_text(strip=True)
        job_href = tag.get("href", "")
        job_url = f"https://www.shixiseng.com{job_href}" if job_href.startswith("/") else job_href

        # 临时放宽条件，只包含 java
        if "实习" in job_title.lower():
            matched_jobs.append((job_title, job_url))

    return matched_jobs

def send_wechat_notification(jobs):
    if not jobs:
        print("📭 暂无 Java + AI 岗位")
        return

    content_lines = ["🎯 **发现 实习 岗位如下：**\n"]
    for title, link in jobs:
        content_lines.append(f"- [{title}]({link})")
    content = "\n".join(content_lines)

    print(f"📄 即将发送的内容:\n{content}")

    url = f"https://sctapi.ftqq.com/{SERVER_CHAN_KEY}.send"
    payload = {
        "title": "【招聘提醒】Java岗位更新",
        "desp": content
    }

    try:
        response = requests.post(url, data=payload)
        print(f"📤 推送状态码: {response.status_code}")
        print(f"📤 返回内容: {response.text}")
        if response.status_code == 200:
            print("✅ 微信通知发送成功")
        else:
            print("❌ 微信推送失败，请检查SendKey或格式")
    except Exception as e:
        print(f"❌ 推送异常：{e}")

def run_monitor():
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} 开始监控...")
    jobs = fetch_jobs()
    send_wechat_notification(jobs)