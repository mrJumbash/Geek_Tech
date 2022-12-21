'''Класс - Человек'''

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married
    '''Информация о человеке'''
    def __str__(self, introduce_myself):
        return f"Person name is {self.fullname}, his/her age - {self.age}, Family status - {self.is_married},"

'''Подкласс - Студент'''

class Student(Person):
    def __init__(self, fullname, age, is_married, marks={}):
        super().__init__(fullname, age, is_married)
        self.marks = marks
    '''Средняя Оценка'''
    def average_marks(self):
        self.average_marks = round(sum(self.marks.values()) / len(self.marks.values()), 1)
        return self.average_marks
    '''Информация Студента'''
    def __str__(self, introduce_myself):
        return f"Person name is {self.fullname}, his/her age - {self.age}, Family status - {self.is_married}, " \
               f"Lessons - Marks: {self.marks}"

'''Подкласс - Учитель'''

class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, experience=0):
        super().__init__(fullname, age, is_married)
        self.experience = experience
    '''Информация Учителя'''
    def __str__(self, introduce_myself):
        return f"Person name is {self.fullname}, his/her age - {self.age}, Family status - {self.is_married}, " \
               f"Exp: {self.experience} years, Salary - {Teacher.salary} som"
    '''Метод подсчета зарплаты'''
    def per_salary(self):
        exp = self.experience
        while exp != 0 and exp != 1 and exp != 2:
            exp -= 3
            Teacher.salary = round((Teacher.salary * 0.05) + Teacher.salary, 1)
        return Teacher.salary

'''Список студентов'''

def create_students(first_student, second_student, third_student):
    list_of_stu = []
    list_of_stu.append(first_student)
    list_of_stu.append(second_student)
    list_of_stu.append(third_student)
    return list_of_stu

'''Данные Студентов'''

info = create_students(Student('Кубаныч', "17", 'Холост', {'Math': 3, 'Bio': 5, 'English': 4}),
                Student('Михаил', "15", 'Холост', {'Math': 2, 'Bio': 5, 'English': 5}),
                Student('Пётр', "16", 'Холост', {'Math': 4, 'Bio': 4, 'English': 4}))
for obj in info:
    print(obj.__str__(introduce_myself=''))

'''Данные учителя'''

alex = Teacher('Алексей', "32", 'Женат', 11)
print(alex.per_salary())
print(alex.__str__(introduce_myself=''))