from new_student import Student

student = Student(name="Edward", surname="agle")
print(student)
print("---")

try:
    student = Student(name="Edward", surname="agle", id="toto")
    print(student)
except TypeError as e:
    print(f"TypeError: {e}")
print("---")

try:
    student = Student(name="Edward", surname="agle", login="admin")
    print(student)
except TypeError as e:
    print(f"TypeError: {e}")
print("---")

try:
    student = Student(name="filip", surname="Farkas")
    print(student)
except TypeError as e:
    print(f"TypeError: {e}")
