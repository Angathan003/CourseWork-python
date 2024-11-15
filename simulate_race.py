import random

def simulate_race(selected_horses):
    # Simulate the race and assign random times between 0 and 90 seconds using randint
    race_results = {}
    for group, horse in selected_horses.items():
        race_results[group] = {
            'horse': horse,
            'time': random.randint(0, 90)  # Use randint to generate integer values
        }

    # Bubble sort to sort the horses based on their race times
    results_list = list(race_results.items())
    n = len(results_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if results_list[j][1]['time'] > results_list[j+1][1]['time']:
                results_list[j], results_list[j+1] = results_list[j+1], results_list[j]

    # Save horse name and time in ascending order of place
    view_winning_horses = []
    place = 1
    for group, result in results_list[:3]:
        horse_name = result['horse']['Horse Name']
        race_time = result['time']
        view_winning_horses.append({'Place': place, 'Horse Name': horse_name, 'Time': race_time})
        place += 1

    # Print the race results
    print("Race Results:")
    for group, result in results_list[:3]:
        print(f"Group: {group}")
        for key, value in result['horse'].items():
            print(f"{key}: {value}")
        print(f"Time: {result['time']} seconds")  # Use integer values
        print()
    return view_winning_horses

