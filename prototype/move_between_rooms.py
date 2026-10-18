# A dictionary for the simplified dragon text game. 
# The dictionary links a room to other rooms.
rooms = {
    'Great Hall': {'south': 'Bedroom'},
    'Bedroom': {'north': 'Great Hall', 'east': 'Cellar'},
    'Cellar': {'west': 'Bedroom'}
}

# Start the player in the Great Hall
current_room = 'Great Hall'

# Main gameplay loop
while current_room != 'exit':
    # Output the room the player is currently in
    print(f"\nYou are in the {current_room}.")

    # Prompt the player for a command
    command = input("Enter your move (or 'exit'): ").strip().lower()

    # Handle exit command
    if command == 'exit':
        current_room = 'exit'
        print("Thanks for playing!")
    # Handle valid movement commands
    elif command in rooms[current_room]:
        current_room = rooms[current_room][command]
    # Handle 'go <direction>' format just in case
    elif command.startswitch('go ') and command[3:] in rooms[current_rooms]:
        current_room = rooms[current_room][command[3:]]
    # Input validation for invalid commands
    else:
        print("Invalid command! You cannot go that way.")
                
