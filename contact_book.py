contacts = {}
while True:
    print("\n1.Add")
    print("2.View")
    print("3.Search")
    print("4.Delete")
    print("5.Exit")
    choice = input("Pick a Choose: ")
    if choice == "1":
        name = input("Name: ")
        phone = input("Phone no: ")
        contacts[name] = phone
        print("Contact Saved!")
    elif choice == "2":
        print(contacts)
    elif choice == "3":
        name = input("Search Name: ")
        if name in contacts:
            print("phone:", contacts[name])
        else:
            print("Sorry! Not Found!")
    elif choice == "4":
        name = input("Delete name: ")
        if name in contacts:
            del contacts[name]
            print("Deleted Successfully!")
        else:
            print("Sorry! Not found!")
    elif choice == "5":
        print("See You Again!...")
        break
    else:
        print("Invalid choice!")
    
    