#Find and Replace, replace day with month.
words = "it's thanksgiving day. It's my birthday, too!"
print words.find('day')
newWord = words.replace('day','month')
print newWord

#Min and Max, print the min and max in a list.
x = [2,54,-2,7,12,98]
print min(x)
print max(x)

#First and Last, print the first and last values in a list.
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) -1]

#New List sort your list then split your list in half. Push the list created from the first half to position of 0 of the list created from the second half.
#output should be [-3, -2, 2 6, 7],10,12,19,32,54,98]
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
x.sort()
print x
first_list = x[:len(x)/2] 
second_list = x[len(x)/2:]
print "first list", first_list
print "second_list", second_list
second_list.insert(0,first_list)
print second_list

