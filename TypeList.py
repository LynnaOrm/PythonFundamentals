#Type List, Write a program that takes a list and prints a message for each element in the list, based on that element's data type.
#program input will always be a list, for each item test it's data type. If string concatenate it onto a new string. If its a number add it to a running sum.
#At the end of the program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise print "mixed."


mixed_list = ['Purple', 23, 'Turqoise', 33, 'Pink']
integer_list = [10,11,12,13,14]
string_list = ['Chicken', 'Nuggets']


def identify_list_type(lst):
    new_string = ''
    total = 0

    for value in lst:
        if isinstance(value, int) or isinstance(value, float):
            total += value
        elif isinstance(value, str):
            new_string += value

    if new_string and total:
        print "The list you entered is of mixed type"
        print "String:", new_string
        print "Total:", total

    elif new_string:
        print "The list you entered is of string type"
        print "String:",new_string

    else:
        print "The list you entered is of integer type"
        print "Total:", total

print identify_list_type(mixed_list)
print identify_list_type(integer_list)
print identify_list_type(string_list)

