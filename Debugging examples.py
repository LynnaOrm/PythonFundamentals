#Debugging Example

def multiply(arr,num):
    for x in arr:
        x *= num
    return arr


a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16]

#You might have discovered this problem yourself and had to work it out. 
# Without some more information you might have had a hard time tracking down where the problem was occurring. 
# We can get information by using print statements to display that data in the terminal.
#The first thing to do is to step through your code in the order it runs and try to figure out if there are any unknowns. 
#Let's step through the example code. What runs first? The first line is a function, so the interpreter runs in this order:

  def multiply(arr,num): #don't go inside the function until the function is called
  a = [2,4,10,16]
  b = multiply(a,5) # now our function executes; what is a function call equal to?
  print b # and the resulting value is printed

#So far, we don't have too many questions. Here's what happened, in order:

declare a function
instantiate a variable whose value is a list containing integers
print the output of that function by calling it after a print statement

def multiply(arr,num):
    print arr, num
    for x in arr:
        x *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16] 5
>>>[2,4,10,16]

Our output confirms that our code is doing everything we've tested for so far. Now to prove that our next line runs as expected. 
This line: for x in arr: indicates the start of a for loop. Let's confirm we're entering the loop, 
and that "x" contains the value we expect. Now our code looks like this:

def multiply(arr,num):
    print arr, num
    for x in arr:
        print x
        x *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16] 5
>>>2
>>>4
>>>10
>>>16
>>>[2,4,10,16]

def multiply(arr,num):
    print arr, num # output should be [2,4,10,16] 5
    for x in arr:
        print x
        x *= num
        print x
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16] 5
>>>2
>>>4
>>>10
>>>16
>>>10
>>>20
>>>50
>>>80

def multiply(arr,num):
    print arr, num # output should be [2,4,10,16] 5
    for x in arr:
        print x
        x *= num
        print arr
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[2,4,10,16] 5
>>>2
>>>4
>>>10
>>>16
>>>[2,4,10,16]
>>>[2,4,10,16]
>>>[2,4,10,16]
>>>[2,4,10,16]

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
>>>[10,20,50,80]
Learning to use print statements to their greatest advantage and how to correctly search for answers are not one-time skills. 
You can't just do this assignment and move on, or assume that we'll tell you when you need to use these skills.
 What we've introduced here is a skill set you'll use for every assignment in all of your code forever. Now is the time to start practicing, 
 because the better you get, the more self-sufficient you become.