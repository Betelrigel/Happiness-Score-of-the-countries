
# coding: utf-8

# In[2]:


import pandas as pd
data=pd.read_csv("happyscore.csv")
print(data)


# In[30]:


happy=data["happyScore"]
income=data["avg_income"]
print(happy)


# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('happyscore.csv')
data.sort_values('avg_income',inplace=True) #sort avg income in ascending order 
richest=data[data['avg_income']>15000]      #inplace=true means we're sorting the same data itself rather than making a copy from original one
richest #displaying the list
richest.iloc[0] #lowest in the list
richest.iloc[-1] #highest in the list
richest.iloc[0:5] #displays the first five of the list

rich_mean=np.mean(richest['avg_income'])
all_mean=np.mean(data['avg_income'])
print(all_mean,rich_mean)
plt.scatter(richest['avg_income'],richest['happyScore'])
plt.text(richest.iloc[0]['avg_income'],   #plotting the lowest with label
         richest.iloc[0]['happyScore'],
         richest.iloc[0]['country'])
plt.text(richest.iloc[-1]['avg_income'],  #plotting the highest with the label
         richest.iloc[-1]['happyScore'],
         richest.iloc[-1]['country'])

for k,row in richest.iterrows(): #to label all the points in the data we use the for loop
    plt.text(row['avg_income'],
             row['happyScore'],
             row['country'])
            


# In[4]:


import pandas as pd
data=pd.read_csv('happyscore.csv')
happy=data['happyScore']
income=data['avg_income']
ineq=data['income_inequality']
income.max()


# In[5]:


import matplotlib.pyplot as plt
plt.xlabel('income')              #here we label the x and y axis
plt.ylabel('happy score')
#plt.scatter(income,happy)
plt.scatter(income,happy,s=ineq*10, alpha=0.25)  #here we display a third dimension ie inequality
                                                 #s=ineq is used to change the size of the dots according to the inequality
                                                 # 10 is the range of size of ineq and alpha is the transparency


# In[13]:


from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
data=pd.read_csv('happyscore.csv')
happy=data['happyScore']
income=data['avg_income']

income_happy=np.column_stack((income,happy))
km_res= KMeans(n_clusters=3).fit(income_happy)
clusters=km_res.cluster_centers_

plt.scatter(income,happy)
plt.scatter(clusters[:,0],clusters[:,1],s=2000, alpha=0.5)

#eyeballing
km_res.cluster_centers_  #finding the cluster centres


# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('happyscore.csv')
data.sort_values('avg_income',inplace=True) 
poor=data[data['avg_income']<15000]      

plt.xlabel('income of poor')             
plt.ylabel('happy score')

poor_ineq= poor['income_inequality']
plt.scatter(poor['avg_income'],poor['happyScore'],s=poor_ineq*10, alpha=0.25)
plt.text(poor.iloc[0]['avg_income'],   
         poor.iloc[0]['happyScore'],
         poor.iloc[0]['country'])
plt.text(poor.iloc[-1]['avg_income'],   
         poor.iloc[-1]['happyScore'],
         poor.iloc[-1]['country'])


                  

