num=int(input("enter the numerator:"))
deno=int(input("enter the denominator:"))
try:
    quo=num/deno
    print("quotient:",quo)
except Exception:
    print("denominator cannot be zero")
