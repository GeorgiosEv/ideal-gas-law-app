### Ideal Gas Law is an equation of state, which describes the correlation between the pressure, volume & temperature of a hypothetical ideal gas.

### The following application is a primitive, Python-based Ideal Gas Law Calculator.
### VERSION 2: Using number of molecules N and the Boltzmann constant k.

### ------- CONSTANTS ------- ###
k = 1.381 * 10**(-23) # Boltzmann constant (J/K)

### ------- HELPER FUNCTION: INPUT VALIDATION ------- ###
# Gets a positive float from user input. 
def get_positive_float(prompt, allow_zero=False):
    # The WHILE loop keeps running until the user provides a valid input.
    while True:
        try:
            # Convert the input into a float. EXCEPT "catches" and "rejects" any non-numerical input. 
            value = float(input(prompt))
            # POSITIVE NUMBER ENFORCEMENT: If zero IS NOT allowed and value is zero or less, the code prints an error message. 
            if not allow_zero and value <= 0:
                print("❌ Value must be greater than zero. Please try again!")
                continue
            # ZERO-ALLOWED: If zero IS allowed and value is negative, the code prints an error message.
            if allow_zero and value < 0:
                print("❌ Value cannot be negative. Please try again!")
                continue
            return value
        except ValueError:
            print("❌ Invalid input: Please enter a numerical value!")

### ------- CALCULATION FUNCTIONS ------- ###
# 1: Calculate Pressure (P)
def Pressure(N,V,T):
    if V <= 0 or N <= 0 or T < 0:
        raise ValueError(
        "Invalid input: \n"
            "- Volume (V) must be greater than zero. \n" 
            "- Number of molecules (N) must be equal to or greater than zero. \n"
            "- Temperature (T) must be equal to or greater than zero. \n"
            ) 
    return (N * k * T) / V

# 2: Calculate Volume (V)
def Volume(N,P,T):
    if P <= 0 or N <= 0 or T <= 0:
        raise ValueError(
        "Invalid input: \n"
            "- Pressure (P) must be greater than zero. \n" 
            "- Number of molecules (N) must be equal or greater than zero. \n"
            "- Temperature (T) must be equal or greater than zero. \n"
            )
    return (N * k * T) / P

# 3: Calculate Temperature (T)
def Temperature(N,P,V):
    if N < 0 or P <= 0 or V <= 0:
        raise ValueError(
        "Invalid input: \n"
            "- Number of molecules (N) greater than zero. \n" 
            "- Pressure (P) must be equal or greater than zero. \n"
            "- Volume (V) must be equal or greater than zero. \n"
            )
    return (P * V) / (N * k)

### ------- CALCULATOR'S MAIN MENU ------- ##
def main():
    while True: # This WHILE loop keeps the calculator running, until user selects EXIT.
        print("\n***  Welcome to the Ideal Gas Law Calculator!  ***")
        
        print("\n You can pick from the following quantities: ")
        print("1. Pressure (P) in Pascals [Pa]")
        print("2. Volume (V) in cubic metres [m³]")
        print("3. Temperature (T) in Kelvin [K]")
        print("4. Exit Calculator")    
        
        # Allow user to select which quantity they wish to calculate!
        options = input("\n Select the quantity you want to calculate (1-4): ").strip()
        
        # You can select between MATCH STATEMENT or CONDITIONAL STATEMENT (IF/ELSE)
        # For the answers, I am using FLOAT format with 2 decimal places (.2f)
        match options:
            case "1": # Select this case to calculate Pressure (P)
                print("\n--- Calculation of Pressure (P) ---")
                N = get_positive_float("\nEnter the number of molecules (N): ") * 10**(23)
                V = get_positive_float("Enter Volume (V) of the container (m³): ")
                T = get_positive_float("Enter Temperature (T) of the container (K): ", allow_zero=True)
                try:
                    P = Pressure(N,V,T)
                    print(f"\n ✅️ Pressure P = {P:.2f} Pa \n")
                except ValueError as e:
                    print(f"\n {e} \n")
            case "2": # Select this case to calculate Volume (V)
                print("\n--- Calculation of Volume (V) ---")
                N = get_positive_float("\nEnter the number of molecules (N): ") * 10**(23)
                V = get_positive_float("Enter Pressure (P) of the container (m³): ")
                T = get_positive_float("Enter Temperature (T) of the container (K): ", allow_zero=True)
                try:
                    V = Volume(N,P,T)
                    print(f"\n ✅️ Volume V = {V:.2f} m³ \n")
                except ValueError as e:
                    print(f"\n {e} \n")
            case "3": # Select this case to calculate Temperature (T)
                print("\n--- Calculation of Temperature (T) ---")
                N = get_positive_float("\nEnter the number of molecules (N): ") * 10**(23)
                V = get_positive_float("Enter Pressure (P) of the container (Pa): ")
                T = get_positive_float("Enter Volume (V) of the container (m³): ", allow_zero=True)
                try:
                    T = Temperature(N,P,V)
                    print(f"\n ✅️ Temperature T = {T:.2f} K \n")
                except ValueError as e:
                    print(f"\n {e} \n")
            case "4": # Select this case to exit the programme
                print("\n 👋🏻 Thank you for using the Ideal Gas Calculator - Goodbye! \n")
                break
            case _: # Safe switch for invalid entry
                print("\n Invalid Choice: Please select a number between 1 and 4. \n")
    
if __name__ == "__main__":
    main()
