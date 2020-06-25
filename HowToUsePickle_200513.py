#DUMP IS WRITE / LOAD IS READ

import pickle
favorite_color = {"lion":"yellow", "kitty":"red"}
pickle.dump (favorite_color, open("save.pkl","wb"))
favorite_color_load = pickle.load(open("save.pkl","rb"))
print(favorite_color_load)
