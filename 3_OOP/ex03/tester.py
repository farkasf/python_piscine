from ft_calculator import calculator

v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v1 + 5
print("---")
v2 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
v2 * 5
print("---")
v3 = calculator([10.0, 15.0, 20.0])
v3 - 5
v3 / 5

GREEN = "\033[92m"
DEF = "\033[0m"

print(f"\n{GREEN}--- CUSTOM v4 ---{DEF}")
v4 = calculator([6.0, 7.0, 8.0, 9.0, 10.0, 11.0])
print(f"original: {v4}")
print("v4 - 5:", end=" ")
v4 - 5
print("v4 * -1:", end=" ")
v4 * -1
print("v4 / 2:", end=" ")
v4 / 2

print(f"\n{GREEN}--- CUSTOM v5 ---{DEF}")
v5 = calculator([24.0, 25.0, 26.0, 27.0, 28.0, 29.0])
print(f"original: {v5}")
print("v5 + 18:", end=" ")
v5 + 18
print("v5 * 10:", end=" ")
v5 * 10
print("v5 / 0:", end=" ")
v5 / 0
