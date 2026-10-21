####STUDENT REPORT CARD PROJECT
subject = ['TAMIL', 'ENGLISH', 'MATHS', 'SCIENCE', 'SOCIAL']
name = input(" Name : ")
standard = input("Standard :")
mark = {}
#looping to enter the maks for each subject
for i in range(len(subject)):
    marks=int(input('Enter the marks obtained for '+ subject[i] + ':'))
    mark[subject[i]]=marks
    
#control flow statements for grade of the marks
print('***** STUDENT REPORT CARD ***')
print("Name :",name)
print("Class :",standard)
for sub, marks in mark.items():
        if marks>=90 and marks<=100:
            grade = 'O'
        elif marks>=80 and marks<=89:
            grade = 'A'
        elif marks>=70 and marks<=79:
            grade = 'B'
        elif marks>=60 and marks<=69:
            grade = 'C'
        elif marks>=50 and marks<=59:
            grade = 'D'
        elif marks>=1 and marks<=49:
            grade = 'F'
        else:
            print("Enter the correct mark")
        print(sub, ':', marks, 'Grade:', grade)
        
