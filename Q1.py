def find_min(first,second):
    if first>=second:
         minimum = second
    elif second>first:
        minimum = first
    return minimum


first = int(input("Enter first number: "))
second = int(input("Enter second number: "))
    
minimum = find_min(first,second)

print("Minimum: ", minimum)        