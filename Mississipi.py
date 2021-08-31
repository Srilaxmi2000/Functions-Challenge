
X=input("Please enter the string:")
def most_frequent(string):
    d=dict()
    for key in string:
        if key in d:
            d[key]=+1
        else:
            d[key]=1
    return d

print(most_frequent(X))

            

