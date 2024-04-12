#project no.1
num1 , num2 , num3 , num4 , num5 = map(int, input().split())
avg = (num1 + num2 + num3 + num4 + num5)/5
print(avg)
variance = ((num1 - avg)**2 + (num2 - avg)**2 + (num3 - avg)**2 + (num4 - avg)**2 + (num5 - avg)**2)/5
print(variance)