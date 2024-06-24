#1


class Student:
    def __init__(self, name, group):
        self.name = name
        self.group = group

    def show(self):
        return f"Студент {self.name}, группа {self.group}"

    def __del__(self):
        print(f"Экземпляр {self.name} удален")


student1 = Student(name="Данияр", group="ПОВТ1-24")


print(student1.show())

del student1



