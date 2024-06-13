def calculate_total_ticket_cost(no_of_adults,no_of_childrens):
    total_ticket_cost=0
    result=(no_of_adults*37550.0 + no_of_childrens*(37550.0/3))
    service_tax=(0.07*result)
    result=service_tax+result
    discount=0.1*result
    total_ticket_cost=result-discount
    return total_ticket_cost

total_ticket_cost=calculate_total_ticket_cost(3,1)
print(total_ticket_cost)
    