

#Part I

def draw_stars(x):
    star = ""
    for i in range(0,len(x)): # i runs through the values from 0 to the length of x
        temp = x[i]
        for j in range(0,temp): # j runs through the values from 0 to each temp value
            star+= "*"          # Then the star = star + * into the new container "star"
        print star
draw_stars([4,6,1,3,5,7,25])

#Part II

def stars2(arr):
    for x in arr: # x is for each index in the array
        if isinstance(x, int): # x = object, int = classinfo isinstance > if x is an interger next line: do something
            print "*" * x
        elif isinstance(x, str):
            length = len(x)     #variable length set to be the length of the x index element. Example tom = 3
            letter = x[0].lower()   #.lower() makes the str lower case letter, x[0] is the first position for of index x
            print letter * length # t * 3 (example using "tom")

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
stars2(x)