# Conditional Execution

hrs = input("Enter Hours:")
h = float(hrs)
rphr = input("Enter Rate per hour:")
r = float(rphr)
if h <= 40:
    print(h * r)
else:
    print(40 * r + (h-40) * 1.5 * r)
