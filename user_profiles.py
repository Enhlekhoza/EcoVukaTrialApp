class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role  # "waste_picker" or "citizen"
        self.profile = {}

    def create_profile(self, profile_data):
        self.profile = profile_data

def main():
    users = []

    while True:
        print("User Registration and Profiles")
        print("1. Register as Waste Picker")
        print("2. Register as Citizen")
        print("3. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            username = input("Enter username: ")
            waste_picker = User(username, "waste_picker")
            profile_data = {"name": input("Enter your name: "), "location": input("Enter your location: ")}
            waste_picker.create_profile(profile_data)
            users.append(waste_picker)
            print("Waste Picker registered successfully!")
        elif choice == "2":
            username = input("Enter username: ")
            citizen = User(username, "citizen")
            profile_data = {"name": input("Enter your name: "), "location": input("Enter your location: ")}
            citizen.create_profile(profile_data)
            users.append(citizen)
            print("Citizen registered successfully!")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please select again.")

    print("User profiles:")
    for user in users:
        print(f"Username: {user.username}, Role: {user.role}, Profile: {user.profile}")

if __name__ == "__main__":
    main()
