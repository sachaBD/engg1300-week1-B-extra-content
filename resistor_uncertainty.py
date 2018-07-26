import random
import matplotlib.pyplot as plt

"""
Generate the combined series resistance for n resistance with a value
resistance and a random tolerance.
"""
def n_series_resistors(n, resistance, tolerance):
    total = 0

    for i in range(0,n):
        actualR = resistance * ( 1 - tolerance * (random.random() * 2 - 1))
        
        total += actualR

    return total

"""
Generate the combined parralel resistance for n resistance with a value
resistance and a random tolerance.
"""
def n_parralel_resistors(n, resistance, tolerance):
    total = 0

    for i in range(0,n):
        actualR = resistance * ( 1 - tolerance * (random.random() * 2 - 1))
        
        total += (actualR)**(-1)

    return (total)**(-1)

"""
Create a nice graph to visually show the distributions of resistance due
to varying combinations.
"""
def create_graphics(number, resistance, tolerance):
    # Store many samples for the possible resistor space
    RT = []
    
    # Generate many samples from resistors of these values
    for i in range(0, 100000):
        RT.append(n_series_resistors(number, resistance, tolerance))
        
    # Place into buckets of 0.1 ohms to count occurances
    binned = {}
    
    for r in RT:
        binned.setdefault(round(r,2) , 0)
        binned[round(r,2)] += 1
        
    # normalise the occurance function
    vNormed = [float(i)/sum(binned.values()) for i in binned.values()]

    print(len(binned), len(vNormed))

    plt.title("Series resistance of 10 10 Ohm resistors with tolerance 5%. 10^6 samples.")
    plt.xlabel("Resistance (Ohms)")
    plt.ylabel("Occurances grouped to 0.01 Ohms")
    plt.scatter(binned.keys(), vNormed)
    plt.ylim([min(vNormed) - max(vNormed) * 0.1, max(vNormed) * 1.1])
    plt.show()





"""
Inputs to the program:
"""
R1 = 2
R2 = 100
tolerance = 0.05

create_graphics(R1, R2, tolerance)

