#function to revers the string
def revStr(orgStr):
    #initialize an empty string
    revStr = ""
    #loop to reverse the string
    for i in range(len(orgStr) -1, -1, -1):
        #append each character to the reversed string
        revStr += orgStr[i]
     #return the reversed string
    return revStr


#calling the function to print the result
print ("Printing the string in reverse order:")
print(revStr("tutorials"))
print(revStr("Wesley"))
