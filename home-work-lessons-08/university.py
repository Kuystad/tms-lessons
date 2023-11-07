from student import Student
students = [Student('Anton', 8),
            Student('Max', 4),
            Student('Eliz', 9)]
def calc_summ_scholarship(students):
    total_scholarship = 0
    for student in students:
        total_scholarship += student.get_scholarship()
    return f'{total_scholarship} dollars.'

def get_excellent_student_count(students):
    excellent_count = 0
    for student in students:
        if student.is_excellent():
            excellent_count += 1
    return excellent_count

print(calc_summ_scholarship(students))
print(get_excellent_student_count(students))
