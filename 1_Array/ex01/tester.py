from array2D import slice_me

GREEN = "\033[92m"
RED = "\033[1m\033[91m"
DEFAULT = "\033[0m"

print(f"{RED} -------------- \n|    TEST 1    |\n -------------- {DEFAULT}")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
start = 0
end = 2
print(f"{GREEN}input:\n{DEFAULT}family -> {family}\n\
start -> {start}\nend -> {end}")
print(f"\n{GREEN}slice_me:{DEFAULT}")
print(slice_me(family, start, end))

print(f"\n{RED} -------------- \n|    TEST 2    |\n -------------- {DEFAULT}")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
start = 1
end = -2
print(f"{GREEN}input:\n{DEFAULT}family -> {family}\n\
start -> {start}\nend -> {end}")
print(f"\n{GREEN}slice_me:{DEFAULT}")
print(slice_me(family, start, end))

print(f"\n{RED} -------------- \n|    TEST 3    |\n -------------- {DEFAULT}")
family = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
start = 1
end = 2
print(f"{GREEN}input:\n{DEFAULT}family -> {family}\n\
start -> {start}\nend -> {end}")
print(f"\n{GREEN}slice_me:{DEFAULT}")
print(slice_me(family, start, end))

print(f"\n{RED} -------------- \n|    TEST 4    |\n -------------- {DEFAULT}")
family = [[1.80, 78.4, 4.2], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
start = 1
end = 2
print(f"{GREEN}input:\n{DEFAULT}family -> {family}\n\
start -> {start}\nend -> {end}")
print(f"\n{GREEN}slice_me:{DEFAULT}")
print(slice_me(family, start, end))

print(f"\n{RED} -------------- \n|    TEST 5    |\n -------------- {DEFAULT}")
family = []
start = 1
end = 3
print(f"{GREEN}input:\n{DEFAULT}family -> {family}\n\
start -> {start}\nend -> {end}")
print(f"\n{GREEN}slice_me:{DEFAULT}")
print(slice_me(family, start, end))

print(f"\n{RED} -------------- \n|    TEST 6    |\n -------------- {DEFAULT}")
family = [[1.80, 78.4], [2.15, 102.7], [2.10, 98.5], [1.88, 75.2]]
start = "hello"
end = 1
print(f"{GREEN}input:\n{DEFAULT}family -> {family}\n\
start -> {start}\nend -> {end}")
print(f"\n{GREEN}slice_me:{DEFAULT}")
print(slice_me(family, start, end))
