def visualize_winning_horses(view_winning_horses):
    # Display the winning horses with their place, name, and visualization based on time
    print("Wenning horses:")
    for horse in view_winning_horses:
        # Print horse details, including place, name, time, and a visual representation based on time
        print(f"{horse['Place']} Place: {horse['Horse Name']} {horse['Time']} seconds {'*' * ((horse['Time'] // 10))}")