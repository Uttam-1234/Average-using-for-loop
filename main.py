# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height=0
for height_sum in student_heights:
  total_height = total_height + height_sum
total_number_students = 0
for number in student_heights:
  total_number_students = total_number_students+1
average_height = total_height/total_number_students
rounded_average_height = round(average_height)
print(rounded_average_height)
