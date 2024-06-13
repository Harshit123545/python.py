fuel=70
mileage=10
ticket_price=80
distance=int(input("the distance in km"))
n_pass = int(input("the number of passenger"))
collection = n_pass*ticket_price
print(collection)
fuel_consume = (distance//mileage)*fuel
print(fuel)
if fuel<collection:
    print("profit")
else:
    print("loss")
    