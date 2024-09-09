booth_types = ["Food", "Games", "Music", "Crafts"]
schedule = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00 PM"]
items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

#Use a for loop to iterate over each booth type
#For each booth type, print the booth type, the scheduled time, and the item needed.
#Ensure that each booth type is matched with the correct schedule time and the item needed from the list provided

for booth in booth_types:
    if booth == "Food":
        print(f"This is the {booth} booth. It will open be open starting at {schedule[1]}. We still need to get the {items_needed[0]}")
    elif booth == "Games":
        print(f"This is the {booth} booth. It will be open at {schedule[0]}. We're just waiting on the {items_needed[1]}")
    elif booth == "Music":
        print(f"This is the {booth} booth. It will open at {schedule[2]} once we get all the {items_needed[2]}")
    elif booth == "Crafts":
        print(f"This is the {booth} booth. It will open at {schedule[-1]} once we have all the {items_needed[-1]}")
    else:
        print("That's not one of the booths available today!")