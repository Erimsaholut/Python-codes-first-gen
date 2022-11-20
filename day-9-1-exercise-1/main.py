student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

for i in student_scores:
    if student_scores[i] > 90:
        student_scores[i] = "Outstanding"
    elif student_scores[i] > 80:
        student_scores[i] = "Exceeds Expectations"
    elif student_scores[i] > 70:
        student_scores[i] = "Acceptable"
    else:
        student_scores[i] = "Fail"
    student_grades[i] = student_scores[i]

    

        
        
    

#TODO-2: Write your code below to add the grades to student_grades.👇

    

# 🚨 Don't change the code below 👇

print(student_grades)





