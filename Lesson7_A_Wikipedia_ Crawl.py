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
# import requests
# from bs4 import BeautifulSoup

# def continue_crawl(search_history,target_url,max_steps=25):
#     if search_history[-1] == target_url:
#         print("We have found!")
#         return False

#     elif len(search_history) > max_steps:
#         print("The search has gone on suspiciously long, aborting search!")
#         return False
    
#     elif search_history[-1] in search_history[:-1]:
#         print("We've arrived at an article we've already seen, aborting search!")
#         return False
    
#     else:return True
    
# print("======")
# print(continue_crawl(['https://en.wikipedia.org/wiki/Floating_point'],'https://en.wikipedia.org/wiki/Philosophy'))

"""这四个步骤可作为 while 循环构架中的注释。

while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    # add the first link to article_chain
    # delay for about two seconds
现在可以执行一些操作。

第一步，在 article_chain 中下载最后一篇文章的 html 是我们将使用请求包从维基百科获取 html 的命令。第二步，查找该 html 中的第一个链接 将涉及使用 BeautifulSoup 解析该 html，以获取第一个链接的 URL。

我建议将这两个步骤合并成一个单一的函数，其输入将是包含维基百科文章 URL 的字符串，输出将是包含维基百科文章正文中第一个链接的 URL 的字符串。我们调用此函数 find_first_link。

步骤： 在 article_chain 中下载最后一篇文章的 html 与 查找该 html 中的第一个链接 是我们计划中最初的前两个步骤，但将它们放在一个帮助函数 find_first_link 中，可使用外部库请求和 while 循环之外的 BeautifulSoup 提取全部详细信息。这样做也很有用，原因是如果将来关于这些库工作原理的详细信息发生变化，我们仍然可以保留主 while 循环，而且只需更改帮助函数。这也有助于保持代码真正可读性。

因为已经适当地定义了 find_first_link 的输入和输出，所以我可以把这个函数留给 Philip 执行 - 之后他将开始处理。现在，我可以根据这个函数的输出内容，并通过将 find_first_link 调用到 while 循环中来使其发挥作用。

while continue_crawl(article_chain, target_url): 
    # download html of last article in article_chain
    # find the first link in that html
    first_link = find_first_link(article_chain[-1])
    # add the first link to article chain
    # delay for about two seconds
索引 [-1] 提供了 article_chain 列表中的最后一个条目，所以在下一行，将 first_link 添加到 article_chain 的末尾可起到一定作用 - 下一步将编写该代码！"
"""
import requests
from bs4 import BeautifulSoup



# response = requests.get('https://en.wikipedia.org/wiki/A._J._W._McNeilly')
# response = requests.get('https://en.wikipedia.org/wiki/Oryzomys_dimidiatus')

# html=response.text
# print(html)
# soup = BeautifulSoup(html,'html.parser')

"""第一行代码查找到包含文章正文的 div。 如果该标签是 div 的子类，则下一行在 div 中循环每个<p>。我们从文档了解到，"如果想让 Beautiful Soup 只考虑直接子类，可以按照recursive=False进行传递" 。

循环主体可以查看段落中是否存在 a 标签。如果这样，从链接中获取 url，并将其存储在 first_relative_link 中，然后结束循环。
"""
# content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')
# for element in content_div.find_all("p", recursive=False):
#     if element.find("a",recursive=False):
#         # first_relative_link = element.a.get('href')
#         first_relative_link = element.find("a",recursive=False).get('href')
#         break
# print(first_relative_link)

# print(soup.find(id='mw-content-text').find(class_='mw-parser-output').p.a.get('href'))
# print(soup.find(id='mw-content-text').find(class_='mw-parser-output').p.a.get('href'))

def find_first_link(url):
    response=requests.get(url)
    html=response.text
    soup = BeautifulSoup(html,"html.parser")
    
    # TODO: find the first link in the article, or set to None if
    content_div = soup.find(id='mw-content-text').find(class_='mw-parser-output')


    # there is no link in the article.
    article_link = "a url, or None"

    for element in content_div.find_all("p", recursive=False):
        if element.find("a",recursive=False):
        # first_relative_link = element.a.get('href')
            first_relative_link = element.find("a",recursive=False).get('href')
        break
    print(first_relative_link)
    
    if not article_link:
        return
    
    # Build a full url from the relative article_link url
    first_link = urllib.parse.urljoin('https://en.wikipedia.org/', article_link)

    return first_link

import time
def web_crawl():
    while continue_crawl(article_chain, target_url): 
        # download html of last article in article_chain
        # find the first link in that html
        first_link = find_first_link(article_chain[-1])
        # add the first link to article chain
        # delay for about two seconds
        time.sleep(2)
        
"""习题 1/2
在这些方法中，哪些可能有助于我们查找到想要的链接，而不是 mw-content-text div 标签较远后代标签的链接？选择所有看似相关的方法。

find_all方法
children方法

可使用 children 方法查找直接后代。我们也可以使用 find_all 方法，并将 recursive 参数设置为 False，以便仅查找子类。
"""


