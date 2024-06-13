health_status=input("enter health status")
age=int(input("enter age"))
locality=input("enter locality")
gender=input("enter gender")
#a
if health_status==("excellent") and (age>=25 and age<=35) and locality =="city"and gender =="male":
    print("premium amount Rs.4 per thousand and his policy amount cannot exceed Rs.2 lakh")
#b
elif health_status==("excellent") and (age>=25 and age<=35) and locality =="city"and gender =="female": 
    print(" Rs. 3 per thousand and her policy amount cannot exceed Rs.1 lakh")
#c
elif health_status==("poor") and (age>=25 and age<=35) and locality =="village"and gender =="male":
    print("cannot exceed Rs.10000")
#d
else:
    ("person is not secured")



