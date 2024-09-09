booth_types = ["Food", "Games", "Music", "Crafts"]
schedule = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

#Use a for loop to iterate over each booth type
#For each booth type, print the booth type, the scheduled time, and the item needed.
#Ensure that each booth type is matched with the correct schedule time and the item needed from the list provided

for i in range(len(booth_types)):
    booth = booth_types[i]
    time = schedule[i]
    item = items_needed[i]
    print(f"{booth} Booth - Schedule: {time} - Items Needed: {item}")