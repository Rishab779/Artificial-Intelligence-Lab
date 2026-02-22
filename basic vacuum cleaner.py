def vacuum_agent(percept):
    location, status = percept
    
    if status == "Dirty":
        return "SUCK"
    elif location == "A":
        return "RIGHT"
    else:
        return "LEFT"


# Initial Environment
rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

total_rooms = len(rooms)
cleaned_rooms = 0
current_location = "A"
percept_sequence = []

print("\nSTEP | LOCATION | ACTION | STATUS | PERFORMANCE | PERCENTAGE | PERCEPT")

for step in range(1, 7):

    # Get current status
    status = rooms[current_location]
    
    # Create percept
    percept = (current_location, status)
    percept_sequence.append(percept)
    
    # Decide action
    action = vacuum_agent(percept)

    # Perform action
    if action == "SUCK":
        if rooms[current_location] == "Dirty":
            rooms[current_location] = "Clean"
            cleaned_rooms += 1

    elif action == "RIGHT":
        current_location = "B"

    elif action == "LEFT":
        current_location = "A"

    # Performance calculation
    performance = cleaned_rooms
    percentage = (cleaned_rooms / total_rooms) * 100

    # Print output
    print(f"{step:^4} | {current_location:^8} | {action:^6} | "
          f"{rooms[current_location]:^6} | {performance:^11} | "
          f"{percentage:^10.0f}% | {percept}")
