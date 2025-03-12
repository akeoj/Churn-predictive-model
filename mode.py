import pandas as pd 
import numpy as np
from sklearn.preprocessing import LabelEncoder
import pickle

model = pickle.load(open('model.pkl', 'rb'))
cat_col = pickle.load(open('fugazi.pkl', 'rb'))

def prediction(data):
    le = LabelEncoder()
    df = pd.DataFrame(data)

    for i in data:
        if type(i) == str:
            df.iloc[data.index(i)] = le.fit_transform(df.iloc[data.index(i)])
            

    df= df.drop([0])
    pred = model.predict(df.values.reshape(1,-1))
    if pred[0] == 1:
        return "The Customer Left the Telecommunication Service"
    else:
        return "The Customer enjoys the Telecommunication Service"
    

print(prediction(['00003d165737109921ebd21f883cb8cff028b626',
 'TAMBACOUNDA',
 'K > 24 month',
 4000.0,
 8.0,
 4000.0,
 1333.0,
 8.0,
 257.0,
 1620.0,
 9.0,
 6.0,
 1.0,
 2.0,
 'NO',
 45,
 'On-net 500F_FNF;3d',
 8.0]))