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