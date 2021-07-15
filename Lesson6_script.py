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
def create_groups(items, num_groups):
   try:
    size = len(items) // num_groups
   except ZeroDivisionError as e:
      print("WARNING: Returning empty list. Please use a nonzero number!!!{}!!!.".format(e))
      return []
   else:
    groups = []
    for i in range(0, len(items), size):
        groups.append(items[i:i + size])
    return groups
   finally:
    print("{} groups returned.".format(num_groups))
    

print("Creating 6 groups...")
for group in create_groups(range(32), 6):
    print(list(group))

print("\nCreating 0 groups...")
for group in create_groups(range(32), 0):
    print(list(group))

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