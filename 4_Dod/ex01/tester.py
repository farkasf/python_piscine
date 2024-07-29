from in_out import outer
from in_out import square
from in_out import pow


my_counter = outer(3, square)
print(my_counter())
print(my_counter())
print(my_counter())
print("---")
another_counter = outer(1.5, pow)
print(another_counter())
print(another_counter())
print(another_counter())

print("---")
one_more = outer(pow(2), square)
for _ in range(5):
    print(one_more())

print("---")
last_one = outer(0.5, pow)
for _ in range(3):
    print(last_one())
