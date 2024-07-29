from callLimit import callLimit


@callLimit(3)
def f():
    print("f()")


@callLimit(1)
def g():
    print("g()")


for i in range(3):
    f()
    g()

print("---")


@callLimit(10)
def knock(i: int) -> None:
    print("HaHa" * i)


for i in range(1, 12):
    knock(i)
