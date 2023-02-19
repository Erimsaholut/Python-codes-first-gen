# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
top = 0
kiş = 0
for a in student_heights:
  top += a
  kiş += 1
ort = top/kiş
print(round(ort))

