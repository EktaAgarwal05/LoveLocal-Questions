def palindrome(s):
    n=len(s)

    i=n
    while i >0 and s[:i] != s[i-1::-1]:
        i -= 1

    return s[i:][::-1] + s

s=input()

result=palindrome(s)
print(result)