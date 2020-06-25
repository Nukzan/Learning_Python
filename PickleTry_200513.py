# CALLING CLASS AND APPLY IT
from ClassEmployee_200513 import Employee as emp
emp1 = emp("Zara",2000)
emp1.displayEmployee()

# MAKE PICKLE AND LOAD WHAT IT LEANT BEFORE(RECORD/REMEMBER)
import pickle
pickle.dump(emp1, open("./emp1.pkl", "wb"))
emp1_pkl = pickle.load(open("./emp1.pkl", "rb"))
emp1_pkl.displayEmployee()