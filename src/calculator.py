def reynolds_number():
    try:
        density = float(input("Density: "))
        velocity = float(input("Velocity: "))
        diameter = float(input("Diameter: "))
        viscosity = float(input("Viscosity: "))
        
        Re = (density * velocity * diameter) / viscosity
        
        print(f"\nRe = {Re:.2f}")
        
        if Re < 2000:
            print("Laminar")
        elif Re <= 4000:
            print("Transitional")
        else:
            print("Turbulent")
            
    except:
        print("Invalid input")