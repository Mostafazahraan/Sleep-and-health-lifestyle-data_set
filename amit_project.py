#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import pypyodbc as podbc
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')
df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")


# In[18]:


df.head()


# In[19]:


categorical_cols = df.select_dtypes(include='object').columns


# In[20]:


categorical_cols


# In[21]:


for i in categorical_cols:
    print(df[i].unique())


# In[22]:


df.isnull().sum()


# In[23]:


import seaborn as sns


# In[24]:


df


# In[25]:


df.shape


# In[26]:


df.info()


# In[27]:


df.duplicated().sum()


# In[28]:


df.drop_duplicates()


# In[29]:


df.describe()


# In[30]:


gender_count=df['Gender'].value_counts().reset_index()
gender_count.columns = ['Gender', 'count']
gender_count


# In[31]:


df['Age'].describe()


# In[32]:


age_count=df['Age'].value_counts().reset_index()
age_count.columns = ['Age', 'count']
age_count


# In[33]:


df['Occupation'].unique()


# In[52]:


Occupation_count=df['Occupation'].value_counts().reset_index()
Occupation_count.columns = ['Occupation', 'count']
Occupation_count


# In[35]:


df['Sleep Duration'].describe()


# In[53]:


Sleep_Duration_count=df['Sleep Duration'].value_counts().reset_index()
Sleep_Duration_count.columns = ['Sleep Duration', 'count']
Sleep_Duration_count


# In[37]:


df['Quality of Sleep'].unique()


# In[103]:


Quality_of_Sleep_count=df['Quality of Sleep'].value_counts().reset_index()
Quality_of_Sleep_count.columns = ['Quality of Sleep', 'count']
Quality_of_Sleep_count


# In[39]:


df['Physical Activity Level'].describe()


# In[69]:


Physical_Activity_Level=df['Physical Activity Level'].value_counts().reset_index()
Physical_Activity_Level.columns=['Physical Activity Level','count']
Physical_Activity_Level


# In[41]:


df['Stress Level'].unique()


# In[92]:


Stress_Level_counts=df['Stress Level'].value_counts().reset_index()
Stress_Level_counts.columns=['Stress Level','counts']
Stress_Level_counts


# In[43]:


df['BMI Category'].unique()


# In[44]:


df['BMI Category']=df['BMI Category'].replace({'Normal':'Normal Weight'})


# In[96]:


BMI_Category_count=df['BMI Category'].value_counts().reset_index()
BMI_Category_count.columns=['BMI Category', 'count']
BMI_Category_count


# In[46]:


df['Blood Pressure'].unique()


# In[99]:


Blood_Pressure_count=df['Blood Pressure'].value_counts().reset_index()
Blood_Pressure_count.columns=['Blood Pressure','count']
Blood_Pressure_count


# In[104]:


Heart_Rate_count=df['Heart Rate'].value_counts().reset_index()
Heart_Rate_count.columns=['Heart Rate', 'count']
Heart_Rate_count


# In[49]:


df['Daily Steps'].describe()


# In[129]:


Daily_Steps_count=df['Daily Steps'].value_counts().reset_index()
Daily_Steps_count=Daily_Steps_count.sort_values(by='Daily Steps',ascending=False).head(5)
Daily_Steps_count


# In[ ]:


df['Sleep Disorder'].unique()


# In[105]:


Sleep_Disorder_count=df['Sleep Disorder'].value_counts().reset_index()
Sleep_Disorder_count.columns=['Sleep Disorder', 'count']
Sleep_Disorder_count


# In[3]:


fig = px.pie(gender_count, values='count', names='Gender',title='Each  Gender and its count  ')
fig.show()


# In[118]:


fig=px.bar(age_count,x='Age',y='count',title='The Age and The Number of people in The same Age')
fig.show()


# In[70]:


fig=px.bar(Physical_Activity_Level,x='Physical Activity Level',y='count',title='The Physical Activity Level and The Number of peapol ')
fig.show()


# In[82]:


fig=px.bar(Quality_of_Sleep_count,x='Quality of Sleep',y='count',title='The Quality of Sleep and The Number of people ')
fig.show()


# In[86]:


fig=px.bar(Sleep_Duration_count,x='Sleep Duration',y='count',title='The Sleep Duration and The Number of people ')
fig.show()


# In[85]:


fig=px.bar(Occupation_count,x='Occupation',y='count',title='The Occupation and The Number of people ')
fig.show()


# In[4]:


fig = px.pie(Stress_Level_counts,values='counts',names='Stress Level',title=" Stress Level")
fig.show()


# In[132]:


plt.title('The Stress Level and the number of it in each Occupation')
plt.xlabel('Stress Level')
plt.ylabel('Count')
plt.xticks(rotation=90)
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.show()


# In[97]:


fig=px.pie(BMI_Category_count,values='count',names='BMI Category',title="the BMI Category")
fig.show()


# In[100]:


fig=px.bar(Blood_Pressure_count,x="Blood Pressure",y="count",title="the Blood Pressure and each count")
fig.show()



# In[107]:


fig=px.bar(Heart_Rate_count,x="Heart Rate",y="count",title="the Heart Rate and each count")
fig.show()


# In[131]:


fig=px.bar(Daily_Steps_count,x='index',y='Daily Steps',title="the top 5 Daily Steps")
fig.show()


# In[ ]:




