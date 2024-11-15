# Importing functions from modules
from add_horse import add_horse
from update_horse import update_horse
from delete_horse import delete_horse
from view_horses import view_horses
from save_to_file import save_to_file
from select_horses_for_race import select_horses_for_race
from simulate_race import simulate_race
from visualize_winning_horses import visualize_winning_horses

# List to store horse details
horses = []
horses_selected = False # Flag to track
# Create a new list to store horse_ids
horse_id_list = []
# Create a dictionary to store the count of horses in each group
horse_groups = {"A": 0, "B": 0, "C": 0, "D": 0}


while True:
    # Displaying the menu options in main programing loop
    print("\n===== Horse Race Event Menu =====")
    print("1. Type AHD for adding horse details.")
    print("2. Type UHD for updating horse details.")
    print("3. Type DHD for deleting horse details.")
    print("4. Type VHD for viewing the registered horses' details table. (Sort according to horse ID).")
    print("5. Type SHD for saving the horse details to the text file.")
    print("6. Type SDD for selecting four horses randomly for the major round.")
    print("7. Type WHD for displaying the Winning horses' details.")
    print("8. Type VWH for Visualizing the time of the winning horses.")
    print("9. Type ESC to exit the program.")

    choice = input("Enter your choice: ").upper()

    # user choices
    if choice == "AHD" and not horses_selected:
        add_horse(horses, horse_id_list, horse_groups)
    elif choice == "UHD" and not horses_selected:
        # print(horses)
        update_horse(horses)
    elif choice == "DHD" and not horses_selected and not horses_selected:
        delete_horse(horses, horse_id_list, horse_groups)
    elif choice == "VHD":
        print(horses)
        view_horses(horses)
    elif choice == "SHD" and not horses_selected:
        save_to_file(horses)
    elif choice == "SDD" and not horses_selected:
        selected_horses = select_horses_for_race()
        horses_selected = True
    elif choice == "WHD" and horses_selected:
        view_winning_horses = simulate_race(selected_horses)
    elif choice == "VWH" and horses_selected:
        visualize_winning_horses(view_winning_horses)
    elif choice == "ESC":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option.")
