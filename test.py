from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# 微博内容
WEIBO_CONTENT = "copilot万岁！o(*￣▽￣*)ブ"

# 微博标签（示例）。将你想要的标签放在这个列表中，程序会把它们格式化为 #标签# 并拼接到正文前面
TAGS = ["茶几5mini不好用", "还得是克劳德酱w"]

def build_weibo_message():
    """根据 TAGS 和 WEIBO_CONTENT 生成最终要发布的文本"""
    if TAGS:
        tags_part = ' '.join(f"#{t}#" for t in TAGS)
        return f"{tags_part} {WEIBO_CONTENT}"
    return WEIBO_CONTENT

# 定时发布时间
SCHEDULED_TIME = "2025-11-06 22:57:45"

def wait_until_target_time(target_time):
    """等待直到目标时间"""
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if current_time >= target_time:
            break
        print(f"当前时间：{current_time}，等待中...")
        time.sleep(1)

def is_logged_in(driver):
    """判断是否已登录"""
    try:
        # 检查是否存在用户头像元素
        driver.find_element(By.XPATH, '//div[@class="woo-badge-box"]/img[contains(@class, "Ctrls_avatar_3Hf0X")]')
        print("已检测到登录状态")
        return True
    except:
        print("未检测到登录状态，需要登录")
        return False

def wait_for_login(driver):
    """等待用户完成登录"""
    print("请完成登录...")
    while not is_logged_in(driver):
        time.sleep(5)  # 每隔5秒检查一次登录状态
    print("登录成功！")

def post_weibo():
    """发布微博"""
    # 初始化 Chrome 浏览器
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # 打开微博页面
        driver.get("https://weibo.com/")
        time.sleep(5)  # 等待页面加载

        # 等待用户手动完成登录
        wait_for_login(driver)  # 等待用户完成登录

        # 检查是否需要切换到 iframe
        try:
            iframe = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "iframe"))
            )
            driver.switch_to.frame(iframe)
        except:
            print("未找到 iframe，继续操作主页面")

        # 显式等待发布框加载
        post_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//textarea[@placeholder="有什么新鲜事想分享给大家？"]'))
        )
        post_box.click()
        # 构建最终发布内容（将标签并入正文前）
        message = build_weibo_message()
        post_box.send_keys(message)

        # 点击发布按钮
        post_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "woo-button-primary") and contains(@class, "Tool_btn_2Eane")]'))
        )
        post_button.click()
        time.sleep(5)  # 等待发布完成

        print("微博发布成功！")
        print("浏览器将保持打开状态，您可以手动关闭...")
        
        # 等待用户手动关闭浏览器或按任意键继续
        input("按 Enter 键关闭浏览器...")

    except Exception as e:
        print("发生错误：", e)
        # 发生错误时也保持浏览器打开，方便调试
        input("发生错误，浏览器保持打开。按 Enter 键关闭浏览器...")

    finally:
        # 关闭浏览器
        driver.quit()

if __name__ == "__main__":
    # 等待到指定时间
    wait_until_target_time(SCHEDULED_TIME)
    # 发布微博
    post_weibo()