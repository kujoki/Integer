a = int(input('Enter: '))
l = a%10
m = (a//10)%10
n = a//100
r = n*100+l*10+m
p = m*100+n*10+l
print(r,p)
