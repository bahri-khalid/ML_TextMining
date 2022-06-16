import pandas as pd
import numpy as np
import nltk
import string
import re
nltk.download('stopwords')
from nltk.corpus import stopwords
#this function takes a dictionary that containe for each element the category name as key and the file name as value
def makeDataFrame(dictionnaire_class_article,separateur):
    classes = []
    articles = []
    for key in dictionnaire_class_article.keys():
        file = open('./Data/'+dictionnaire_class_article[key], 'r') # here you need to specify the path on you disk
        Lines = file.readlines()
        buffer = ''
        for i in range(len(Lines)):
            if separateur  not in Lines[i]:
                buffer+=Lines[i]
            else:
                classes.append(key)
                articles.append(buffer)
                buffer = ''
            if i == len(Lines)-1: # this if is just to handle the last article in the buffer 
                classes.append(key)
                articles.append(buffer)
                buffer = ''
    return pd.DataFrame(data = {'classe':classes,'article':articles})
    
    

#this function just take a dataframe (as pandas object) and create a zip file containing the csv format of the DataFrame
def downloadDataset(df):
    compression_opts = dict(method='zip',
                        archive_name='singleDataSet.csv')  
    df.to_csv('bahri.zip', index=False,
            compression=compression_opts)  

def netoyage(CED,wordsToRemove):
    pattern = 's’est'
    L = len(CED)
    for i in range(L):
        CED[i] = CED[i].lower()
    for i in range(L):
        for c in string.punctuation:
            x = CED[i].replace(c,' ')
            CED[i] = x
    stopwords_french = stopwords.words("french")
    for i in range(L):
        ls = CED[i].split()
        print(ls)
        for mot in ls:
            if mot in stopwords_french or mot in wordsToRemove:
                while mot in ls:
                    ls.remove(mot)
        CED[i] = " ".join(ls)
    return CED