import json
import time
from urllib.parse import quote
from selenium.webdriver.support import ui, expected_conditions
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By


def get_message(city):
    url = f'https://zhaopin.baidu.com/?query=&city={quote(city)}'
    chrome.get(url)
    time.sleep(3)
    # 获取搜索框
    query = chrome.find_element_by_css_selector('input[name="query"]')
    # 这里输入想搜索的岗位
    query.send_keys('Python')
    time.sleep(0.5)
    # 向右滚动1000px
    chrome.execute_script('var q = document.documentElement.scrollLeft=1000')
    # 点击搜索按钮
    chrome.find_element_by_css_selector('.search-btn').click()
    time.sleep(5)
    # 模拟向下滚动页面1000px
    chrome.execute_script('var q = document.documentElement.scrollTop=1000')
    time.sleep(3)
    ui.WebDriverWait(chrome, 60).until(
        expected_conditions.visibility_of_element_located((By.CLASS_NAME, 'listitem')),
        'listitem的div元素没有出现'
    )

def get_detail_message():
    # 获取岗位信息
    items = chrome.find_elements(By.CSS_SELECTOR, '.listitem>a')
    for item in items:
        # 过滤广告信息
        try:
            adv = item.find_element(By.CLASS_NAME, 'adbar-item')
            continue
        except:
            pass
        data = item.find_element(By.TAG_NAME, 'div').get_attribute('data-click')
        info_url = json.loads(data)['url']  # 获取岗位详情url
        title = item.find_element(By.CLASS_NAME, 'title').text  # 获取岗位名字
        salary = item.find_element(By.CSS_SELECTOR, '.salaryarea span').text  # 获取岗位薪资
        company = item.find_element(By.CSS_SELECTOR, '.company span').text  # 获取公司名字
        detail = [detail.text for detail in item.find_elements(By.CSS_SELECTOR, '.detail span')]  # 获取职位要求
        chrome.execute_script('var q = document.documentElement.scrollTop=1000')
        time.sleep(0.5)
        print(info_url, title, salary, company, detail)


if __name__ == '__main__':
    # 驱动浏览器
    chrome = Chrome('D:\chromedriver.exe')
    get_message('深圳')
    get_detail_message()





