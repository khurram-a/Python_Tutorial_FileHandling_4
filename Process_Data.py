#---------------------------------------------------
#------Created  : 01/01/2025 - Khurram Asif
#------Modified : 
#------Description : Python file handling tutorial 4
#----------------------------------------------------


#-----Define Funtions---------------
def calculate_average(scores):
    return sum(scores) / len(scores)

def assign_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

#-----End Funtions---------------



# importing csv module
import csv



# initializing the students list
students = []

# reading csv file
with open('Students.csv', 'r') as file:
        # creating a csv reader object
        reader = csv.reader(file)

        # Read the header (first row)
        header = next(reader) 
        
        # extracting field names through first row
        for row in reader:
            name, math, science, english = row
            average = calculate_average([int(math), int(science), int(english)])
            grade = assign_grade(average)
            students.append([name, math, science, english, average, grade])

with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Science', 'English', 'Average', 'Grade'])
        writer.writerows(students)

print('Results saved to student_results.csv')




