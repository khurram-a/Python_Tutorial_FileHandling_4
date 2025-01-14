#---------------------------------------------------
#------Created  : 01/01/2025 - Khurram Asif
#------Modified : 14/01/2025 - Khurram Asif
#------Modification Reason : Change the headings and calcs in the output file
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
            #average = calculate_average([int(math), int(science), int(english)])
            m_grade = assign_grade(int(math))
            s_grade = assign_grade(int(science))
            e_grade = assign_grade(int(english))
            students.append([name, math, m_grade, science, s_grade, english, e_grade])

with open('Student_Results.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Math', 'Math_Grade','Science','Science_Grade', 'English', 'English_Grade'])
        writer.writerows(students)

print('Results saved to student_results.csv')




