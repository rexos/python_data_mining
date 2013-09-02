def fibonacci(n):
    ary = [1,1]
    for i in range(2,n):
        ary.append(ary[i-1]+ary[i-2])
    return ary[n-1]

print fibonacci(10)
        
