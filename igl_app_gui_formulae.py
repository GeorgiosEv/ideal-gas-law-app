### Ideal Gas Law is an equation of state, which describes the correlation between the pressure, volume & temperature of a hypothetical ideal gas.

### The following set of functions will be used as the backbone of the igl_app_gui.py file, supporting the execution of the calculations for the GUI I created with QT Designer.
### Using number of moles n and ideal gas constant R from Version 1 of part 1.

### ------- CONSTANTS ------- ###
R = 8.314 # Ideal gas constant (J/mol*K)

### ------- CALCULATION FUNCTIONS ------- ###
# 1: Calculate Pressure (P)
def Pressure(n,V,T):
    if n < 0 or V < 0 or T <= 0:
        raise ValueError(
        "Invalid input: \n"
            "- Number of moles (n) must be greater than zero. \n"
            "- Volume (V) must be greater than zero. \n"
            "- Temperature (T) must be equal to or greater than zero. \n"
            ) 
    return (n * R * T) / V

# 2: Calculate Volume (V)
def Volume(n,P,T):
    if n < 0 or P < 0 or T <= 0:
        raise ValueError(
        "Invalid input: \n"
            "- Number of moles (n) must be greater than zero. \n"
            "- Pressure (P) must be greater than zero. \n"
            "- Temperature (T) must equal to or greater than zero. \n"
            )
    return (n * R * T) / P

# 3: Calculate Temperature (T)
def Temperature(n,P,V):
    if n < 0 or P <= 0 or V <= 0:
        raise ValueError(
        "Invalid input: \n"
            "- Number of moles (n) greater than zero. \n" 
            "- Pressure (P) must be equal or greater than zero. \n"
            "- Volume (V) must be equal or greater than zero. \n"
            )
    return (P * V) / (n * R)

if __name__ == "__main__":
    main()