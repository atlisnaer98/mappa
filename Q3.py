# The function definition goes here
def inn_range(num):
    if 1<num<555:
        print(num, "is in range.")
    else:
        print(num, "is outside the range!")
    

num = int(input("Enter a number: "))

inn_range(num)