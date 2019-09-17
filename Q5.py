def palindrome(s):
    '''Returns True if the given string is a palindrome and False otherwise.'''
    s_clean = ''
    for ch in s:
        if ch.isalnum():
            s_clean += ch.lower()
    return s_clean == s_clean[::-1]

s = input("input a sentence: ")

if palindrome(s) == True:
    print("""" """ + s + """" """ + " is a palindrome")
else:
    print("""" """ + s + """" """ + " is not a palindrome")