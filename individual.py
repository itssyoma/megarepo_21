a, b = map(float, input("Enter 2 numbers: ").split())
mean_a = (abs(a) + abs(b)) / 2
mean_g = (abs(a) * abs(b))**0.5
print(f"Arithmetic mean: {mean_a}\nGeometric mean: {mean_g}")
