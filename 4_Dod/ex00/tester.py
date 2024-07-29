from statistics import ft_statistics

BLUE = "\033[94m"
RED = "\033[93m"
RED = "\033[91m"
GREEN = "\033[92m"
DEF = "\033[0m"

ft_statistics(
    1, 42, 360, 11, 64,
    toto="mean", tutu="median", tata="quartile"
)
print("-----")
ft_statistics(
    5, 75, 450, 18, 597, 27474, 48575,
    hello="std", world="var"
)
print("-----")
ft_statistics(
    5, 75, 450, 18, 597, 27474, 48575,
    ejfhhe="heheh", ejdjdejn="kdekem"
)
print("-----")
ft_statistics(toto="mean", tutu="median", tata="quartile")


print(f"\n{RED}--- TEST F1 ---{DEF}")
print(f"\n{GREEN}[EXPECTED] mean : 5.2 | median : 5 | \
quartile : [3.0, 7.0]\n{DEF}")
ft_statistics(
    3, 7, 5, 9, 2,
    mean="mean", blah="what", median="median", quartile="quartile"
)

print(f"\n{RED}--- TEST F2 ---{DEF}")
print(f"\n{GREEN}[EXPECTED] std : 28.722813232690143 | var : 825.0\n{DEF}")
ft_statistics(
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100,
    std="std", var="var"
)

print(f"\n{RED}--- TEST F3 ---{DEF}")
print(f"\n{GREEN}[EXPECTED] TypeError: Arguments must be numbers.\n{DEF}")
ft_statistics(
    10, 20, 30, 40, "Marvin", 50,
    std="std", var="var"
)

print(f"\n{RED}--- TEST F4 ---{DEF}")
print(f"\n{GREEN}[EXPECTED] mean : 42.0 | median : 42 | \
quartile : [42.0, 42.0] | std : 0.0 | var : 0.0\n{DEF}")
ft_statistics(
    42,
    mean="mean", median="median", quartile="quartile", std="std", var="var"
)

print(f"\n{RED}--- TEST F5 ---{DEF}")
print(f"\n{GREEN}[EXPECTED] mean : 100.2 | median : 21 | \
quartile : [13.0, 42.0] | std : 160.37381332374684 | \
var : 25719.760000000002\n{DEF}")
ft_statistics(
    5, 13, 21, 42, 420,
    mean="mean", median="median", quartile="quartile", std="std", var="var"
)
