def calculate_grade():
    marks = []
    for i in range(5):
        mark = int(input("Enter subject mark: "))
        marks.append(mark)
    average = sum(marks) / len(marks)
    print("Marks:", marks)
    print("Average:", average)
    if average >= 90:
        print("Grade: A")
    elif average >= 75:
        print("Grade: B")
    elif average >= 50:
        print("Grade: C")
    else:
        print("Grade: F")
calculate_grade()
