try:
    print("hello world")
except ZeroDivisionError:
    print("zero division occur")
except ValueError:
    print("value error occured")
finally:
    print("no error ocuured")