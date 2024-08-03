#original string
orgnlStr = "Wesley"

#subsring to find
newStr = "Wes"

#to find the index of the substring
indx = orgnlStr.find(newStr)

#to check if the subsring is found
if indx == -1:
    print("-1")
else:
    print("Subsring found at index: ", indx)