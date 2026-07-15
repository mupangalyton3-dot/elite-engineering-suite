def reynolds_number():
    print("\n=== Reynolds Number Calculator ===")

    velocity = float(input("Enter velocity (m/s): "))
    density = float(input("Enter density (kg/m³): "))
    diameter = float(input("Enter diameter (m): "))
    viscosity = float(input("Enter viscosity (Pa·s): "))

    Re = (density * velocity * diameter) / viscosity

    print(f"\nReynolds Number: {Re}")

    if Re < 2000:
        print("Flow Type: Laminar")
    elif 2000 <= Re <= 4000:
        print("Flow Type: Transitional")
    else:
        print("Flow Type: Turbulent")