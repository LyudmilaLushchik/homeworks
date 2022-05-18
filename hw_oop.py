class Student:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def add_courses(self, course_name):
        self.courses_in_progress.append(course_name) 

    def add_courses_finished(self, course_name):
        self.finished_courses.append(course_name)   

    def add_in_list(self, income_list):
        self_dict = dict()
        self_dict.setdefault('name', self.name)
        self_dict.setdefault('surname', self.surname)
        self_dict.setdefault('grades', self.grades)
        income_list.append(self_dict) 
    
    def _calc_avg_grade(self):
        if len(self.grades) != 0:
            grades_sum = 0
            grades_count = 0
            for _, item in self.grades.items():
                grades_sum += sum(item)
                grades_count += len(item)
                res = (round(grades_sum / grades_count, 2))
            return res
        else:
            res = 0
            return res
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Не студент!')
            return
        return self._calc_avg_grade() < other._calc_avg_grade()
     
    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and \
            course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'''\n   Имя, Фамилия: {self.name} {self.surname} 
        \tСредняя оценка за домашние задания: {self._calc_avg_grade()} 
        \tКурсы в процессе изучения: {', '.join(self.courses_in_progress)} 
        \tЗавершенные курсы: {', '.join(self.finished_courses)}'''
        return res
 
     
class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []    
        
    def add_courses(self, course_name):
        self.courses_attached.append(course_name)     


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {} 

    def add_in_list(self, income_list):
        Student.add_in_list(self, income_list)
    
    def _calc_avg_grade(self):
        # Попробовала от класса Студент унаследовать этот метод, но тогда на выходе None..?
        # Student._calc_avg_grade(self)        
        if len(self.grades) != 0:
            grades_sum = 0
            grades_count = 0
            for _, item in self.grades.items():
                grades_sum += sum(item)
                grades_count += len(item)
                res = (round(grades_sum / grades_count, 2))
            return res
        else:
            return 0
        
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Не лектор!')
            return
        return self._calc_avg_grade() < other._calc_avg_grade()   

    def __str__(self):
        res = f'''\n   Имя, Фамилия: {self.name} {self.surname} 
        \tСредняя оценка за лекции: {self._calc_avg_grade()}''' 
        return res


class Reviewer(Mentor):
    
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and \
            course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'\n   Имя, Фамилия: {self.name} {self.surname}'
        return res

students_list = []
lecturers_list = []
#Создание экземпляров классов и применение к ним всех методов:
stud1 = Student('Василий', 'Тёркин')
stud1.add_courses('Стрельба')
stud1.add_courses('Физподготовка')
stud1.add_courses_finished('Окопы')
stud1.add_in_list(students_list)

stud2 = Student('Роза', 'Шанина')
stud2.add_courses('Стрельба')
stud2.add_courses('Физподготовка')
stud2.add_courses_finished('Маскировка')
stud2.add_in_list(students_list)

lect1 = Lecturer('Иван', 'Иванов')
lect1.add_courses('Маскировка')
lect1.add_courses('Физподготовка')
lect1.add_in_list(lecturers_list)

lect2 = Lecturer('Пётр', 'Петров')
lect2.add_courses('Стрельба')
lect2.add_courses('Окопы')
lect2.add_in_list(lecturers_list)

rev1 = Reviewer('Александр', 'Александров')
rev1.add_courses('Стрельба')
rev2 = Reviewer('Филипп', 'Филиппов')
rev2.add_courses('Физподготовка')

rev1.rate_hw(stud1, 'Стрельба', 8)
rev1.rate_hw(stud1, 'Стрельба', 9)
rev1.rate_hw(stud2, 'Стрельба', 7)
rev1.rate_hw(stud2, 'Стрельба', 9)
rev2.rate_hw(stud2, 'Физподготовка', 10)
rev2.rate_hw(stud2, 'Физподготовка', 7)
rev2.rate_hw(stud1, 'Окопы', 8) # Иван уже закончил курс, оценка не выставится
rev2.rate_hw(rev1, 'Физподготовка', 10) # Александр не студент, оценка не выставится

stud1.rate_lecture(lect1, 'Физподготовка', 7)
stud1.rate_lecture(lect1, 'Физподготовка', 8)
stud1.rate_lecture(lect2, 'Стрельба', 6)
stud1.rate_lecture(lect2, 'Стрельба', 7)
stud2.rate_lecture(lect1, 'Физподготовка', 9)
stud2.rate_lecture(lect1, 'Маскировка', 10) # Роза ставит оценку за завершённый курс, оценка не выставится
stud2.rate_lecture(lect1, 'Окопы', 10) # Роза ставит оценку за курс, на котором не обучается, оценка не выставится

print('\nИнформация о студентах:')
print(stud1)
print(stud2)
print('\nИнформация о лекторах:')
print(lect1)
print(lect2)
print('\nИнформация о проверяющих:')
print(rev1)
print(rev2)
print()
print(f'Учится ли Василий хуже Розы?: {stud1 < stud2}')
print(f'Преподаёт ли Иван Иваныч хуже Петра Петровича?: {lect1 < lect2}')

def calc_avg_hw_grade_on_course(students, course_name):
    avg_sum = 0
    count_stud = 0
    students_on_course = [student for student in students if course_name in student['grades'].keys()]
    if len(students_on_course) > 0:
        for student in students_on_course: 
            avg_sum += sum(student['grades'].get(course_name)) / len(student['grades'].get(course_name))
            count_stud += 1
        return round(avg_sum / count_stud, 2)    
    else:
        return 0

print(f'Список студентов: \n{students_list}')
print(f'Средняя оценка за дз на курсе по стрельбе: {calc_avg_hw_grade_on_course(students_list, "Стрельба")}')
print(f'Средняя оценка за дз на курсе по физподготовке: {calc_avg_hw_grade_on_course(students_list, "Физподготовка")}')
print(f'Средняя оценка за дз на невостребованном курсе вязания: {calc_avg_hw_grade_on_course(students_list, "вязание")}')

def calc_avg_lect_grade_on_course(lecturers, course_name):
    count_stud = 0
    avg_sum = 0
    for lecturer in lecturers:
        avg = 0
        list_gr = []
        if course_name in lecturer['grades'].keys():
            list_gr = lecturer['grades'].get(course_name)
            count_stud += 1
        if len(list_gr) > 0:           
            avg = round(sum(list_gr) / len(list_gr), 2)             
        avg_sum += avg
    if count_stud > 0:        
        avg_sum = avg_sum / count_stud  
    return avg_sum

print(f'Список лекторов: \n{lecturers_list}')
print(f'Средняя оценка лекций по стрельбе: {calc_avg_lect_grade_on_course(lecturers_list, "Стрельба")}')
print(f'Средняя оценка лекций по физподготовке: {calc_avg_lect_grade_on_course(lecturers_list, "Физподготовка")}')
print(f'Средняя оценка лекций по неоценённому копанию окопов: {calc_avg_lect_grade_on_course(lecturers_list, "Окопы")}')