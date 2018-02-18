#Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.
#hint every word containing the letter "o"

word_list = ['Hello','world','my','name','is','Lynna']
char = 'o'

def characters(word_list, char):
    new_list= []

    for i in range(0, len(word_list)):
        if word_list[i].find(char) != -1:
            new_list.append(word_list[i])
    print new_list

characters(word_list, char)