from give_bmi import give_bmi
from give_bmi import apply_limit

GREEN = "\033[92m"
RED = "\033[1m\033[91m"
DEFAULT = "\033[0m"

print(f"{RED} -------------- \n|    TEST 1    |\n -------------- {DEFAULT}")
height = [2.71, 1.15]
weight = [165.3, 38.4]
print(f"{GREEN}input:\n{DEFAULT}height -> {height}\nweight -> {weight}\n")
print(f"{GREEN}give_bmi:{DEFAULT}")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(f"\n{GREEN}apply_limit (26):{DEFAULT}")
print(apply_limit(bmi, 26))

print(f"\n{RED} -------------- \n|    TEST 2    |\n -------------- {DEFAULT}")
height = [1.85, 1.15, 1.5]
weight = [120.3, 38.4, 41.5]
print(f"{GREEN}input:\n{DEFAULT}height -> {height}\nweight -> {weight}\n")
print(f"{GREEN}give_bmi:{DEFAULT}")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(f"\n{GREEN}apply_limit (26):{DEFAULT}")
print(apply_limit(bmi, 26))

print(f"\n{RED} -------------- \n|    TEST 3    |\n -------------- {DEFAULT}")
height = []
weight = [120.3, 38.4, 57.5]
print(f"{GREEN}input:\n{DEFAULT}height -> {height}\nweight -> {weight}\n")
print(f"{GREEN}give_bmi:{DEFAULT}")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(f"\n{GREEN}apply_limit (26):{DEFAULT}")
print(apply_limit(bmi, 26))

print(f"\n{RED} -------------- \n|    TEST 4    |\n -------------- {DEFAULT}")
height = [1.85, 1.15, 1.5]
weight = []
print(f"{GREEN}input:\n{DEFAULT}height -> {height}\nweight -> {weight}\n")
print(f"{GREEN}give_bmi:{DEFAULT}")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(f"\n{GREEN}apply_limit (26):{DEFAULT}")
print(apply_limit(bmi, 26))

print(f"\n{RED} -------------- \n|    TEST 5    |\n -------------- {DEFAULT}")
height = [1.85, 1.15, 1.5]
weight = [120.3, 38.4]
print(f"{GREEN}input:\n{DEFAULT}height -> {height}\nweight -> {weight}\n")
print(f"{GREEN}give_bmi:{DEFAULT}")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(f"\n{GREEN}apply_limit (26):{DEFAULT}")
print(apply_limit(bmi, 26))

print(f"\n{RED} -------------- \n|    TEST 6    |\n -------------- {DEFAULT}")
height = ["hello", "world", "!"]
weight = [120.3, 38.4, 57.5]
print(f"{GREEN}input:\n{DEFAULT}height -> {height}\nweight -> {weight}\n")
print(f"{GREEN}give_bmi:{DEFAULT}")
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(f"\n{GREEN}apply_limit (26):{DEFAULT}")
print(apply_limit(bmi, 26))
