class Student:
    def __init__(self, name, fives, tens, twenties):
        self.name = name
        self.fives = fives
        self.tens = tens
        self.twenties = twenties

    def getMoney(self):
        return self.fives * 5 + self.tens * 10 + self.twenties

    def __str__(self):
        return self.name + " " + str(self.getMoney())



def most_money(students):
    student_name = ''
    sum_student = 0
    check_all = 0
    for student in students:
        current_sum = student.fives * 5 + student.tens * 10 + student.twenties * 20
        if current_sum > sum_student:
            sum_student = current_sum
            student_name = student.name
        elif current_sum == sum_student:
            if check_all == 0:
                check_all += 2
            else:
                check_all += 1

    if check_all == len(students):
        return 'all'

    return student_name



phil = Student("Phil", 2, 2, 1)
cam = Student("Cameron", 2, 2, 0)
geoff = Student("Geoff", 0, 3, 0)


print(most_money([cam, geoff, phil]))
print(most_money([cam, geoff]))
print(most_money([geoff]))
