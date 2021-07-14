# manifest = [("bananas", 15), ("mattresses", 24),
#             ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# # the code breaks the loop when weight exceeds or reaches the limit
# print("METHOD 1")
# weight = 0
# items = []
# for cargo_name, cargo_weight in manifest:
#     print("current weight: {}".format(weight))
#     if weight >= 100:
#         print("  breaking loop now!")
#         break
#     else:
#         print("  adding {} ({})".format(cargo_name, cargo_weight))
#         items.append(cargo_name)
#         weight += cargo_weight

# print("\nFinal Weight: {}".format(weight))
# print("Final Items: {}".format(items))

# # skips an iteration when adding an item would exceed the limit
# # breaks the loop if weight is exactly the value of the limit
# print("\nMETHOD 2")
# weight = 0
# items = []
# for cargo_name, cargo_weight in manifest:
#     print("current weight: {}".format(weight))
#     if weight >= 100:
#         print("  breaking from the loop now!")
#         break
#     elif weight + cargo_weight > 100:
#         print("  skipping {} ({})".format(cargo_name, cargo_weight))
#         continue
#     else:
#         print("  adding {} ({})".format(cargo_name, cargo_weight))
#         items.append(cargo_name)
#         weight += cargo_weight

# print("\nFinal Weight: {}".format(weight))
# print("Final Items: {}".format(items))

# # HINT: modify the headlines list to verify your loop works with different inputs
# headlines = ["Local Bear Eaten by Man",
#              "Legislature Announces New Laws",
#              "Peasant Discovers Violence Inherent in System",
#              "Cat Rescues Fireman Stuck in Tree",
#              "Brave Knight Runs Away",
#              "Papperbok Review: Totally Triffic"]

# news_ticker = ""
# # write your loop here
# for headline in headlines:
#     news_ticker += headline + " "
#     if len(news_ticker) >= 140:
#         news_ticker = news_ticker[:140]
#         break

# print(news_ticker)

# n = 0
# news_ticker = news_ticker+headlines[n]
# while len(news_ticker) <= 140:
#     print("1."+news_ticker,len(news_ticker))
#     if len(news_ticker)+1+len(headlines[n+1]) >=140:
#         print("2."+news_ticker,len(news_ticker))
#         break
#     else:
#         news_ticker= news_ticker + " " + headlines[n+1]
#         n+=1
#         print("3."+news_ticker,len(news_ticker))
# m= 140-len(news_ticker)
# news_ticker=news_ticker+" "+headlines[n+1][0:m-1]
# print(news_ticker,len(news_ticker))

# letters = ['a', 'b', 'c']
# nums = [1, 2, 3]

# for letter, num in zip(letters, nums):
#     print("{}: {}".format(letter, num))


# some_list = [('a', 1), ('b', 2), ('c', 3)]
# letters, nums = zip(*some_list)

# letters = ['a', 'b', 'c', 'd', 'e']
# for i, letter in enumerate(letters):
#     print(i, letter)


# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

# points = []
# # write your for loop here
# for label,x,y,z in zip(labels,x_coord,y_coord,z_coord):
#     points.append([label,x,y,z])


# for point in points:
#     print("{}:{},{},{}".format(point[0],point[1],point[2],point[3]))

# x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
# y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
# z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
# labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]

# points = []
# # write your for loop here
# for label,x,y,z in zip(labels,x_coord,y_coord,z_coord):
#     points.append("{}: {}, {}, {}".format(*[label,x,y,z]))
# for point in points:
#     print(point)

# cast_names = ["Barney", "Robin", "Ted", "Lily", "Marshall"]
# cast_heights = [72, 68, 72, 66, 76]
# for cast in zip(cast_names,cast_heights):
#     print("{}:{}".format(*cast))
#     # cast = "{}:{}".format(*cast)
# # replace with your code
# # print(cast)

# cast = (("Barney", 72), ("Robin", 68), ("Ted", 72), ("Lily", 66), ("Marshall", 76))

# # define names and heights here
# names,heights = zip(*cast)

# print(names)
# print(heights)

# data = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (9, 10, 11))

# data_transpose = tuple(zip(*data))
# print(data_transpose)


# cast = ["Barney Stinson", "Robin Scherbatsky", "Ted Mosby", "Lily Aldrin", "Marshall Eriksen"]
# heights = [72, 68, 72, 66, 76]

# # write your for loop here
# for i,n in enumerate(cast):
#     cast[i]=n+" "+str(heights[i])
# print(cast)

# cities=["xiaoming","nano"]
# capitalized_cities = []
# # for city in cities:
# #     capitalized_cities.append(city.title())
# capitalized_cities = [city.title() for city in cities]
# print(capitalized_cities)

# squares = [x**2 for x in range(9) if x % 2 == 0]
# print(squares)

# squares = [x**2 if x % 2 == 0 else x + 3 for x in range(9)]
# print(squares)

# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# first_names = [name.split()[0].lower() for name in names]
# # write your list comprehension here
# print(first_names)


# multiples_3 = [(x+1)*3 for x in range(20)]
# print(multiples_3)

# scores = {
#              "Rick Sanchez": 70,
#              "Morty Smith": 35,
#              "Summer Smith": 82,
#              "Jerry Smith": 23,
#              "Beth Smith": 98
#           }
# print(scores)
# # passed = [name for name,score in scores.items() if score >= 65 ] 
# # print(passed)
# print(scores.items())