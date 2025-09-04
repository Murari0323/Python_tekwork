def palindrome(word):
    if word==word[::-1]:
        print("Palindrome word")
    else:
        print("Not a palindrome word")

word=input("Enter a word or string: ")
palindrome(word)