## Dataset

The dataset folder contains the numpy arrays containing the tokenized scripts using PSParser. 
As well as the dataset dataframe created in the notebook. 


Loading the dataset 
```
import pandas as pd

df = pd.read_csv('Dataset/dataset.csv')
df.drop("Unnamed: 0", axis='columns', inplace=True)
df.head()
     
```




