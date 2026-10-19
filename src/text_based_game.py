# Author: Bre'Shanna Fields
# Description: Text-Based Adventure Game (IT 140 Project Two)

def show_instructions():
    """Displays game title, goals, and movement commands."""
    print("Dragon Text Adventure Game")
    print("Collect 6 items to win the game, or be eaten by the dragon.")
    print("Move commands: go South, go North, go East, go West")
    print("Add to Inventory: get 'item name'")


def main():
    """Main game loop and mechanics."""
    # Dictionary linking rooms to the other rooms and their respective items
    rooms = {
        'Great Hall': {'south': 'Bedroom', 'north': 'Dungeon', 'east': 'Kitchen', 'west': 'Library'},
        'Bedroom': {'north': 'Great Hall', 'east': 'Cellar', 'item': 'Armor'},
        'Cellar': {'west': 'Bedroom', 'item': 'Helmet'},
        'Dining Room': {'south': 'Kitchen', 'item': 'Dragon'},  #Villain Room
        'Library': {'east': 'Great Hall', 'item': 'Book'}
        'Kitchen': {'west': 'Great Hall', 'north': 'Dining Room', 'item': 'Potion'},
        'Dungeon': {'south': 'Great Hall', 'item': 'Sword'}
    }

    # Starting conditions
    current_room = 'Great Hall'
    inventory = []

    # Display game instructions once at the start
    show_instructions()

    # Main gameplay loop
    while True:
        print("\n" + "-" * 30)
        print(f"You are in the {current_room}")
        print(f"Inventory: {inventory}")

        # Check if the room contains an item that hasn't been collected
        room_item = rooms[current_room].get('item')
        if room_item and room_item != 'Dragon':
            print(f"You see a {room_item}")

        # Check for villain encounter (Loss Condition)
        if room_item == 'Dragon':
            if len(inventory) == 6:
                # Player collected all items and won
                print("\nCongratulations! You have collected all items and defeated the dragon!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            else:
                # Player encountered dragon without all items
                print("\nNOM NOM... GAME OVER!")
                print("Thanks for playing the game. Hope you enjoyed it.")
            break

        print("-" * 30)

        # Get input from user
        user_input = input("Enter your move: ").strip().Split(" ", 1)
        command = user_input[0].lower() if len(user_input) > 0 else ""
        argument = user_input[1] if len(user_input) > 1 else ""

        # Handle movement ("go North", "go South", etc.)
        if command == "go":
            direction = argument.lower()
            if direction in rooms[currect_room]:
                current_room = rooms[current_room][direction]
            else:
                print("You can't go that way!")

        # Handle retrieving items ("get Armor", "get Sword", etc.)
        elif command == "get":
            item_name = argument
            if 'item' in rooms[current_room] rooms[current_room]['item'].lower() == item_name.lower():
               inventory.append(rooms[current_room]['item'])
               print(f"{rooms[current_room]['item']} retrieved!")
               del rooms[current_room]['item'] # Remove item from room after collecting
          else:
               print(f"Can't get {item_name}!")

    else:
        print("Invalid command! Use 'go [direction]' or 'get [item_name]'.")


if __name__ == '__main__':
    main()
