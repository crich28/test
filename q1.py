'''
    "Duplicate W's in a String"

    Write a function called duplicate_w that takes in a string
    and duplicates w's in that string.

    Examples:
        duplicate_w("wow") --> "wwoww"
        duplicate_w("www.google.com") --> "wwwwww.google.com"
        duplicate_w("apple") --> "apple"
'''

#Write your function under here
def duplicate_w(str):
    
    for i in range(len(str)+1):
        if str[i] == 'w':
            str = str[i]+str
    return str          
print(duplicate_w('worldw'))