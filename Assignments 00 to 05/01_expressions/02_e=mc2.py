C: int = 299792458
def main():
  mass_in_kg: float = float(input("Enter kilos of mass:"))
 # E stands for energy, m stands for mass, and C is the speed of light
 # Enter kilos of mass: 100
 # m = 100.0 kg
  energy_in_joules = mass_in_kg *  (C ** 2)
  print("e = m * C^2...")
  print("m = " + str(mass_in_kg) + " kg")
  print("C = " + str(C) + "m/s")
  print(str(energy_in_joules) + "joules of energy!")
main()

