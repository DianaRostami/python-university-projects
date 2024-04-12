#project no.1 prototype version 3

#library
import statistics

#input
num1, num2, num3, num4, num5 = map(int, input().split())
num =[num1, num2, num3, num4, num5]

#function
avg = sum(num)/5
variance = statistics.variance(num)

#output
print("average is =", avg)
print("Variance =", variance)
