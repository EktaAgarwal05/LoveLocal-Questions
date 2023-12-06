def maxRect(matrix):
    if not matrix or not matrix[0]:
        return 0
    m,n=len(matrix),len(matrix[0])
    max_area,h=0,[0]*n

    for i in range(m):
        row_input=input({i+1})
        matrix[i]=list(map(int,row_input[2:-2].split(',')))
        h=[h[j]+matrix[i][j] if matrix[i][j] ==1 else 0 for j in range(n)]

        stack,w=[],-1
        for j in range(n+1):
            while stack and (j==n or h[j]<h[stack[-1]]):
                h,w=h[stack.pop()],stack[-1] if stack else -1
                max_area=max(max_area,h*(j-w-1))
            stack.append(j)

    return max_area

usr_input=input()
matrix=[list(map(int,row.split(','))) for row in usr_input[2:-2].split('],[')]

out=maxRect(matrix)
print(out)