## Dataset

The dataset folder contains the dataset dataframe containing the tokenized scripts using PSParser as well as the script itself.

The 0 label is used to indicate a malicious script while 1 is for a benign script.  


Loading the dataset 
```
import pandas as pd

df = pd.read_csv('Dataset/dataset.csv')
df.drop("Unnamed: 0", axis='columns', inplace=True)
df.head()
```




