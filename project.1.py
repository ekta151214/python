def add_friend(friendships, person, friend):
    if person not in friendships:
        friendships[person] = set()
    friendships[person].add(friend)

def find_common_friends(friendships, person1, person2):
    return friendships.get(person1, set()).intersection(friendships.get(person2, set()))

def main():
    friendships = {}

    while True:
        print("1. Add a friend")
        print("2. Find common friends")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            person = input("Enter the person's name: ")
            friend = input("Enter the friend's name: ")
            add_friend(friendships, person, friend)
            add_friend(friendships, friend, person)  # Assuming friendship is mutual
            print(f"{person} and {friend} are now friends.")

        elif choice == "2":
            person1 = input("Enter the first person's name: ")
            person2 = input("Enter the second person's name: ")
            common_friends = find_common_friends(friendships, person1, person2)
            if common_friends:
                print(f"Common friends between {person1} and {person2}:")
                for friend in common_friends:
                    print(friend)
            else:
                print(f"{person1} and {person2} have no common friends.")

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")
main()