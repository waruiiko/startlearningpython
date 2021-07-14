# # write your function here
# def population_density(population,land_area):
#     return population/land_area

# # test cases for your function
# test1 = population_density(10, 1)
# expected_result1 = 10
# print("expected result: {}, actual result: {}".format(expected_result1, test1))

# test2 = population_density(864816, 121.4)
# expected_result2 = 7123.6902801
# print("expected result: {}, actual result: {}".format(expected_result2, test2))

"""
写一个叫做 readable_timedelta 的函数，该函数有一个参数：整数 days，并返回一个表示由多少周多少天组成的字符串。例如 readable_timedelta(10) 应返回“1 week(s) and 3 day(s).”。 
"""
# # write your function here
# def readable_timedelta(days):
#     m = int(days/7)
#     n = days % 7
#     return "{} week(s) and {} day(s).".format(m,n)

# # test your function
# print(readable_timedelta(10))

"""lambda表达式"""
# def multiply(x, y):
#     return x * y

# double = lambda x, y: x * y

"""
练习：Lambda 与 Map
map() 是一个高阶内置函数，接受函数和可迭代对象作为输入，并返回一个将该函数应用到可迭代对象的每个元素的迭代器。下面的代码使用 map() 计算 numbers 中每个列表的均值，并创建列表 averages。测试运行这段代码，看看结果如何。

通过将 mean 函数替换为在 map() 的调用中定义的 lambda 表达式，重写这段代码，使代码更简练。
"""
# numbers = [
#               [34, 63, 88, 71, 29],
#               [90, 78, 51, 27, 45],
#               [63, 37, 85, 46, 22],
#               [51, 22, 34, 11, 18]
#            ]

# # def mean(num_list):
# #     return sum(num_list) / len(num_list)

# # averages = list(map(mean, numbers))
# averages = list(map(lambda num_list:sum(num_list)/len(num_list),numbers))
# print(averages)

"""
练习：Lambda 与 Filter
filter() 是一个高阶内置函数，接受函数和可迭代对象作为输入，并返回一个由可迭代对象中的特定元素（该函数针对该元素会返回 True）组成的迭代器。下面的代码使用 filter() 从 cities 中获取长度少于 10 个字符的名称以创建列表 short_cities。测试运行这段代码，看看结果如何。

通过将 is_short 函数替换为在 filter() 的调用中定义的 lambda 表达式，重写这段代码，使代码更简练。
"""
cities = ["New York City", "Los Angeles", "Chicago", "Mountain View", "Denver", "Boston"]

def is_short(name):
    return len(name) < 10

short_cities = list(filter(is_short, cities))
print(short_cities)