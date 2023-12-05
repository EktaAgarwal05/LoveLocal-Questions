def pascal_triangle(num_rows):
    triangle = []

    for i in range(num_rows):
        row = [1]*(i+1)
        
        for j in range(1,i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)
    
    return triangle

num_rows = int(input())
result = pascal_triangle(num_rows)
print(result)