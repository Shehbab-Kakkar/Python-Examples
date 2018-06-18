#!/usr/bin/python3.6
import time
start = time.time()
result = eval('1.0 + 2.0 + 3.0 + 4.0 + 5.0 + 6.0')
print(result)
calculation=input("Please enter the calculation: ")
result = eval(calculation)
print("The result of your entered calculation is ",result)
end = time.time()
print(end - start)


