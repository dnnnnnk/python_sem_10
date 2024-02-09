import pandas as pd
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
one_hot = pd.get_dummies(data['whoAmI'])
data = pd.concat([data, one_hot], axis=1)
data.head()