#!/usr/bin/env python3.6
#Stripping function 
# lstrip()
# rstrip()
# strip()
city=input("Enter Your City Name:")
list=["Hydrabad","Bangalore","Ferozepur","Chandigarh"]
if city.lstrip() in list:
     print("Your city is available and CCC and XXX")
else:
     print(city,"Please enter valid city Name")
