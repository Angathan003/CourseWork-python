import random

def select_horses_for_race():
    # List to store all horse details
    all_horses = []

    try:
        # Read the file and store horse details in a list
        with open('horse_details.txt', 'r') as file:
            lines = file.readlines()
            current_group = None
            for line in lines:
                if line.startswith('Group'):
                    current_group = line.split(': ')[1].strip()
                else:
                    # Split the line into elements
                    elements = line.split(', ')
                    
                    # Check if the line has enough elements
                    if len(elements) >= 6:
                        horse_details = {
                            'Group': current_group,
                            'Horse ID': elements[0].split(': ')[1],
                            'Horse Name': elements[1].split(': ')[1],
                            'Jockey Name': elements[2].split(': ')[1],
                            'Age': elements[3].split(': ')[1],
                            'Breed': elements[4].split(': ')[1],
                            'Race Record': elements[5].split(': ')[1].strip()
                        }
                        all_horses.append(horse_details)

        # Check total number of horse details
        if len(all_horses) != 20:
            raise ValueError("Total horse details should be 20")

        # Check for duplicated Horse IDs using a list
        horse_ids = []
        for horse in all_horses:
            if horse['Horse ID'] in horse_ids:
                raise ValueError("Duplicated values for Horse ID are not allowed")
            horse_ids.append(horse['Horse ID'])

        # Organize the data into a dictionary by group
        horse_groups = {}
        for horse in all_horses:
            group = horse['Group']
            if group not in horse_groups:
                horse_groups[group] = []
            horse_groups[group].append(horse)

        # Select a random horse from each group
        selected_horses = {}
        for group, horses in horse_groups.items():
            selected_horses[group] = random.choice(horses)

        # Print the selected horses
        for group, horse in selected_horses.items():
            print(f"Group: {group}")
            for key, value in horse.items():
                print(f"{key}: {value}")
            print("\n")

        return selected_horses

    except ValueError as ve:
        print(f"Error: {ve}")
