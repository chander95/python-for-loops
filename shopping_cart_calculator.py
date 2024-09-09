#Use a for loop to iterate through the list of prices
#Calculate the total cost by adding up the prices of all the items
# Print the total cost at the end

cart = [4.99, 5.99, 12.99, 99.99, 29.99, 899.97]
total = 0

for item in cart:
    total += item
print(total)