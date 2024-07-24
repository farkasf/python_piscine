from ft_calculator import calculator

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a, b)
calculator.add_vec(a, b)
calculator.sous_vec(a, b)

GREEN = "\033[92m"
DEF = "\033[0m"

print(f"\n{GREEN}--- CUSTOM 1 ---{DEF}")
c = [20, 30, 40]
d = [10, 10, 10]
print(f"c: {c} || d: {d}")
calculator.dotproduct(c, d)
calculator.add_vec(c, d)
calculator.sous_vec(c, d)

print(f"\n{GREEN}--- CUSTOM 2 ---{DEF}")
e = [1, 10, 100]
f = [42, 42, 42]
print(f"e: {e} || f: {f}")
calculator.dotproduct(e, f)
calculator.add_vec(e, f)
calculator.sous_vec(e, f)
