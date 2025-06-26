for item in ['Mosh', 'John', 'Sarah', 1, 2, 3, 4]:  # square brackets show a list
    print(item)




for item in range(5, 10, 2):  # range function - start, stop(exclusive), step
    print(item)



prices = [10, 20, 30]
total = 0
for price in prices:
    total += price  # total = total + price
print(f"Total: {total}")