str = input("PLease enter your string name:  ")

def most_frequent(string):
    mydict=dict()
    for key in string:
        if key not in mydict:
            mydict[key]=1
        else:
            mydict[key]+=1
    return mydict

print(most_frequent(str))
