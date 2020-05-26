#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# 1.สร้างกราฟธรรมดาเป็นฟังก์ชั่น Y = X^2 พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน 

# In[2]:


x = np.arange(1,9)
y = x**2 
plt.plot(x,y)
plt.title('Y=X^2')
plt.xlabel('X')
plt.ylabel('Y=X^2')
plt.show()


# 2.สร้างกราฟฟังก์ชั่น Sin (เหมือนตัวอย่าง) พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน เปลี่ยนสีเส้นเป็นสีชมพู 

# In[6]:


x = np.arange(1,8)
y = np.sin(x)
plt.plot(x,y,c='m')
plt.title('Sin')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


# 3.สร้างกราฟธรรมดาเป็นฟังก์ชั่น X = Y^2 พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน เปลี่ยนสีเส้นเป็นสีเขียวอ่อนโดยใช้ค่ารหัสสีฐานสิบหก

# In[7]:


y = np.arange(1,9)
x = y**2 
plt.plot(x,y,c='#CCFFCC')
plt.title('X=Y^2')
plt.xlabel('X=Y^2')
plt.ylabel('Y')
plt.show()


# 4.สร้างกราฟฟังก์ชั่น Cos (เหมือนตัวอย่าง) พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน เปลี่ยนสีเส้นเป็นสีแดง ใส่ Line Style เป็นเส้น - - 

# In[9]:


x = np.arange(1,8)
y = np.cos(x)
plt.plot(x,y,c='r',ls = '--')
plt.title('Cos')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()


# 5. สร้างกราฟธรรมดาเป็นฟังก์ชั่น Y = X^2 และ Y = X^3 พล็อตลงในรูปเดียวกัน พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน ใช้สีแดงและน้ำเงินตามลำดับ โดยเส้นแรกใช้วงกลมเป็น marker และเส้นสองใช้สามเหลี่ยมเป็น marker

# In[24]:


x = np.arange(1,8)
y1 = x**2
y2 = x**3 
plt.plot(x,y1,c='r',marker ='o',label='x^2')
plt.plot(x,y2,c='b',marker ='^',label='x^3')
plt.legend(loc=0)
plt.title('x^2 & x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.show


# 6. สร้างกราฟธรรมดาเป็นฟังก์ชั่น Y = X^2 และ X = Y^2 พล็อตลงในรูปเดียวกัน พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน ใช้สีแดงและน้ำเงินตามลำดับ โดยเส้นแรกใช้วงกลมเป็น marker และเส้นสองใช้สามเหลี่ยมเป็น marker และใส่ legend และเพิ่มเส้นตารางข้างหลัง

# In[29]:


x = np.arange(1,8)
y = x**2
x2 = y**2
plt.plot(x,y,c='r',marker ='o',label='y=x^2')
plt.plot(x2,y,c='b',marker ='^',label='x=y^2')
plt.legend(loc=0)
plt.title('y=x^2 & x=y^2')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show


# 7. สร้างกราฟธรรมดาเป็นฟังก์ชั่น X = Y^2 + 4*Y พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน เปลี่ยนสีเส้นเป็นสีเหลืองอ่อนโดยใช้ค่ารหัสสีฐานสิบหก จำกัดแกน X และ Y ให้เหมาะสม 

# In[30]:


y = np.arange(1,8)
x = (y**2) + (4*y)
plt.plot(x,y,c='#FFFF99')
plt.title('X = Y^2 + 4*Y')
plt.xlabel('x=y^2+4*y')
plt.ylabel('y')
plt.show()


# 8. สร้างกราฟใหญ่ด้วยสมการ X = Y^3 และกราฟเล็กด้วย Y = X^2 + 2 พล็อตลงในรูปเดียวกัน พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน และใส่ legend 

# In[38]:


y = np.arange(1,8)
x = y**3
y2 = x**2 + 2
fig = plt.figure()
ax1 = fig.add_axes([0.1,0.1,0.95,0.85])
ax1.plot(x,y,label=('x=y^3'))
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc=0)
ax2 = fig.add_axes([0.7,0.2,0.3,0.3])
plt.plot(x,y2,label=('y=x^2+2'))
plt.legend(loc=0)
plt.xlabel('x')
plt.ylabel('y')
plt.show()


# In[40]:


import pandas as pd


# In[42]:


df = pd.read_csv('../Desktop/DataCamp/train.csv')


# In[51]:


df.head()


# 9.ให้หาอัตราส่วนตั๋วโดยสารชั้น 1 2 3 และพล็อตเป็น Pie chart 

# In[92]:


fare_class1 = (df['Pclass']==1).sum()
fare_class2 = (df['Pclass']==2).sum()
fare_class3 = (df['Pclass']==3).sum()
fare_allclasses = (df['Pclass']).count()
print(fare_class1)
print(fare_class2)
print(fare_class3)
print(fare_allclasses)


# In[82]:


fare_class1_ratio = fare_class1/fare_allclasses
fare_class2_ratio = fare_class2/fare_allclasses
fare_class3_ratio = fare_class3/fare_allclasses
print(fare_class1_ratio)
print(fare_class2_ratio)
print(fare_class3_ratio)


# In[83]:


fare_class_ratio = [fare_class1_ratio,fare_class2_ratio,fare_class3_ratio]
fare_class_ratio


# In[84]:


plt.figure(figsize = [5,5])
labels = ['fare class1 ratio','fare class2 ratio','fare class3 ratio']
plt.pie(fare_class_ratio,labels = labels)
plt.show()


# 10. ให้หาอัตราส่วนของจุดหมายปลายทาง (Embark) และพล็อต Pie chat พร้อมทั้งให้ Queenstown เป็น explode

# In[94]:


embarkS = (df['Embarked']=='S').sum()
embarkQ = (df['Embarked']=='Q').sum()
embarkC = (df['Embarked']=='C').sum()
embarkall = (df['Embarked']).count()
print(embarkS)
print(embarkQ)
print(embarkC)
print(embarkall)


# In[95]:


embarkS_ratio = embarkS/embarkall
embarkQ_ratio = embarkQ/embarkall
embarkC_ratio = embarkC/embarkall
print(embarkS_ratio)
print(embarkQ_ratio)
print(embarkC_ratio)


# In[96]:


embark_ratio = [embarkS_ratio,embarkQ_ratio,embarkC_ratio]
embark_ratio


# In[101]:


plt.figure(figsize = [5,5])
explode = [0,0.1,0]
labels = ['embarkS ratio','embarkQ ratio','embarkC ratio']
plt.pie(embark_ratio,labels = labels, explode = explode)
plt.show()


# 11. นำราคาตั๋วโดยสารทั้งหมดมาหา histogram

# In[103]:


fare = df['Fare']
fare 


# In[108]:


plt.figure(figsize = [5,5])
plt.hist(fare,bins=30)
plt.show()


# 12.สร้างพล็อตแบบกระจายโดยให้อายุเป็นแกน X และ ราคาตั๋วโดยสารเป็นแกน Y

# In[109]:


age = df['Age']
age


# In[111]:


plt.figure(figsize = [5,5])
plt.scatter(age,fare)
plt.title('Scatter Plot')
plt.show()


# 13.สร้าง bar chart โดยใช้ข้อมูลจากราคาตั๋วโดยสารเฉลี่ยแต่ละชั้น 

# In[113]:


fare_class1= df['Fare'][df['Pclass']==1].mean()
fare_class2= df['Fare'][df['Pclass']==2].mean()
fare_class3= df['Fare'][df['Pclass']==3].mean()
print(fare_class1)
print(fare_class2)
print(fare_class3)


# In[116]:


fare_class = [fare_class1,fare_class2,fare_class3]
fare_class


# In[117]:


classtitanic = [3,2,1]
classtitanic


# In[119]:


plt.figure(figsize = [5,5])
plt.bar(fare_class,classtitanic)
plt.title('Bar Chart')
plt.show()


# 14. สร้าง bar chart โดยใช้ข้อมูลจากราคาตั๋วโดยสารต่ออายุของผู้โดยสาร

# In[120]:


plt.figure(figsize = [5,5])
plt.bar(fare,age)
plt.title('Bar Chart')
plt.show()


# 15. สร้าง bar chart โดยใช้ข้อมูลผู้ที่นามสกุลซ้ำกัน โดยความถี่เป็นแกน Y

# In[240]:


df = pd.read_csv('../Desktop/DataCamp/train.csv')
df[['Last','First']] = df14.Name.str.split(",",expand=True)
df.head()


# In[252]:


grouped= df.groupby(['Last']).filter(lambda x: len(x)>1)
grouped


# In[256]:


group_count = grouped['Last'].value_counts()
group_count


# In[260]:


values = grouped['Last'].value_counts().values
values


# In[261]:


index = grouped['Last'].value_counts().index
index


# In[268]:


fig=plt.figure(figsize = [45,5])
plt.bar(index,values)
plt.title('Bar Chart')
plt.xlabel('Last names')
plt.ylabel('Frequency')
fig.autofmt_xdate()
plt.show()


# 16.สร้างหลายกราฟในรูปเดียว โดยมีสองคอลัมน์ คอลัมน์แรกมีสามแถว คอลัมน์สองมีสองแถว พร้อมใส่ชื่อกราฟ รายละเอียดแต่ละแกน โดยสมการแต่ละกราฟสามารถคิดเองได้โดยใช้ข้อมูลจากไฟล์ titanic และไม่ต้องซ้ำกัน (optional)

# In[ ]:




