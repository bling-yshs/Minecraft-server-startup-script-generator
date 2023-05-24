# import requests
# from bs4 import BeautifulSoup
# import re
#
# # 获取用户输入的地址
# url = input("请输入需要爬取的网址：")
# # 发送请求获取网页内容
# response = requests.get(url)
# response.encoding = 'utf-8'  # 设置编码格式为utf-8
# # 解析HTML页面标签
# soup = BeautifulSoup(response.text, 'html.parser')
# # 获取所有链接
# links = soup.find_all('a')
# # 筛选server.jar结尾的链接并输出
# for link in links:
#     href = link.get('href')
#     if href and href.endswith('server.jar'):
#         print(href)
