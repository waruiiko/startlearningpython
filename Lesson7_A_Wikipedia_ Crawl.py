# # pip3 install requests 安装requests
# import requests
# response = requests.get('https://en.wikipedia.org/wiki/Dead_Parrot_sketch')
# print("======")
# # print(response.text)
# # print(type(response.text))
# html = response.text

# # pip3 install beautifulsoup4 安装beautifulsoup4
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.p)

"""测验：continue_crawl 函数
我们需要编写的第一个帮助函数是 continue_crawl，其将用于我们的 while 循环，如下所示：

while continue_crawl(search_history, target_url):
例如，我们可以使用这些值调用函数：

continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],
                       'https://en.wikipedia.org/wiki/Philosophy')
search_history 是维基百科文章 url 的字符串列表。列表中的最后一个项目是最近发现的 url。
如果 target_url 是查找到结果，停止搜索时文章 url 的字符串。
根据以下规则，continue_crawl 应该返回 True 或 False： 如果 search_history 中最近的文章是目标文章，则应停止搜索，函数应返回 False 如果列表中有 25 个 url，函数应返回 False 如果列表中有一个循环，函数应返回 False 否则应继续搜索，函数应返回 True。
"""
import requests
from bs4 import BeautifulSoup

def continue_crawl(search_history,target_url,max_steps=25):
    if search_history[-1] == target_url:
        print("We have found!")
        return False

    elif len(search_history) > max_steps:
        print("The search has gone on suspiciously long, aborting search!")
        return False
    
    elif search_history[-1] in search_history[:-1]:
        print("We've arrived at an article we've already seen, aborting search!")
        return False
    
    else:return True
    
print("======")
print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],'https://en.wikipedia.org/wiki/Philosophy'))