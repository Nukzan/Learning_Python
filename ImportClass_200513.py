## CLASS CLASS FROM OTHER FILE(CLASS)
# from ClassEmployee_200513 import Employee as emp
# emp1 = emp("Zara",2000)
# emp2 = emp("Manni",5000)

# emp1.displayEmployee()
# emp2.displayEmployee()

# CALL CLASS FROM PACKAGES
from packages.ClassAthlete_200513 import Athlete as ath
ath1 = ath('Sarah', '2001-01-01', ['2:58','2.58','1.56'])
print(ath1.times)
jane = ath('Jane')
print(jane.name)