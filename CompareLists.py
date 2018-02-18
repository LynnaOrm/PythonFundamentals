#Write a program that compares two lists and prints a message depending on if the inouts are identical or not.
#Program should be able to accept and compare two lists: list_one and list_two. If boths lists are identical print "The lists are the same." if they are not identical print
#"The lists are not the same." try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

if list_one == list_two:
    print "The lists are indentical"
elif list_one != list_two:
    print "These lists are not the same"


list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

if list_one == list_two:
    print "The lists are indentical"
elif list_one != list_two:
    print "These lists are not the same"


list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

if list_one == list_two:
    print "The lists are indentical"
elif list_one != list_two:
    print "These lists are not the same"

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

if list_one == list_two:
    print "The lists are indentical"
elif list_one != list_two:
    print "These lists are not the same"
