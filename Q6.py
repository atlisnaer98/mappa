# Your function definition goes here

def fibo(N):
    first_num = 1
    second_num = 0
    third_num = 0
    count = 0
    while count < N:
        third_num = first_num + second_num
        print(third_num,end=" ")
        first_num = second_num
        second_num = third_num
        count += 1
    return

        


n = int(input("Input the length of Fibonacci sequence (n>=1): "))
# Call your function here

fibo(n)