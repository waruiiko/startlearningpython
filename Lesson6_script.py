# how_many_snakes = 1
# snake_string = """
# Welcome to Python3!

#              ____
#             / . .\\
#             \  ---<
#              \  /
#    __________/ /
# -=:___________/

# <3, Juno
# """


# print(snake_string * how_many_snakes)

# name = input("Enter your name: ")
# print("Hello there, {}!".format(name.title()))

# result = eval(input("Enter an expression: "))
# print(result)

# num = int(input("Enter an integer"))
# print("hello" * num)

# names = input("Enter names separated by commas: ").title().split(",")
# assignments = input("Enter assignment counts separated by commas: ").split(",")
# grades = input("Enter grades separated by commas: ").split(",")

# message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
# submit before you can graduate. You're current grade is {} and can increase \
# to {} if you submit all assignments before the due date.\n\n"

# for name, assignment, grade in zip(names, assignments, grades):
#     print(message.format(name, assignment, grade, int(grade) + int(assignment)*2))

"""练习：处理除以零的情形
现在运行下面的代码将在第二次调用 handle_zero 函数时导致错误，因为它遇到了 ZeroDivisionError 异常。

请修改下面的函数以处理该异常。如果在函数的第一行遇到该异常，应该输出警告消息并返回空列表。否则，应该运行函数的剩余代码。最后，该函数应该始终输出返回了多少组。
"""
# def create_groups(items, num_groups):
#    try:
#     size = len(items) // num_groups
#    except ZeroDivisionError as e:
#       print("WARNING: Returning empty list. Please use a nonzero number!!!{}!!!.".format(e))
#       return []
#    else:
#     groups = []
#     for i in range(0, len(items), size):
#         groups.append(items[i:i + size])
#     return groups
#    finally:
#     print("{} groups returned.".format(num_groups))
    

# print("Creating 6 groups...")
# for group in create_groups(range(32), 6):
#     print(list(group))

# print("\nCreating 0 groups...")
# for group in create_groups(range(32), 0):
#     print(list(group))

# def create_groups(items, num_groups):
#     try:
#         size = len(items) // num_groups
#     except ZeroDivisionError:
#         print("WARNING: Returning empty list. Please use a nonzero number.")
#         return []
#     else:
#         groups = []
#         for i in range(0, len(items), size):
#             groups.append(items[i:i + size])
#         return groups
#     finally:
#         print("{} groups returned.".format(num_groups))

# print("Creating 6 groups...")
# for group in create_groups(range(32), 6):
#     print(list(group))

# print("\nCreating 0 groups...")
# for group in create_groups(range(32), 0):
#     print(list(group))

"""读写文件
以下是如何在 Python 中读写文件的方式。

读取文件
f = open('my_path/my_file.txt', 'r')
file_data = f.read()
f.close()
首先使用内置函数 open 打开文件。需要文件路径字符串。open 函数会返回文件对象，它是一个 Python 对象，Python 通过该对象与文件本身交互。在此示例中，我们将此对象赋值给变量 f。
你可以在 open 函数中指定可选参数。参数之一是打开文件时采用的模式。在此示例中，我们使用 r，即只读模式。这实际上是模式参数的默认值。
使用 read 访问文件对象的内容。该 read 方法会接受文件中包含的文本并放入字符串中。在此示例中，我们将该方法返回的字符串赋值给变量 file_data。
当我们处理完文件后，使用 close 方法释放该文件占用的系统资源。
写入文件
f = open('my_path/my_file.txt', 'w')
f.write("Hello there!")
f.close()
以写入 ('w') 模式打开文件。如果文件不存在，Python 将为你创建一个文件。如果以写入模式打开现有文件，该文件中之前包含的所有内容将被删除。如果你打算向现有文件添加内容，但是不删除其中的内容，可以使用附加 ('a') 模式，而不是写入模式。
使用 write 方法向文件中添加文本。
操作完毕后，关闭文件。
"""

"""With
Python 提供了一个特殊的语法，该语法会在你使用完文件后自动关闭该文件。

with open('my_path/my_file.txt', 'r') as f:
    file_data = f.read()
该 with 关键字使你能够打开文件，对文件执行操作，并在缩进代码（在此示例中是读取文件）执行之后自动关闭文件。现在，我们不需要调用 f.close() 了！你只能在此缩进块中访问文件对象 f。
"""

# with open(camelot.txt) as song:
#     print(song.read(2))
#     print(song.read(8))
#     print(song.read())

# f = open('xiaoming.txt', 'r')
# file_data = f.read()
# # file_data = f.readline()
# # file_data = f.readlines()
# print(file_data)
# f.close()

"""很方便的是，Python 将使用语法 for line in file 循环访问文件中的各行内容。 我可以使用该语法创建列表中的行列表。因为每行依然包含换行符，因此我使用 .strip() 删掉换行符。

camelot_lines = []
with open("camelot.txt") as f:
    for line in f:
        camelot_lines.append(line.strip())

print(camelot_lines)
输出：

["We're the knights of the round table", "We dance whenever we're able"]
"""


"""练习：《飞翔的马戏团》 演员名单
你将创建一个演员名单，列出参演电视剧《巨蟒剧团之飞翔的马戏团》的演员。

写一个叫做 create_cast_list 的函数，该函数会接受文件名作为输入，并返回演员姓名列表。 它将运行文件 flying_circus_cast.txt（信息收集自 imdb.com）。文件的每行包含演员姓名、逗号，以及关于节目角色的一些（凌乱）信息。你只需提取姓名，并添加到列表中。你可以使用 .split() 方法处理每行。
"""
# def create_cast_list(filename):
#     cast_list = []
#     with open(filename) as f:
#         for line in f:
#             cast_list.append(line.split(",")[0])
#     #use with to open the file filename
#     #use the for loop syntax to process each line
#     #and add the actor name to cast_list

#     return cast_list

# cast_list = create_cast_list('flying_circus_cast.txt')
# for actor in cast_list:
#     print(actor)

# import math
# # x= math.exp(3)


# x= math.frexp(3)
# print(x)

"""练习：密码生成器
写一个叫做 generate_password 的函数，该函数会从提供的单词文件中随机选择三个单词，并将它们连接成一个字符串。我们已经在起始代码中提供了从文件中读取数据的代码，你需要利用这些部分构建一个密码。
"""
# # TODO: First import the `random` module
# import random

# # We begin with an empty `word_list`
# word_file = "words.txt"
# word_list = []

# # We fill up the word_list from the `words.txt` file
# with open(word_file,'r') as words:
#     for line in words:
# 		# remove white space and make everything lowercase
#         word = line.strip().lower()
# 		# don't include words that are too long or too short
#         if 3 < len(word) < 8:
#             word_list.append(word)

# # TODO: Add your function generate_password below
# # It should return a string consisting of three random words 
# # concatenated together without spaces
# def generate_password():
#     return random.choice(word_list) + random.choice(word_list) + random.choice(word_list)
	
    


# # Now we test the function
# print(generate_password())

"""
我们的推荐模块
Python 标准库包含大量模块！为了帮助你熟悉那些实用的模块，我们在下面筛选了一些我们推荐的 Python 标准库模块并解释为何我们喜欢使用它们！

csv：对于读取 csv 文件来说非常便利
collections：常见数据类型的实用扩展，包括 OrderedDict、defaultdict 和 namedtuple
random：生成假随机数字，随机打乱序列并选择随机项
string：关于字符串的更多函数。此模块还包括实用的字母集合，例如 string.digits（包含所有字符都是有效数字的字符串）。
re：通过正则表达式在字符串中进行模式匹配
math：一些标准数学函数
os：与操作系统交互
os.path：os 的子模块，用于操纵路径名称
sys：直接使用 Python 解释器
json：适用于读写 json 文件（面向网络开发）
希望你能用上这些模块！
"""

"""导入模块技巧
还有一些在不同情形下很有用的其他形式的 import 语句。

1.要从模块中导入单个函数或类：
from module_name import object_name
2.要从模块中导入多个单个对象：
from module_name import first_object, second_object
3.要重命名模块：
import module_name as new_name
4.要从模块中导入对象并重命名：
from module_name import object_name as new_name
5.要从模块中单个地导入所有对象（请勿这么做）：
from module_name import *
6.如果你真的想使用模块中的所有对象，请使用标准导入 module_name 语句并使用点记法访问每个对象。
import module_name
"""

"""使用 requirements.txt 文件
大型 Python 程序可能依赖于十几个第三方软件包。为了更轻松地分享这些程序，程序员经常会在叫做 requirements.txt 的文件中列出项目的依赖项。下面是一个 requirements.txt 文件示例。

beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1
该文件的每行包含软件包名称和版本号。版本号是可选项，但是通常都会包含。不同版本的库之间可能变化不大，可能截然不同，因此有必要使用程序作者在写程序时用到的库版本。

你可以使用 pip 一次性安装项目的所有依赖项，方法是在命令行中输入 pip install -r requirements.txt。
"""

"""实用的第三方软件包
能够安装并导入第三方库很有用，但是要成为优秀的程序员，还需要知道有哪些库可以使用。大家通常通过在线推荐或同事介绍了解实用的新库。如果你是一名 Python 编程新手，可能没有很多同事，因此为了帮助你了解入门信息，下面是优达学城工程师很喜欢使用的软件包列表。（可能部分网站在国内网络中无法打开）

IPython - 更好的交互式 Python 解释器
requests - 提供易于使用的方法来发出网络请求。适用于访问网络 API。
Flask - 一个小型框架，用于构建网络应用和 API。
Django - 一个功能更丰富的网络应用构建框架。Django 尤其适合设计复杂、内容丰富的网络应用。
Beautiful Soup - 用于解析 HTML 并从中提取信息。适合网页数据抽取。
pytest - 扩展了 Python 的内置断言，并且是最具单元性的模块。
PyYAML - 用于读写 YAML 文件。
NumPy - 用于使用 Python 进行科学计算的最基本软件包。它包含一个强大的 N 维数组对象和实用的线性代数功能等。
pandas - 包含高性能、数据结构和数据分析工具的库。尤其是，pandas 提供 dataframe！
matplotlib - 二维绘制库，会生成达到发布标准的高品质图片，并且采用各种硬拷贝格式和交互式环境。
ggplot - 另一种二维绘制库，基于 R's ggplot2 库。
Pillow - Python 图片库可以向你的 Python 解释器添加图片处理功能。
pyglet - 专门面向游戏开发的跨平台应用框架。
Pygame - 用于编写游戏的一系列 Python 模块。
pytz - Python 的世界时区定义。

"""