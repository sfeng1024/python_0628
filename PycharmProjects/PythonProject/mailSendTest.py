import yagmail
import requests
from bs4 import BeautifulSoup

# Gmail 设置
sender_email = 'shuaifeng1024@gmail.com'           # 你的 Gmail 地址
app_password = 'zdzi waxb gzed gvsq'         # Gmail 应用密码（不是登录密码）
receiver_email = 's_feng1024@icloud.com'         # 收件人邮箱，可以是你自己


# 抓取岗位信息（模拟结构，需改成目标网站的实际HTML结构）
def fetch_jobs():
    url = 'https://www.shixiseng.com/interns?type=intern&city'  # 替换为实际招聘网站地址
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 模拟提取岗位标题（示例选择器，请根据页面结构修改）
    jobs = []
    for job in soup.select('.job-title'):
        jobs.append(job.get_text(strip=True))

    return jobs


# 发送邮件
def send_job_email(jobs):
    yag = yagmail.SMTP(user=sender_email, password=app_password)

    if jobs:
        subject = "实习"
        content = '\n'.join(jobs)
    else:
        subject = "职位提醒：暂无新职位"
        content = "今天没有发现新的岗位信息。"

    # 发送邮件
    yag.send(to=receiver_email, subject=subject, contents=content)
    print(f"✅ 邮件已发送：{subject}")


# 主函数
def main():
    jobs = fetch_jobs()
    send_job_email(jobs)