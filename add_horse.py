def add_horse(horses, horse_id_list, horse_groups):
    # Check if the total number of horses is less than 20
    if len(horse_id_list) >= 20:
        print("Total horse details should be 20")
        return horse_id_list, horse_groups

    # Try to get a valid integer input for horse ID
    try:
        horse_id = int(input("Enter Horse ID to update (integer): "))
    except ValueError:
        print("Invalid input. Horse ID must be an integer.")
        return horse_id_list, horse_groups

    # Check if the horse ID is already in the list
    if horse_id in horse_id_list:
        print(f"The horse with ID {horse_id} is already added. Duplicated values are not allowed.")
        return horse_id_list, horse_groups

    # Get input for horse details
    horse_name = input("Enter Horse Name: ")
    if not horse_name.isalpha():
        print("Invalid input. Horse Name must contain only alphabetic characters.")
        return horse_id_list, horse_groups

    jockey_name = input("Enter Jockey Name: ")

    age = input("Enter Age (integer): ")
    if not age.isdigit():
        print("Invalid input. Age must be an integer.")
        return horse_id_list, horse_groups

    breed = input("Enter Breed: ")
    race_record_input = input("Enter Race Record (e.g., '5 wins in 6 races'): ")

    # Split the input and extract wins and total races
    race_record_parts = [part for part in race_record_input.split() if part.isdigit()]

    # Validate and parse the race record input
    if len(race_record_parts) != 2:
        print("Invalid input. Please use the format 'X wins in Y races', where X is the number of wins and Y is the total number of races.")
        return horse_id_list, horse_groups

    wins, total_races = map(int, race_record_parts) 
    if wins > total_races:
        print("Invalid input. The number of wins cannot exceed the total number of races.")
        return horse_id_list, horse_groups
    race_record = f"{wins}/{total_races}"
    group = input("Enter Group (A, B, C, D): ").upper()
    
    # Check if each group has only 5 horse IDs using the horse_groups dictionary
    if horse_groups.get(group, 0) >= 5:
        print(f"Cannot add more horses to Group {group}. Maximum limit (5) reached for this group.")
        return horse_id_list, horse_groups

    if group not in ["A", "B", "C", "D"]:
        print("Invalid input. Group must be A, B, C, or D.")
        return horse_id_list, horse_groups

    # Create a dictionary with horse details
    horse = {
        "horse_id": horse_id,
        "horse_name": horse_name,
        "jockey_name": jockey_name,
        "age": int(age),
        "breed": breed,
        "race_record": race_record,
        "group": group
    }

    # Append 'horse_id' to the horse_id_list
    horse_id_list.append(horse_id)
    horses.append(horse)  # Append horse details to the horses list

    # Update the count of horses in the corresponding group
    horse_groups[group] += 1
    
    print("Horse added successfully!")

    return horse_id_list, horse_groups
