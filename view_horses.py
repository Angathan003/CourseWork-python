def view_horses(horses):
    horse_ids = []
    for horse in horses:
        # Extract horse IDs from the list of horses
        horse_ids.append(horse['horse_id'])

    # Sort horse IDs in ascending order
    n = len(horse_ids)
    for i in range(n):
        for j in range(0, n-i-1):
            if horse_ids[j] > horse_ids[j+1]:
                horse_ids[j], horse_ids[j+1] = horse_ids[j+1], horse_ids[j]

    # Display sorted horse details
    print("\n===== Sorted Horse Details =====")
    for sorted_id in horse_ids:
        for horse in horses:
            if horse['horse_id'] == sorted_id:
                print(f"Horse ID: {horse['horse_id']}")
                print(f"Horse Name: {horse['horse_name']}")
                print(f"Jockey Name: {horse['jockey_name']}")
                print(f"Age: {horse['age']}")
                print(f"Breed: {horse['breed']}")
                print(f"Race Record: {horse['race_record']}")
                print(f"Group: {horse['group']}")
                print("--------------------------")

