#!/usr/bin/env python
# coding: utf-8

# Q-1 What are the three measures of central tendency ?

# Ans-2 The three measures of central tendency are:
# 
# 1. MEAN: It is the average of a set of values, calculated by adding up all the values and dividing by the total numbers of data points.
# 2. MEDIAN : It is the middle value in a sorted list of data .If there is an even numbers of data points the median is the average of the two middle values.
# 3. MODE : It is the value that occurs most frequently in a dataset .

# Q-2 What is the difference between the mean , median ,and mode ?How are they used to measure the central tendency of a dataset ?

# Ans-1 
# 1. MEAN : This is what most people commonly refer to as the "average" .It is calculated by adding up all the values in a dataset and dividing by the total number of values. The mean can be sensitive to outliers ,meaning it can be greatly influenced by unusually high or low values.
# 2. MEDIAN : The median is the middle value in a dataset when the values are arranged in ascending or descending order .If there are an even number of data points , the median is the average of the two middle values .The median is less affected by extreme values or outliers compared to the mean .
# 3. MODE : The mode is the value that occurs most frequently in a dataset. A dataset can have one mode , more than one mode (multi-modal)  or no mode at all if all values occur with equal frequency.

# Q-3 Measure the three measures of central tendency for the given height data.
# [178,177,178.2,178,175,179,180,175,,178.9,176.2,177,172.5,178,176.5]

# In[5]:


height=[178,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]


# In[4]:


import numpy as np


# In[6]:


np.mean(height)


# In[7]:


np.median(height)


# In[9]:


from scipy import stats


# In[10]:


stats.mode(height)


# Q-4 Find the standard deviation for the given data:

# In[11]:


height=[178,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]


# In[12]:


np.std(height)


# Q-5 How are measures of disperion such as range , variance ,and standard deviation used to describe the spread of a dataset ? Provide an example.

# RANGE : Range is the simplest measures of dispresion .It is the difference between the maximum and minimum values in a dataset.
# VARIANCE : Variance measures the average of the squared difference from the mean .It provides a more detailed view of the spread compared to range.
# STANDARD DEVIATION :The standard deviation is the square root of the variance .It provides a measures of how spread out the data is relative to the maen.

# In[13]:


height=[178,177,178.2,178,175,179,180,175,178.9,176.2,177,172.5,178,176.5]


# In[14]:


np.range(height)


# In[15]:


np.var(height)


# In[16]:


np.std(height)


# Q-6 What is venn diagram ?

# Ans-6 A VENN Diagram is a visual representation that illustrates the relationships between different sets of data. It consists of overlapping circles, each representing a set ,and the overlapping portions indicates the elements that are common to those sets . 

# Q-7 For the two given sets A=(2,3,4,5,6,7) and B=(0,2,6,8,10). FIND :
# (i) A intersaction B
# (ii) A union B

# (i) A intersaction B ={2}
# (ii) A union B ={0,2,3,4,5,6,7,8,10}

# Q-8 What do you understand about skewness in data ?

# Ans-8 Skewness in data refers to the asymmetry of the probability distribution of a dataset .It is a measures of the deviation of the data from a normal distribution .In a skewed distribution ,the data points tend to cluster more on one side of the mean than the other.
# There are three type of skewness :
# 1. POSITIVE SKEW(RIGHT SKEW) : In a positively skewed distribution , the tail on the right- hand side is longer or fatter than the left-hand side. This means that there are more data points on the left side of the distribution , and the distribution is stretched towards the right .The mean is typically greater than the median in a positively skewed distribution. 
# 2. NEGATIVE SKEW(LEFT SKEW) : In a negatively skewed distribution , the tail on the left- hand side is longer or fatter than the right-hand side. This means that  there are more data points on the right-hand-sude of thr distribution ,and the distribution is stretched towards the left.The means is typically less than the median in a negatively skewed distribution.
# 3. NO SKEW(SYMMETRICAL) : In a symmetrical distribution , the data is evenly distributed around the mean . The left and right tails are approximately the same.
#  

# Q-9 If a data is right skewed then what will be the position of median with respect to mean ?

# Ans-9 In a right-skewed distribution , the tail of the distribution is stretched towards the right , meaning that there are few extreme high values pulling the mean in that direction . As a result , the mean will be greater than the median .So , in a right- skewed distribution , the position of the median will be to the left of the mean .

# Q-10 Explain the difference between covariance and correlation .How are these measures used in statistical analysis ?

# Ans-10 
# 1. COVARIANCE : Covariance measures the extent to which two varaible change together .It indicates whether they tend to increase or decrease together .
# 2. CORRELATION : Correlation is a standardized version of covariance.It measures the strength and direction of a linear relationship between two variable .It is always between -1 and 1.
# DIFFERENCE :
# 
# Covariance indicates the direction of the linear relationship between two variables ,while correlation quantifies the strength and direction of that relationship in a standardized way , making it more interpretable and widely used in practice.
# 
# USE IN STATISTICAL ANALYSIS :
# 
# 1. Covariance is used in variance statistical calculations ,but it's not as commonly used in practice as correlation because of its scale- dependency.
# 2. Correlation is widely used to analyze relationship between variables in fields like economics, finance ,psychology, and many others.

# Q-11 What is the formula for calculating the sample mean ? Provide an example calculation for a datase.

# Ans-11 The formula for calculating the sample mean(x) of a dataset is :
#        X = Σxi / n
#        where,
# 
#  Σxi is the sum of terms in the sample,
# 
# n is the number of terms in the sample.
# 
# EXAMPLE :
# 
# We have the sample, 15, 20, 72, 43, 21
# 
# Sum of terms(S) = 15 + 20+ 72 + 43 + 21 = 171
# 
# Number of terms(n) = 5
# 
# Using the formula for sample mean, we get
# x̄ = S/n
# 
# = 171/5
# 
# = 34.2

# Q-12 For a normal distribution data what is the relationship between its measures of central tendency ?

# Ans-12 For a dataset that follows a normal distribution , the measures of central tendency (mean median, and mode) exhibit a specific relationship :
# 
# 1. MEAN : This is what most people commonly refer to as the "average" .It is calculated by adding up all the values in a dataset and dividing by the total number of values. The mean can be sensitive to outliers ,meaning it can be greatly influenced by unusually high or low values.
# 2. MEDIAN : The median is the middle value in a dataset when the values are arranged in ascending or descending order .If there are an even number of data points , the median is the average of the two middle values .The median is less affected by extreme values or outliers compared to the mean .
# 3. MODE : The mode is the value that occurs most frequently in a dataset. A dataset can have one mode , more than one mode (multi-modal)  or no mode at all if all values occur with equal frequency.
# 
# RELATIONSHIP :
#   
#  For a perfectly normal distribution , the mean , median and mode are all equal .In practical scenarios ,specially with finite sample sizes ,they may be close but not exactly equal due to sampling variability.

# Ans-13 How is covariance different from correlation ?

# Ans-13
# Covariance indicates the direction of the linear relationship between variables, while correlation measures both the strength and direction of the linear relationship between two variables.
# Correlation is a function of the covariance.
# Covariance is when two variables vary with each other, whereas correlation is when the change in one variable results in the change in another variable.

# Q-14 How do outliers affect measures of central tendency and dispersion ? provide an example .

# Ans-14
# Outliers affect measures of central tendency and dispersion123. Specifically, they:
# 
# 1.Inflate the mean value12
# 2.Have little effect on the median or mode3
# 3.Make the mode useless as a measure of central tendency1
# 4.Are more sensitive to summary measures like the mean and sample standard deviation than rank-based measures like the median and IQR2
# 5.The effect of outliers diminishes as the sample size increases
