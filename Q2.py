def count_case(user_input):
    upper_counter = 0
    lower_counter = 0
    for letter in user_input:
        if letter.isupper():
            upper_counter += 1
        elif letter.isalpha():
            lower_counter +=1
    return upper_counter, lower_counter

user_input = input("Enter a string: ")

output = count_case(user_input)
upper_counter, lower_counter = output




print("Upper case count: ", upper_counter)
print("Lower case count: ", lower_counter)