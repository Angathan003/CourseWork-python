def update_horse(horses):
    # Try to get a valid integer input for horse ID
    try:
        user_input_id = int(input("Enter Horse ID to update (integer): "))
    except ValueError:
        print("Invalid input. Horse ID must be an integer.")
        return
    # Check if the horse ID in horses list matches the user input ID
    for horse in horses:
        if horse["horse_id"] == user_input_id:
            horse_name = input("Enter updated Horse Name: ")
            if not horse_name.isalpha():
                print("Invalid input. Horse Name must contain only alphabetic characters.")
                return

            jockey_name = input("Enter updated Jockey Name: ")


            try:
                age = int(input("Enter updated Age (integer): "))
            except ValueError:
                print("Invalid input. Age must be an integer.")
                return

            breed = input("Enter updated Breed: ")
            race_record_input = input("Enter updated Race Record (e.g., 5 wins in 6 races): ")
            race_record_parts = [part for part in race_record_input.split() if part.isdigit()]
             # Validation of record input
            if len(race_record_parts) != 2:
                print("Invalid input. Please use the format 'X wins in Y races', where X is the number of wins and Y is the total number of races.")
                return

            wins, total_races = map(int, race_record_parts)
            if wins > total_races:
                print("Invalid input. The number of wins cannot exceed the total number of races.")
                return
            race_record = f"{wins}/{total_races}"
            
            group = input("Enter updated Group (A, B, C, D): ").upper()
            if group not in ["A", "B", "C", "D"]:
                print("Invalid input. Group must be A, B, C, or D.")
                return
            # Update the horse details
            horse["horse_name"] = horse_name
            horse["jockey_name"] = jockey_name
            horse["age"] = age
            horse["breed"] = breed
            horse["race_record"] = race_record
            horse["group"] = group
            print("Horse details updated successfully!")
            break
    else:
        # loop complete without break
        print("Horse not found!")

