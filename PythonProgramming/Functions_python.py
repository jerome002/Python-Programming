

def large_power(base, exponent):
    base = int(input("Enter the base number: "))
    exponent = int(input("Enter the exponent: "))
    if base ** exponent > 5000:
        return True
    else:
        return False