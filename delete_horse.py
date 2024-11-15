def delete_horse(horses, horse_id_list, horse_groups):
    # Try to get a valid integer input for horse ID
    try:
        user_input_id = int(input("Enter Horse ID to delete (integer): "))
    except ValueError:
        print("Invalid input. Horse ID must be an integer.")
        return horse_id_list, horse_groups

    horse_deleted = False

    # Create a copy of the list to avoid issues when removing elements
    horses_copy = horses.copy()

    for horse in horses_copy:
        # Check if the horse ID matches the user input ID
        if horse["horse_id"] == user_input_id:
            # Remove the horse from the original list
            horses.remove(horse)
            horse_deleted = True
            print("Horse deleted successfully!")

            # If a horse was deleted, decrement the count in the corresponding group
            group = horse["group"]
            horse_groups[group] -= 1

            # Remove the horse_id from the horse_id_list
            if user_input_id in horse_id_list:
                horse_id_list.remove(user_input_id)

            break
    else:
        # loop complete without break
        print("Horse not found!")

    return horse_id_list, horse_groups