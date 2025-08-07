## class Name:First letter Cap<>
class Student:
    name="Sam"
    email="sam@sam.com"
    phone="1234567890"

#student1
student1=Student()
student2=Student()


print("student 1")
print("name",student1.name)
print("email",student1.email)
print("phone",student1.phone)

print("student 2")
print("name",student1.name)
print("email",student1.email)
print("phone",student1.phone)

for key, value in student1.__dict__.items():
    print(key,value)