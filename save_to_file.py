def save_to_file(horses):
    try:
        # Check if the total number of horse details is 20
        if len(horses) != 20:
            raise ValueError("Total horse details should be 20")

        # Extract horse IDs from the list of horses
        horse_ids = []
        for horse in horses:
            current_id = horse['horse_id']

            # Check for duplicated horse IDs
            if current_id in horse_ids:
                raise ValueError(f"Duplicated horse ID '{current_id}' found. Duplicated values are not allowed.")

            horse_ids.append(current_id)

        # Sort horse IDs in ascending order
        n = len(horse_ids)
        for i in range(n):
            for j in range(0, n-i-1):
                if horse_ids[j] > horse_ids[j+1]:
                    horse_ids[j], horse_ids[j+1] = horse_ids[j+1], horse_ids[j]

        # Create a dictionary of unique horses based on their IDs
        unique_horses = {}
        for horse_id in horse_ids:
            for horse in horses:
                if horse['horse_id'] == horse_id:
                    unique_horses[horse_id] = horse
                    break

        # Group horses by their 'group' attribute
        grouped_horses = {}
        for horse_id, horse in unique_horses.items():
            group = horse['group']
            if group not in grouped_horses:
                grouped_horses[group] = []
            grouped_horses[group].append(horse)

        # Validate each group has exactly 5 unique horse IDs without using set
        for group, group_horses in grouped_horses.items():
            if len(group_horses) != 5 or len(set(horse['horse_id'] for horse in group_horses)) != 5:
                raise ValueError(f"Group '{group}' should have exactly 5 unique horse IDs.")

        # Write horse details to a text file
        with open("horse_details.txt", "w") as file:
            for group, group_horses in grouped_horses.items():
                file.write(f"Group: {group}\n")
                for unique_horse in group_horses:
                    file.write(f"Horse ID: {unique_horse['horse_id']}, ")
                    file.write(f"Horse Name: {unique_horse['horse_name']}, ")
                    file.write(f"Jockey Name: {unique_horse['jockey_name']}, ")
                    file.write(f"Age: {unique_horse['age']}, ")
                    file.write(f"Breed: {unique_horse['breed']}, ")
                    file.write(f"Race Record: {unique_horse['race_record']}\n")
                file.write("\n")  # Add a newline after each group

        print("Horse details saved to horse_details.txt")

    except ValueError as e:
        print(f"Error: {e}")