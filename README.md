# ⚛️ ideal_gas_law_app 👨🏻‍🔬
The [ideal gas law](https://www.britannica.com/science/ideal-gas-law) is an equation of state that describes the relation between Pressure (P), Volume (V) and temperature (T) of an ideal gas in the limit of low pressure and high temperature.

According to the definition of the *ideal gas law* (check link above), which is derived from the kinetic theory of gas, there are a few assumptions regarding the nature and size of the molecules and the interactions between them:
> (1) The gas consists of a large number of molecules, which are in random motion and obey Newton’s laws of motion,

> (2) The volume of the molecules is negligibly small compared with the volume occupied by the gas, and

> (3) No forces act on the molecules except during elastic collisions of negligible duration.

The well-known formula that mathematically describes the ideal gas law is the following:
```
DERIVATION
PV = nRT => PV = (N/N_A)RT => PV = N(R/N_A)T => PV = NkT
```
- Pressure (P) (in Pascals | Pa)
- Volume (V) (in cubic metres | m³)
- Temperature (T) (in Kelvin | K)
- n: number of moles , N: number of molecules
- Constants:
  - [Ideal Gas Constant R](https://www.britannica.com/science/universal-gas-constant) = 8.314 J/mol*K
  - [Boltzmann's Constant k](https://www.britannica.com/science/Boltzmann-constant) = 1.381 * 10*{-23} J/K
  - [Avogadro's Number N_A](https://en.wikipedia.org/wiki/Avogadro_constant) = 6.022 * 10*{-23} /mol
- Relations between the constants:
  - n = N / N_A
  - k = R / N_A 

## PART 1️⃣: Python-based script

For the 1st part of this project, I created a simple Python-based script (consisting of 2 versions, one for each form of this equation, as stated above). 
- The script allows the user to input 2 out of 3 main quantities (P, V, T), in addition to definining the number of moles (n) (in V1) or the number of molecules (N) (in V2).
- An simple error-handling system has also been implemented to ensure no invalid input is accepted and optimise functionality.
- The calculation functions will then provide the result (including the appropriate physical units).

A screenshot of a test run (attempting to calculate the Pressure (P), in V1) can be seen below:

⬇️

<img width="316" height="217" alt="Test Run Python-based Ideal Gas Law" src="https://github.com/user-attachments/assets/beefce29-ad31-40e8-96ac-2b61194e5f22" />

The 1st part is located here: [ideal_gas_law_part_1](ideal_gas_law_part_1)

## PART 2️⃣: Python-based GUI (Created in QT Designer)
For the 2nd part of this project, I utilised the functionality of the Python script from part 1 of this project, incorporating it into a Python-based GUI (created in [QT Designer](https://doc.qt.io/qt-6/gettingstarted.html)).
- The GUI allows user to input 2 out of 3 main quantities (P, V, T), in addition to definining the number of moles (n) (in this case and for simplicity, we have only utilised V1 from Part 1).
- An simple error-handling system has also been implemented to ensure no invalid input is accepted and optimise functionality.
- The result will then be displayed at the bottom of the window (including the appropriate physical units).

A screenshot of a test run (attempting to calculate the Pressure (P)) can be seen below:

⬇️

<img width="345" height="381" alt="Test Run Qt-based Ideal Gas Law" src="https://github.com/user-attachments/assets/cfd7d423-0e3e-4f0c-8d3f-bdb47fe3e37d" />

The 2nd part is located here: [ideal_gas_law_part_2](ideal_gas_law_part_2)

## PART 3️⃣: LabVIEW GUI
For the 3rd part of this project, I created a UI-based calculator in LabVIEW from scratch. Due to my past work with LabVIEW, it was easy for me to identify the components that were required and built the system.
- The calculator interface contains a combination of LabVIEW elements (e.g. radio buttons, case structures) that allow the smooth execution of the calculations and the appropriate error handling (e.g. division with zero, case selection and allowed input quantities).
- The GUI allows user to input 2 out of 3 main quantities (P, V, T), in addition to definining the number of moles (n), through the INPUT CONTROL panel.
- The result will then be displayed in the OUTPUT panel (using both visual and numerical means, and including the appropriate physical units).

A screenshot of a test run (attempting to calculate the Pressure (P)) can be seen below:

⬇️

<img width="600" height="443" alt="Test Run LabView-based Ideal Gas Law" src="https://github.com/user-attachments/assets/9b5c407b-f688-4bed-97b7-c461bb373a12" />

The 3rd part is located here: [ideal_gas_law_part_3](ideal_gas_law_part_3)
