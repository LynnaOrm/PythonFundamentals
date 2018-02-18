#Odd/Even, Create a function called odd_even that counts from 1 to 2000. As your loop executes have your program print the number of that iteration and specify whether
#it's an odd or even number. 

def odd_even():
    for num in range(1,200):
        if num % 2 == 0:
            print num, " This is an even number."
        else:
            print num, " This is an odd number."
odd_even()

#Multiply, create a function called "Multiply" that iterates through each value in a list ex. [2,4,10,16] and returns a list where each value is multiplied by 5. 

def multiply(arr, num):
    for mult in range(0, len(arr)):
        arr[mult] *= num
    return arr

a = [2, 4, 10, 16]

print multiply(a, 5)


#Hacker Challenge
def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
