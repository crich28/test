'''
    "Descending List"

    Write a function called descending_list that takes in a positive integer (n)
    and returns a list of all numbers from (n) to 1 in descending order.

    Examples:
        descending_list(5) --> [5, 4, 3, 2, 1]
        descending_list(3) --> [5, 3, 1]
        descending_list(1) --> [1]
'''

#Write your function under here
def descending_list(n):
    while n > 0:
        print(n)
        n-=1  
        
    
    
print(descending_list(8))        