import employee_management as em

def main():
    while True:
        print("\nEmployee Management System")
        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Update Employee")
        print("5. Delete Employee")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            em.add_employee()
        elif choice == "2":
            em.view_employees()
        elif choice == "3":
            em.search_employee()
        elif choice == "4":
            em.update_employee()
        elif choice == "5":
            em.delete_employee()
        elif choice == "6":
            print("Exiting Employee Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
