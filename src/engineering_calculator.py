# Engineering Calculator

while True:

    print("\n=== ENGINEERING CALCULATOR ===")
    print("1. Reynolds Number")
    print("2. Flow Rate")
    print("3. Exit")

    choice = input("Choose an option (1/2/3): ")

    # -------------------------------
    # OPTION 1: REYNOLDS NUMBER
    # -------------------------------
    if choice == "1":
        print("\n--- Reynolds Number Calculator ---")

        density = float(input("Enter fluid density (kg/m^3): "))
        velocity = float(input("Enter velocity (m/s): "))
        diameter = float(input("Enter pipe diameter (m): "))
        viscosity = float(input("Enter viscosity (Pa.s): "))

        Re = (density * velocity * diameter) / viscosity

        print(f"\nReynolds Number: {Re:.2f}")

        if Re < 2000:
            print("Flow Type: Laminar Flow")
        elif Re <= 4000:
            print("Flow Type: Transitional Flow")
        else:
            print("Flow Type: Turbulent Flow")

    # -------------------------------
    # OPTION 2: FLOW RATE
    # -------------------------------
    elif choice == "2":
        print("\n--- Flow Rate Calculator ---")

        diameter = float(input("Enter pipe diameter (m): "))
        velocity = float(input("Enter velocity (m/s): "))

        area = 3.14 * (diameter ** 2) / 4
        flow_rate = area * velocity

        print(f"\nFlow Rate: {flow_rate:.4f} m^3/s")

    # -------------------------------
    # EXIT
    # -------------------------------
    elif choice == "3":
        print("Exiting program...")
        break

    # -------------------------------
    # INVALID INPUT
    # -------------------------------
    else:
        print("Invalid choice. Please try again.")