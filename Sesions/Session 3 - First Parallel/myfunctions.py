#!/usr/bin/env python
# coding: utf-8

# # My Functions Library
# 
# Due to a bug in the multiprocessing module implemented for the Windows Operating System, the functions that will be executed in the parallel threads MUST be implemented in a separate file and imported into the main program.
# 
# In order to load them in your own program, you have to write your own functions here and export them to a Python ".py" file, to be imported into the main script.
# 
# To export to a Python file, select the option *Download as* from the *File* menu, and save it as a *Python (.py)* file.

# ## Functions needed for FirstParallel notebook

# In[ ]:


def f(x):
    return x*x


# In[ ]:


def dot(d):
    r=d[0]*d[1]
    return r


# ## Functions needed for Benchmark notebook

# In[2]:


def work(task):
    """
    Some amount of work that will take time
    
    Parameters
    ----------
    task : tuple
        Contains number, loop, and number processors
    """
    number, loop = task
    b = 2. * number - 1.
    for i in range(loop):
        a, b = b * i, number * i + b
    return a, b


# 
# 

# In[1]:


#This cell should be the last one
#This avoids the execution of this script when it is invoked directly.
if __name__ == "__main__":
    print("This is not an executable library")

