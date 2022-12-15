# Prompt the user to enter the number of students
num_students = int(input("Enter the number of students: "))

# Initialize variables to keep track of the lowest and total score
lowest_score = 100 # Assume that the maximum score is 100
total_score = 0

# Prompt the user to enter each student's score and find the lowest and average score
for i in range(num_students):
    student_score = int(input(f"Enter score for student {i+1}: "))
    lowest_score = min(lowest_score, student_score)
    total_score += student_score

# Calculate the average score
average_score = total_score / num_students

# Display the results
print(f"The lowest score is {lowest_score}")
print(f"The average score is {average_score}")
