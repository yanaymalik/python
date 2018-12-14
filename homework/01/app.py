class student:
    sum_score = 0
    sum_ages = 0
    sum_students = 0

    def __init__(self, score, age):
        self.score = score
        self.age = age
        student.sum_score += score
        student.sum_ages += age
        student.sum_students += 1

    def score_avg(self):
        return student.sum_score/student.sum_students

    def age_avg(self):
        return student.sum_ages/student.sum_students


scores = [100,95,90,85]
ages = [25,24,23,22]
s = ["","","",""]
i = 0
while i < 4:
    s = student(scores[i],ages[i]) 
    i += 1
j = 0
while j < 4:
    print("student number: {0}\nstudent score: {1}\nstudent age: {2}".format(j+1,scores[j], ages[j]))
    print("~~~~~~~~~~~~~")
    j += 1
print("The scores average: {0}\nThe age average {1}".format(s.score_avg(),s.age_avg()))


