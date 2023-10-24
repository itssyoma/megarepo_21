a2, a1, b = map(int, input("Enter a2, a1, b: ").split())
c2 = a2 + (a1 + b) // 10
c1 = (a1 + b) % 10
print(f"Number of tens: {c2}\nNumber of ones: {c1}")
