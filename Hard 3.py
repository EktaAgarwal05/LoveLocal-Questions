def DigitOne(n):
    c=0
    factor=1

    while factor <= n:
        div=factor*10
        c += (n // div) * factor +min(max(n%div-factor+1,0),factor)

        factor *= 10

    return c

n=int(input())
result=DigitOne(n)
print(result)