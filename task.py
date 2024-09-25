def task():

    # grade should be a tuple containing student name (str), subject (str) and score (int)
    name= input("Enter a name: ")
    subject= input("Enter subject: ")
    score= int(input("Enter a score out of a 100: "))

    grade= (name, subject, score)
    return grade
print(task())