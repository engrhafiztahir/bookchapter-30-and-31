#!/usr/bin/env python
# coding: utf-8

# In[12]:


Computer = {1:"Mouse",2:"Keyboard",3:"Monitor",4:"System Unit", 5:"RAM",6:"Hard Disk"}
Computer_part = Computer[1]
print(Computer_part)
print(Computer)
del Computer[1]
print(Computer)
Computer[2] = "Speaker"
print(Computer)


# In[16]:


Computer = {1:"Mouse",2:"Keyboard",3:"Monitor",4:"System Unit", 5:"RAM",6:"Hard Disk"}
Computer_part = Computer[1]
print(Computer_part)
print(Computer)
Computer[1] = "Speaker"
print(Computer)
Computer[2] = "Mother Board"
print(Computer)


# In[17]:


Computer = {1:"Mouse",2:"Keyboard",3:"Monitor",4:"System Unit", 5:"RAM",6:"Hard Disk"}
Computer.remove{"Mouse"}
print(Computer)


# In[22]:


Computer = {1:"Mouse",2:"Keyboard",3:"Monitor",4:"System Unit", 5:"RAM",6:"Hard Disk"}
for computer_part in Computer.values():
    print(computer_part)


# In[30]:


number = {"one":1,"two":2,"three":3,"four":4, "five":5}
for a_number in number.values():
    if a_number == 4 % 3:
        print("ok")
    else:
        print("No value")
    break


# In[26]:


print(4 % 2) 


# In[ ]:




