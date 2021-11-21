#Python
#Find smallest value in an array
#https://github.com/wahnepowell

smallest = None
print("Value of smallest before:", smallest)

for num in [4, 45, 10, 76, 9, 2, 19, 27, 1, 17]:
    if smallest is None or num < smallest:
        smallest = num
    
print("Value of smallest after:", smallest)