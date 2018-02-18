#Write a function that generates ten scores between 60 and 100


#random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...

def Scores_Grades(y):
    grade = []          #new data can be stored
    for x in range(0,y):
        import random
        points = random.randint(60,100)
        grade.append(points)
    for points in grade:            # "points" used instead of "i" because points index is established from random.randint
        if points in range(90, 101):
            print "Score: ", points, "your grade is A"    # "," lets you mix data types when concatenate(adding elements)
        elif points in range(80, 89):
            print "Score: ", points, "your grade is B"
        elif points in range(70,79):
            print "Score: ", points, "your grade is C"
        else:
            print "Score: ", points, "your grade is D"
Scores_Grades(10)