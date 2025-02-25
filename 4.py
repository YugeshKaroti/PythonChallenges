#  Dictionary contains names as keys and values as scores. You need to return the name and the score of the highest scorer ?
dict_1 = {"Person_1":45, "Person_2":60, "Person_3":32, "Person_4":60, "Person_5":52}

max_score = max(dict_1.values())

for i,j in zip(dict_1.keys(), dict_1.values()):
    if j == max_score:
        print(f"Name : {i}")
        print(f"Score : {j}")
        print("*"*10)
    else:
        pass