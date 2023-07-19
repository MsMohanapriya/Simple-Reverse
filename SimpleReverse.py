def SimpleReverse(string):
    str=" "
    for i in string:
        str=i+str
    return str
string=input("enter string: ")
print(SimpleReverse(string))
        
        