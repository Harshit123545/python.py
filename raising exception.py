try:
    raise NameError
except NameError:
    print("NameError caught")
except ValueError:
    print("ValueError is handled")