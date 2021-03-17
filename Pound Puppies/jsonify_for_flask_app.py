#!/usr/bin/env python
# coding: utf-8

# In[138]:
import pandas as pd
import requests
from io import StringIO
# In[140]:

# path to csv
train_csv_path = "https://drive.google.com/file/d/1AvEIyNW4bQO9-Mg7CKb4RXFs_Xq-qro8/view?usp=sharing"
color_csv_path = "https://drive.google.com/file/d/1OBvlVnhEGH79DWlfpTtD4JFYsIfIGbX0/view?usp=sharing"
breed_csv_path = "https://drive.google.com/file/d/15-dm0dLnBokkrdwM_Cb1rvlUgTpW2vYl/view?usp=sharing"
down ="https://drive.google.com/uc?export=download&id="

# file ids
train = train_csv_path.split('/')[-2]
color = color_csv_path.split('/')[-2]
breed = breed_csv_path.split('/')[-2]

# dowload csv
train_do = requests.get(down+train).text
color_do = requests.get(down+color).text
breed_do = requests.get(down+breed).text

# getting csv text
train_csv = StringIO(train_do)
color_csv = StringIO(color_do)
breed_csv = StringIO(breed_do)

# df
train_df = pd.read_csv(train_csv)
color_df = pd.read_csv(color_csv)
breed_df = pd.read_csv(breed_csv)

# train_df.head(2)

# In[141]:
breed_df= breed_df[['BreedID','BreedName']]
breed_df.head(2)

# In[142]:
color_df.head(2)

# In[143]:

# pet type
type_df = pd.DataFrame.from_dict({"typeID":[1,2],
                       "type":['dog','cat']}
                      )
type_df

# In[144]:

# adoptibility
adopt_df = pd.DataFrame.from_dict({"adID":[0,1,2,3,4],
                                  "duration":['same day','1-7 days',
                                              '8-30 days','31-90 days',
                                              'no adoption after 100 days'
                                             ]
                                 })
adopt_df

# In[145]:

# to csv
adopt_df.to_csv(path+'adopt_df.csv',index=False)
breed_df.to_csv(path+'breed_df.csv',index=False)
type_df.to_csv(path+'type_df.csv',index=False)

# In[146]:

# read csv to dataFrame
adopt_df = pd.read_csv(path+'adopt_df.csv')
breed_df = pd.read_csv(path+'breed_df.csv')
type_df = pd.read_csv(path+'type_df.csv')

# In[147]:

type_json = type_df.to_json(orient='split', index=False)
# type_json

# In[148]:

breed_json = breed_df.to_json(orient='split', index=False)
# breed_json

# In[149]:

adopt_json = adopt_df.to_json(orient='split', index=False)
# adopt_json

# In[150]:

def type_json_def():
    return type_json

# In[151]:

def adopt_json_def():
    return adopt_json

# In[152]:

def breed_json_def():
    return breed_json

# In[153]:

def id_breed(bre_in):
    a = breed_df.BreedName[breed_df.index[breed_df.BreedID == bre_in]].tolist()[0]
    return a    

# In[154]:

def id_adopt(ado_in):
    a = adopt_df.duration[adopt_df.index[adopt_df.adID == ado_in]].tolist()[0]
    return a

# In[155]:

def id_type(typ_in):
    a = type_df.type[type_df.index[type_df.typeID == typ_in]].tolist()[0]
    return a

# In[ ]:




