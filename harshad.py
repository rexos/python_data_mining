num = raw_input('type a number \n')
sum = 0
for char in num:
    sum += int(char)

print( int(num) % sum == 0 )
