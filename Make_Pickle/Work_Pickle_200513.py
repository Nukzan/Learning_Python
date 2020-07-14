from Work_Use_200513 import s1
import pickle
pickle.dump(s1, open("./work_200513.pkl","wb"))
yhiS1_pkl = pickle.load(open("./work_200513.pkl","rb"))
yhiS1_pkl.getPredict()