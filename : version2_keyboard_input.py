
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))
t = float(input("Enter time t (hours): "))

temperature = a * t**2 + b * t + c
print(f"Predicted temperature at time t={t} is {temperature:.2f}°C")
