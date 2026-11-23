prices = [100, 200, 50, 300, 80,350, 400]

expensive = 0
cheap = 0

for i in prices:
    if i >= 150:
        print(i, "Expensive")
        expensive = expensive + 1
    else:
        print(i, "Cheap")
        cheap = cheap + 1

print("Expensive Products:", expensive)
print("Cheap Products:", cheap)
