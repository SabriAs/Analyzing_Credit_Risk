#!/usr/bin/env python
# coding: utf-8
<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>

<style>
.toggle_button_for_code {
    text-align: center
}
</style>
# # CIS 9650 Final Project: 3

# ## Project Objective
# 
# This project is an exploratory data analysis of credit risk data from a South German Bank. 
# 
# The dataset along with additional info. can be <a href="https://archive.ics.uci.edu/ml/datasets/South+German+Credit" target="_blank">found here</a>.
# 
# ### Student:
# 
# Sabri Asmar | Baruch Email: sabri.asmar@baruchmail.cuny.edu

# <br></br>

# ## Table of Contents
# 
# - [Importing Data](#Importing-Data)
#     - [Legend/ Field Info](#Legend/-Field-Info)
# 
# 
# - [Questions](#Questions)
#     - Question 1: [How many rows, columns, and what information is covered in the data?](#Question-1) 
#     - Question 2: [First, provide high level numbers for the breakdown of credit risk. How many good & bad do we have?](#Question-2)
#     - Question 3: [Provide estimates and/or visualizations that describe the age distribution of the applicants](#Question-3)
#     - Question 4: [Credit risk assignments broken down by age/age groups](#Question-4)
#     - Question 5: [Is there a preference for giving a good credit assignment to older or younger aged applicants?](#Question-5)
#     - Question 6: [Does the bank have favorable outcomes for citizens vs foreigners?](#Question-6)
#     - Question 7: [Is there any preference for specific groups? If so, how?](#Question-7)
#     
# 
# - [Conclusion](#Conclusion)
#     - [Useful Links](#Useful-Links)

# <br></br>

# <center>Press the button to see the code behind everything or just view the notebook with code hidden: </center>
# <form action="javascript:code_toggle()" class="toggle_button_for_code"><input type="submit" id="toggleButton" value="Show Code"></form>

# <br></br>

# ## Importing Data

# In[1]:


# required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

pd.set_option('display.max_columns', 100)
pd.options.mode.chained_assignment = None  # default='warn'

df = pd.read_table('SouthGermanCredit.asc', sep = ' ')

english_column_name_mappings = ["status", "duration", "credit_history",
                                "purpose", "amount", "savings",
                                "employment_duration", "installment_rate",
                                "personal_status_sex", "other_debtors",
                                "present_residence", "property",
                                "age", "other_installment_plans",
                                "housing", "number_credits", "job",
                                "people_liable", "telephone", "foreign_worker",
                                "credit_risk"]

df.columns = english_column_name_mappings

df


# ## Legend/ Field Info

# $`laufkont = status`
#                                                
#  1 : no checking account                       
#  2 : ... < 0 DM                                
#  3 : 0<= ... < 200 DM                          
#  4 : ... >= 200 DM / salary for at least 1 year
# 
# $`laufzeit = duration`
#      
# 
# $`moral = credit_history`
#                                                 
#  0 : delay in paying off in the past            
#  1 : critical account/other credits elsewhere   
#  2 : no credits taken/all credits paid back duly   
#  3 : existing credits paid back duly till now   
#  4 : all credits at this bank paid back duly    
# 
# $`verw = purpose`
#                         
#  0 : others             
#  1 : car (new)          
#  2 : car (used)         
#  3 : furniture/equipment   
#  4 : radio/television      
#  5 : domestic appliances   
#  6 : repairs            
#  7 : education          
#  8 : vacation           
#  9 : retraining         
#  10 : business          
# 
# $`hoehe = amount`
#      
# 
# $`sparkont = savings`
#                                
#  1 : unknown/no savings account   
#  2 : ... <  100 DM             
#  3 : 100 <= ... <  500 DM      
#  4 : 500 <= ... < 1000 DM      
#  5 : ... >= 1000 DM            
# 
# $`beszeit = employment_duration`
#                      
#  1 : unemployed      
#  2 : < 1 yr          
#  3 : 1 <= ... < 4 yrs   
#  4 : 4 <= ... < 7 yrs   
#  5 : >= 7 yrs        
# 
# $`rate = installment_rate`
#                    
#  1 : >= 35         
#  2 : 25 <= ... < 35   
#  3 : 20 <= ... < 25   
#  4 : < 20          
# 
# $`famges = personal_status_sex`
#                                          
#  1 : male : divorced/separated           
#  2 : female : non-single or male : single   
#  3 : male : married/widowed              
#  4 : female : single                     
# 
# $`buerge = other_debtors`
#                  
#  1 : none        
#  2 : co-applicant   
#  3 : guarantor   
# 
# $`wohnzeit = present_residence`
#                      
#  1 : < 1 yr          
#  2 : 1 <= ... < 4 yrs   
#  3 : 4 <= ... < 7 yrs   
#  4 : >= 7 yrs        
# 
# $`verm = property`
#                                               
#  1 : unknown / no property                    
#  2 : car or other                             
#  3 : building soc. savings agr./life insurance   
#  4 : real estate                              
# 
# $`alter = age`
#      
# 
# $`weitkred = other_installment_plans`
#            
#  1 : bank  
#  2 : stores   
#  3 : none  
# 
# $`wohn = housing`
#              
#  1 : for free   
#  2 : rent    
#  3 : own     
# 
# $`bishkred = number_credits`
#          
#  1 : 1   
#  2 : 2-3    
#  3 : 4-5    
#  4 : >= 6   
# 
# $`beruf = job`
#                                                
#  1 : unemployed/unskilled - non-resident       
#  2 : unskilled - resident                      
#  3 : skilled employee/official                 
#  4 : manager/self-empl./highly qualif. employee   
# 
# $`pers = people_liable`
#               
#  1 : 3 or more   
#  2 : 0 to 2   
# 
# $`telef = telephone`
#                               
#  1 : no                       
#  2 : yes (under customer name)   
# 
# $`gastarb = foreign_worker`
#         
#  1 : yes   
#  2 : no 
# 
# $`kredit = credit_risk`
#          
#  0 : bad    
#  1 : good   

# <br></br>

# ## Questions

# ### Question 1

# ### How many rows, columns, and what information is covered in the data?
# 
# <b><u>Full Question:</u></b> Provide details of the dataset - How many rows, columns, what information is covered in
# the data?

# In[2]:


# This tells us that our data set has 1000 rows and 21 columns
print('Our data set has (rows, columns) of:', df.shape)

print(end='\n')

df.info()
# We see from df.info() that we have no missing values and every column contains values that are of int64 datatype


# <br></br>

# Some of the int64 values with their respective text/ categories for some of the columns to make it easier to understand. For the rest, please refer to the legend/ field info.

# In[3]:


# In this section of the code I will replace int64
# values with their respective meaning (change to 
# object if necessary for clearer understanding). 
# Content information is also detailed here.

##### status column ####
# not replacing, refer to legend

#### duration column ####
# no change here, credit duration is in months
# leave as int64

#### credit_history column ####
# not replacing, refer to legend

#### purpose column ####
df['purpose'] = df['purpose'].replace([0,1,2,3,4,5,
                                      6,7,8,9,10],['others','car (new)',
                                                  'car (used)','furniture/equipment',
                                                  'radio/television',
                                                  'domestic appliances','repairs',
                                                  'education','vacationing',
                                                  'retraining','business'])

#### amount column ####
# no change here, credit amount in DM

#### savings column ####
# not replacing, refer to legend

#### employment_duration column ####
# not replacing, refer to legend

#### installment_rate column ####
# not replacing, refer to legend

#### personal_status_sex column ####
# not replacing, refer to legend

#### other_debtors column ####
df['other_debtors'] = df['other_debtors'].replace([1,2,3],['none','co-applicant',
                                                           'guarantor'])

#### present_residence column ####
# not replacing, refer to legend

#### property column ####
# not replacing, refer to legend

#### age column ####
# no change here, age in years

#### other_installment_plans column ####
df['other_installment_plans'] = df['other_installment_plans'].replace([1,2,3],
                                                                      ['bank','stores',
                                                                      'none'])

#### housing column ####
df['housing'] = df['housing'].replace([1,2,3],['free','rent','own'])

#### number_credits column ####
# not replacing, refer to legend

#### job column ####
# not replacing, refer to legend

#### people_liable column ####
df['people_liable'] = df['people_liable'].replace([1,2],['3+','0-2'])

#### telephone column ####
df['telephone'] = df['telephone'].replace([1,2],['no','yes'])

#### foreign_worker column ####
df['foreign_worker'] = df['foreign_worker'].replace([1,2],['yes','no'])

#### credit_risk column ####
# replacing 0 -> "bad", 1 -> "good"
df['credit_risk'] = df['credit_risk'].replace([0,1],['bad','good'])

df # show


# In[4]:


# Info that is covered in the dataframe
df.info()


# <br></br>

# ### Question 2

# ### First, provide high level numbers for the breakdown of credit risk. How many good & bad do we have?
# 
# <b><u>Full Question:</u></b> I am primarily interested in understanding the credit risk assignments. First, provide high level numbers for the breakdown of credit risk. How many good & bad do we have?

# In[5]:


# Size of plot, for some reason .figsize is not working
plt.rcParams["figure.figsize"] = (10, 8)

# Assigning respective good and bad credit number of people
# to variables shown:
good_credit = df['credit_risk'].value_counts()['good']
bad_credit = df['credit_risk'].value_counts()['bad']

print(
'Total Number of People with Good Credit:', good_credit, '\n'
'Total Number of People with Bad Credit:', bad_credit, '\n'
)

# Dataset for bar graph
height = [good_credit, bad_credit]
bars = ("Good Credit", "Bad Credit")
x_pos = np.arange(len(bars))

# Create bars
plt.bar(x=x_pos, height=height, color=['#99ff99','#ff9999'])

# Labeling and general adjustments
plt.xticks(x_pos, bars, fontsize=15)
plt.yticks(fontsize=15)
plt.ylabel("Number of People\n", fontsize=20)
plt.xlabel("\nCredit Type", fontsize=20)
plt.title("Credit Type Breakdown\n", fontsize=25)
plt.figsize=(10,8)

# Show graph
plt.show()


# At a high level, out of the 1,000 people in the data set – there are over 2 times as many people with good credit as there are people with bad credit.

# <br></br>

# ### Question 3

# ### Provide estimates and/or visualizations that describe the age distribution of the applicants
# 
# <b><u>Full Question:</u></b> I want to understand the age of my clientele. Provide estimates and/or visualizations that describe the age distribution of the applicants. Feel free to group/bin ages if needed or use individual distributions.

# In[6]:


# Looking at age statistics
df['age'].describe()


# In[7]:


# Age distribution on box plot
df['age'].plot.box(figsize = (15,8), notch=True, 
                   patch_artist=True, color='#59e6a9', vert=False)

# Title, labels, and fontsize
plt.title('Ages Distribution', fontsize=20)
plt.xlabel('Ages', fontsize=15)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# 50% aka Median 
plt.axvline(df['age'].quantile(q=.5), color='r', label="50th Percentile of Ages")

# See where the mean lies
plt.axvline(df['age'].mean(), color='b', label="Mean Age")
plt.legend(fontsize=15)

# Show plot
plt.show()


# Boxplot above shows majority of ages in the dataset are over 27 years old.

# <br></br>

# In[8]:


# Showing age distribution using a histogram
df.hist(column='age', figsize = (12,8), color='#66b3ff', 
        bins=20) # 20 bins because we have 1,000 datapoints

# Adjusting chart title, labels, fontsizes
plt.title('Age Distribution', fontsize=25)
plt.xlabel('Ages', fontsize=20)
plt.ylabel('Number of People', fontsize=20)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)

# Creating easy label lines at the median and mean
median_age = round(df['age'].median())
mean_age = round(df['age'].mean())
plt.axvline(median_age, color='red', label="Median Age")
plt.axvline(mean_age, color='black', label="Mean Age")
plt.legend(fontsize=25)

# Show histogram
plt.show()

# Print out median and mean ages
print(
'The median age of all 1,000 people is:', median_age, '\n'
'The mean age of all 1,000 people is:', mean_age, '\n'
)


# Distribution is right skewed, meaning the majority of ages in the dataset hover around the 30s here, with decreasing concentrations of older people.

# <br></br>

# ### Question 4

# ### Credit risk assignments broken down by age/age groups
# 
# <b><u>Full Question:</u></b> Calculate frequencies by a suitable age group across risky and not risky applicants. That
# is, show me credit risk assignments broken down by age/age groups.

# <u>Differentiating between old and young ages:</u>
# 
# A quick Google search informs us the average life expectancy in Germany is about 81 years old. With some additional research it's also known that the age you can get a credit card is at 18 years old. 
# 
# <b>Note:</b> To keep things simple, let's assume joint credit card accounts under parents/ guardians are not allowed before the age of 18.
# 
# The average life expectancy in half (81/2 = 40.5) as the cut-off to determine 'young' and 'old'. Anyone of ages above 40.5 will be categorized as 'older applicants'.

# In[9]:


young = [i for i in range(19,41) if i in df.age.tolist()]
old = [i for i in range(41,76) if i in df.age.tolist()]

# Credit assignment broken down by younger applicants #
younger_goodCredit = df[(df.age.isin(young)) 
                         & (df.credit_risk == "good")].value_counts().sum()
younger_badCredit = df[(df.age.isin(young)) 
                         & (df.credit_risk == "bad")].value_counts().sum()
total_younger = younger_goodCredit + younger_badCredit

# Creating DataFrame 
younger_creditAssign_df = pd.DataFrame({
    'Number of People': [younger_goodCredit, younger_badCredit],
    'Credit Type': ['Good Credit', 'Bad Credit']
})

# Pie Chart
younger_creditAssign_df.set_index('Credit Type', inplace=True)
younger_creditAssign_df.plot.pie(y='Number of People', figsize = (6,6),
                                     autopct='%1.1f%%',
                                     fontsize=15, colors=['#99ff99','#ff9999'])

# Title,labels, fontsizes
plt.title('Younger Applicants', fontsize=20)
plt.ylabel(None)

# Show chart
plt.show()

# Print Credit Assignment Numbers
print(
'Number of Younger Applicants with Good Credit:', younger_goodCredit, '\n'
'Number of Younger Applicants with Bad Credit:', younger_badCredit, '\n',
)
print(
'\033[4mInterpretation:\033[0m', "{:.1%}".format(younger_badCredit/total_younger), 
    'of younger applicants (ages 18-40) are risky applicants', '\n'
    'due to having bad credit out of',
    total_younger, 'total younger applicants from the given dataset.'
)

print('\n')

# Credit assignment broken down by older applicants #
older_goodCredit = df[(df.age.isin(old)) 
                         & (df.credit_risk == "good")].value_counts().sum()
older_badCredit = df[(df.age.isin(old)) 
                         & (df.credit_risk == "bad")].value_counts().sum()
total_older = older_goodCredit + older_badCredit

# Creating DataFrame 
older_creditAssign_df = pd.DataFrame({
    'Number of People': [older_goodCredit, older_badCredit],
    'Credit Type': ['Good Credit', 'Bad Credit']
})

# Pie Chart
older_creditAssign_df.set_index('Credit Type', inplace=True)
older_creditAssign_df.plot.pie(y='Number of People', figsize = (6,6),
                                     autopct='%1.1f%%',
                                     fontsize=15, colors=['#99ff99','#ff9999'])

# Title,labels, fontsizes
plt.title('Older Applicants', fontsize=20)
plt.ylabel(None)

# Show chart
plt.show()

# Print Credit Assignment Numbers
print(
'Number of Older Applicants with Good Credit:', older_goodCredit, '\n'
'Number of Older Applicants with Bad Credit:', older_badCredit, '\n',
)
print(
'\033[4mInterpretation:\033[0m', "{:.1%}".format(older_badCredit/total_older), 
    'of older applicants (ages 41+) are risky applicants', '\n'
    'due to having bad credit out of',
    total_older, 'total older applicants from the given dataset.'
)


# From these graphs, looking and comparing just the percentage of "bad credit" ratings between what ages we deemed are young and old, we can see that older applicants are <b>less likely</b> to be given a bad credit rating. 

# <br></br>

# ### Question 5

# ### Is there a preference for giving a good credit assignment to older or younger aged applicants?
# 
# <b><u>Full Question:</u></b> Is there a preference for giving a good credit assignment to older or younger aged applicants? Please determine on your own what you consider ‘young’ and ‘old’ and give a reasonable justification.

# From question 4, there does seem to be a preference towards older aged applicants because the percentage of bad credit is lower than those who we considered young.
# 
# For this question ages will be broken down even further into the following:
# - Young -> Young Adults, Adults
# - Old -> Middle Aged Adults, Seniors

# In[10]:


# We're going to group ages into the following groups:
# 19 to 24 -> Young Adults
# 25 to 44 -> Adults
# 45 to 64 -> Middle Aged Adults
# 65+ (65 to 75 in this case) -> Seniors

# Number of Young Adults
young_adults_age_range = [i for i in range(19,25) if i in df.age.tolist()]
young_adults = df['age'].value_counts()[young_adults_age_range].sum()

# Number of Adults
adults_age_range = [i for i in range(25,45) if i in df.age.tolist()]
adults = df['age'].value_counts()[adults_age_range].sum()

# Number of Middle Aged Adults
middle_aged_adults_age_range = [i for i in range(45,65) if i in df.age.tolist()]
middle_aged_adults = df['age'].value_counts()[middle_aged_adults_age_range].sum()

# Number of Seniors        
seniors_age_range = [i for i in range(65,76) if i in df.age.tolist()]
seniors = df['age'].value_counts()[seniors_age_range].sum()

# Show number of people that fall into each age group:
print(
'Number of Young Adults:', young_adults, '\n'
'Number of Adults:', adults, '\n'
'Number of Middle Aged Adults:', middle_aged_adults, '\n'
'Number of Seniors:', seniors
)


# In[11]:


# Size of plot, for some reason .figsize is not working
plt.rcParams["figure.figsize"] = (15, 8)

# Dataset for bar graph
height = [young_adults, adults, middle_aged_adults, seniors]
bars = ("Young Adults (19-24)", "Adults (25-44)", 
        "Middle Aged Adults (45-64)", "Seniors (65+)")
x_pos = np.arange(len(bars))

# Create bars
ax = plt.bar(x=x_pos, height=height, color=['#99ff99','#ff9999','#66b3ff','#ffcc99'])

# Create names on the x-axis
plt.xticks(x_pos, bars, fontsize=15, rotation=20)
plt.yticks(fontsize=15)
plt.ylabel("Number of People\n", fontsize=20)
plt.xlabel("\nAge Groups", fontsize=20)
plt.title("Age Group Breakdown\n", fontsize=25)

# Show graph
plt.show()


# <br></br>

# Now let's look at the credit risk breakdown in each age category.

# In[12]:


# Credit assignment broken down by young adults #
young_adult_goodCredit = df[(df.age.isin(young_adults_age_range)) 
                         & (df.credit_risk == "good")].value_counts().sum()
young_adult_badCredit = df[(df.age.isin(young_adults_age_range)) 
                         & (df.credit_risk == "bad")].value_counts().sum()
total_young_adults = young_adult_goodCredit + young_adult_badCredit

# Creating DataFrame 
young_adult_creditAssign_df = pd.DataFrame({
    'Number of People': [young_adult_goodCredit, young_adult_badCredit],
    'Credit Type': ['Good Credit', 'Bad Credit']
})

# Pie Chart
young_adult_creditAssign_df.set_index('Credit Type', inplace=True)
young_adult_creditAssign_df.plot.pie(y='Number of People', figsize = (6,6),
                                     autopct='%1.1f%%', explode=(0,0.1),
                                     fontsize=15,colors=['#99ff99','#ff9999'])

# Title, labels, fontsizes
plt.title('Young Adults', fontsize=20)
plt.ylabel(None)
plt.axis('equal')

# Show chart
plt.show()

# Print Credit Assignment Numbers
print(
'Number of Young Adults with Good Credit:', young_adult_goodCredit, '\n'
'Number of Young Adults with Bad Credit:', young_adult_badCredit, '\n',
)
print(
'\033[4mInterpretation:\033[0m', "{:.1%}".format(young_adult_badCredit/total_young_adults), 
    'of young adults (ages 19-24) are risky applicants', '\n'
    'due to having bad credit out of',
    total_young_adults, 'total young adults from the given dataset.'
)

print('\n')

#################################################################################

# Credit assignment broken down by adults #
adults_goodCredit = df[(df.age.isin(adults_age_range)) 
                     & (df.credit_risk == "good")].value_counts().sum()
adults_badCredit = df[(df.age.isin(adults_age_range)) 
                     & (df.credit_risk == "bad")].value_counts().sum()
total_adults = adults_goodCredit + adults_badCredit

# Creating DataFrame
adult_creditAssign_df = pd.DataFrame({
    'Number of People': [adults_goodCredit, adults_badCredit],
    'Credit Type': ['Good Credit', 'Bad Credit']
})

# Pie Chart
adult_creditAssign_df.set_index('Credit Type', inplace=True)
adult_creditAssign_df.plot.pie(y='Number of People', figsize = (6,6),
                                     autopct='%1.1f%%', explode=(0,0.1),
                                     fontsize=15,colors=['#99ff99','#ff9999'])

# Title, labels, fontsizes
plt.title('Adults', fontsize=20)
plt.ylabel(None)
plt.axis('equal')

# Show chart
plt.show()

# Print Credit Assignment Numbers
print(
'Number of Adults with Good Credit:', adults_goodCredit, '\n'
'Number of Adults with Bad Credit:', adults_badCredit, '\n'
)

print(
'\033[4mInterpretation:\033[0m', "{:.1%}".format(adults_badCredit/total_adults), 
    'of adults (ages 25-44) are risky applicants', '\n'
    'due to having bad credit out of',
    total_adults, 'total adults from the given dataset.'
)

print('\n')

#################################################################################

# Credit assignment broken down by middle aged adults #
middle_aged_adults_goodCredit = df[(df.age.isin(middle_aged_adults_age_range)) 
                     & (df.credit_risk == "good")].value_counts().sum()
middle_aged_adults_badCredit = df[(df.age.isin(middle_aged_adults_age_range)) 
                     & (df.credit_risk == "bad")].value_counts().sum()
total_middle_aged_adults = middle_aged_adults_goodCredit + middle_aged_adults_badCredit

# Creating DataFrame
middle_aged_adults_creditAssign_df = pd.DataFrame({
    'Number of People': [middle_aged_adults_goodCredit, 
                         middle_aged_adults_badCredit],
    'Credit Type': ['Good Credit', 'Bad Credit']
})

# Pie Chart
middle_aged_adults_creditAssign_df.set_index('Credit Type', inplace=True)
middle_aged_adults_creditAssign_df.plot.pie(y='Number of People', figsize = (6,6),
                                     autopct='%1.1f%%', explode=(0,0.1),
                                     fontsize=15,colors=['#99ff99','#ff9999'])

# Title, labels, fontsizes
plt.title('Middle Aged Adults', fontsize=20)
plt.ylabel(None)
plt.axis('equal')

# Show chart
plt.show()

# Print Credit Assignment Numbers
print(
'Number of Middle Aged Adults with Good Credit:', middle_aged_adults_goodCredit, '\n'
'Number of Middle Aged Adults with Bad Credit:', middle_aged_adults_badCredit, '\n'
)

print(
'\033[4mInterpretation:\033[0m', "{:.1%}".format(middle_aged_adults_badCredit/total_middle_aged_adults), 
    'of middle aged adults (ages 45-64) are risky applicants', '\n'
    'due to having bad credit out of',
    total_middle_aged_adults, 'total middle aged adults from the given dataset.'
)

print('\n')

#################################################################################

# Credit assignment broken down by seniors #
seniors_goodCredit = df[(df.age.isin(seniors_age_range)) 
                     & (df.credit_risk == "good")].value_counts().sum()
seniors_badCredit = df[(df.age.isin(seniors_age_range)) 
                     & (df.credit_risk == "bad")].value_counts().sum()
total_seniors = seniors_goodCredit + seniors_badCredit

# Creating DataFrame
seniors_creditAssign_df = pd.DataFrame({
    'Number of People': [seniors_goodCredit, seniors_badCredit],
    'Credit Type': ['Good Credit', 'Bad Credit']
})

# Pie Chart
seniors_creditAssign_df.set_index('Credit Type', inplace=True)
seniors_creditAssign_df.plot.pie(y='Number of People', figsize = (6,6),
                                     autopct='%1.1f%%', explode=(0,0.1),
                                     fontsize=15,colors=['#99ff99','#ff9999'])

# Title, labels, fontsizes
plt.title('Seniors', fontsize=20)
plt.ylabel(None)
plt.axis('equal')

# Show chart
plt.show()

# Print Credit Assignment Numbers
print(
'Number of Seniors with Good Credit:', seniors_goodCredit, '\n'
'Number of Seniors with Bad Credit:', seniors_badCredit, '\n'
)

print(
'\033[4mInterpretation:\033[0m', "{:.1%}".format(seniors_badCredit/total_seniors), 
    'of seniors (ages 65+) are risky applicants', '\n'
    'due to having bad credit out of',
    total_seniors, 'total seniors from the given dataset.'
)


# You can see from the above graphs that in order of <i>most risk</i> to <i>least risk</i> applicants (in terms of credit), the age group are as follows:
# 
# - Young Adults (41.3% Bad Credit)
# - Adults (28.9% Bad Credit)
# - Seniors (26.1% Bad Credit)
# - Middle Aged Adults (25% Bad Credit)

# Comparisons are a little easier with grouped bar charts:

# In[13]:


# Young Adults (ages 19-24) #####
## Good Credit ##
numYoungAdults_goodCredit = df[df.age.isin(young_adults_age_range) &
                               df.credit_risk.isin(['good'])].value_counts().sum()


## Bad Credit ##
numYoungAdults_badCredit = df[df.age.isin(young_adults_age_range) &
                               df.credit_risk.isin(['bad'])].value_counts().sum()

########################################################################################

##### Adults (ages 25-44) #####
## Good Credit ##
numAdults_goodCredit = df[df.age.isin(adults_age_range) &
                               df.credit_risk.isin(['good'])].value_counts().sum()


## Bad Credit ##
numAdults_badCredit = df[df.age.isin(adults_age_range) &
                               df.credit_risk.isin(['bad'])].value_counts().sum()

########################################################################################

##### Middle Aged Adults (ages 45-64) #####
## Good Credit ##
numMA_goodCredit = df[df.age.isin(middle_aged_adults_age_range) &
                               df.credit_risk.isin(['good'])].value_counts().sum()


## Bad Credit ##
numMA_badCredit = df[df.age.isin(middle_aged_adults_age_range) &
                               df.credit_risk.isin(['bad'])].value_counts().sum()

########################################################################################

##### Seniors (ages 65+) #####
## Good Credit ##
numSeniors_goodCredit = df[df.age.isin(seniors_age_range) &
                               df.credit_risk.isin(['good'])].value_counts().sum()


## Bad Credit ##
numSeniors_badCredit = df[df.age.isin(seniors_age_range) &
                               df.credit_risk.isin(['bad'])].value_counts().sum()

########################################################################################

#### Grouped Bar Graph Good Credit ####
ageGroup_df = pd.DataFrame(
    {
        'Index':['Young Adults\n(Ages 19-24)', 'Adults\n(Ages 25-44)',
                 'Middle Age Adults\n(Ages 45-64)', 'Seniors\n(Ages 65+)'],
        'Good Credits':[numYoungAdults_goodCredit, 
                       numAdults_goodCredit,
                       numMA_goodCredit,
                       numSeniors_goodCredit],
        'Bad Credits':[numYoungAdults_badCredit, 
                       numAdults_badCredit,
                       numMA_badCredit,
                       numSeniors_badCredit]
    }
)

ax = ageGroup_df.plot(x='Index', y=['Good Credits','Bad Credits'],
                      kind='bar', color=['#99ff99','#ff9999'], 
                      figsize=(15,10))

# Labeling and general adjustments
plt.title("Number of Credits Breakdown by Age Group \n", fontsize=25)
plt.xlabel("\n Groups", fontsize=20)
plt.xticks(fontsize=15, rotation=0)
plt.yticks(fontsize=15)
plt.ylabel("Number of People \n", fontsize=20)
plt.legend(fontsize=20)

# Showing values above each bar, respectively
for p in ax.patches:
    ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                fontsize=15)

# Show
plt.show()


# <br></br>

# Recall the order of <i>most risk</i> to <i>least risk</i> applicants (in terms of credit), the age group are as follows:
# 
# - Young Adults (41.3% Bad Credit)
# - Adults (28.9% Bad Credit)
# - Seniors (26.1% Bad Credit)
# - Middle Aged Adults (25% Bad Credit)

# This might be because people who have good credit are generally older, have higher salaries, and can afford to pay back credits. These older folks will likely have more in their checking accounts as well.
# 
# Diving deeper, let's look at the number of people broken down by the respective age group back from question 4 that meets all the following criteria:
# 
# 1. existing credits paid back duly till now (credit_history value 3)
# 2. all credits at this bank paid back duly (credit_history value 4)
# 3. no credits taken/ all credits paid back duly (credit_history value 2)
# 3. checking account > 0 DM (status values 3,4)
# 4. are not unemployed (shows employment history > 1 year) (unemployment_duration values 3,4,5)
# 4. good credit risk

# In[14]:


# Number of people who meet all criteria:
meets_all_criteria_df = df[df.credit_history.isin([2,3,4]) &
                        df.status.isin([3,4]) &
                        df.employment_duration.isin([3,4,5]) &
                        df.credit_risk.isin(['good'])]

# Total number of people who meet all 6 criteria
meets_all_criteria = meets_all_criteria_df.value_counts().sum()

# Number of young adults (ages 19-24)
num_young_adults = meets_all_criteria_df[meets_all_criteria_df.age.isin(young_adults_age_range)].value_counts().sum() 

# Number of adults (ages 25-44)
num_adults = meets_all_criteria_df[meets_all_criteria_df.age.isin(adults_age_range)].value_counts().sum() 

# Number of middle aged adults (ages 45-64)
num_middle_aged_adults = meets_all_criteria_df[meets_all_criteria_df.age.isin(middle_aged_adults_age_range)].value_counts().sum() 

# Number of seniors (ages 65+)
num_seniors = meets_all_criteria_df[meets_all_criteria_df.age.isin(seniors_age_range)].value_counts().sum() 

# Creating DataFrame
breakdown_df = pd.DataFrame({
    'Number of People': [num_young_adults, num_adults, num_middle_aged_adults,
                         num_seniors],
    'Age Group': ['Young Adults', 'Adults', 'Middle Aged Adults',
                  'Seniors']
})

# Pie Chart
breakdown_df.set_index('Age Group', inplace=True)
breakdown_df.plot.pie(y='Number of People', figsize = (9,9),
                                     autopct='%1.1f%%',
                                     fontsize=15, pctdistance=.85,
                                     colors=['#99ff99','#ff9999','#66b3ff','#ffcc99'],
                                     explode=(0.03,0.03,0.03,0.03))

# Title, labels, fontsizes
plt.title('Breakdown of Age Groups with Good Credit (Meeting all 6 Criteria)', fontsize=20)
plt.legend(fontsize=12)
plt.ylabel(None)
plt.axis('equal')

# Donut
centre_circle = plt.Circle((0,0),0.55,fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

# Show chart
plt.show()

# Print Numbers
print(
'Total number of people who meet all 6 criteria:', meets_all_criteria, '\n'
'Total number of young adults (ages 19-24):', num_young_adults, '\n'
'Total number of adults (ages 25-44):', num_adults, '\n'
'Total number of middle aged adults (ages 45-64):', num_middle_aged_adults, '\n'
'Total number of seniors (ages 65+):', num_seniors,
'\n'
)


# The above chart shows that the majority of people who have good credit are adults in the age range 25-44. This supports the hypothesis that older people generally have good credit because they're more likely to meet the 6 criteria as previously discussed. 
# 
# However what is surprising here is that only 24.2% of middle aged adults have good credit. From earlier, this is the <b>LEAST</b> risky group (while adults ages 24-44 are the <b>second most risky</b>). 
# 
# This is something worth investigating more deeply in the future. This could be because there is a less concentration (number) of people who are aged 45-64 than people who are aged 25-44 who use this bank.

# <br></br>

# ### Question 6

# ### Does the bank have favorable outcomes for citizens vs foreigners?
# 
# <b><u>Full Question:</u></b> Do the same process you did with the ‘age’ variable with ‘foreign_worker’ variable. Does
# the bank have favorable outcomes for citizens vs foreigners?

# In[15]:


# Foreign Workers #
num_foreign_workers = df[df.foreign_worker.isin(['yes'])].value_counts().sum()

num_foreign_goodCredit = df[df.foreign_worker.isin(['yes']) &
                            df.credit_risk.isin(['good'])].value_counts().sum()

num_foreign_badCredit = df[df.foreign_worker.isin(['yes']) &
                            df.credit_risk.isin(['bad'])].value_counts().sum()

###############################################################################

# Citizen Workers #
num_citizen_workers = df[df.foreign_worker.isin(['no'])].value_counts().sum()

num_citizen_goodCredit = df[df.foreign_worker.isin(['no']) &
                            df.credit_risk.isin(['good'])].value_counts().sum()

num_citizen_badCredit = df[df.foreign_worker.isin(['no']) &
                            df.credit_risk.isin(['bad'])].value_counts().sum()

###############################################################################

# Pie Chart #
citizen_foreigner_df = pd.DataFrame(
    {'Foreigners':[num_foreign_goodCredit, num_foreign_badCredit],
     'Citizens':[num_citizen_goodCredit, num_citizen_badCredit]},
    index=['Good Credit', 'Bad Credit']
)

# Turns out you can just use the wedgeprops parameter
# to create the donut shape :)
citizen_foreigner_df.plot.pie(subplots=True, figsize=(15, 15), 
                              colors=['#99ff99','#ff9999'], autopct='%1.1f%%', 
                              explode=(0, 0.09), startangle=95, fontsize=15,
                              wedgeprops=dict(width=.3), pctdistance=.85,
                              shadow=True)

# Adjusting sizes
plt.subplots_adjust(wspace=1)
plt.yticks(fontsize=15)

# Fits subplots cleanly
plt.tight_layout()

# Show
plt.show()

# Print Numbers
print(
'Total Number of Foreign Workers:', num_foreign_workers, '\n \t'
'Foreigners with Good Credit:', num_foreign_goodCredit, '\n \t'
'Foreigners with Bad Credit:', num_foreign_badCredit, '\n'
'----------------------------------------------------------', '\n'
'Total Number of Citizen Workers', num_citizen_workers, '\n \t'
'Citizen Workers with Good Credit:', num_citizen_goodCredit, '\n \t'
'Citizen Workers with Bad Credit:', num_citizen_badCredit, '\n'
)


# From a high level, it seems that banks prefer to give foreign workers the "Good Credit" status compared to German citizens. 
# 
# One possibility could be because foreigners are more likely to take out credits/ loans to get their lives started vs citizens. Therefore, banks give foreign workers the "Good Credit" risk label to incentivize and allow foreign workers to take out more credits.
# 
# However, it's best to take this information here with a grain of salt because the <u>total number of foreign workers who use this bank</u> is <b>VERY</b> low ($\Large\frac{37}{1000}$). German citizens who use the bank outnumber foreigners ~26:1.

# <br></br>

# ### Question 7

# ### Is there any preference for specific groups? If so, how?
# 
# <b><u>Full Question:</u></b> Pick one of the two variables: ‘personal_status_sex’ or ‘housing’. Do a similar analysis
# as you did with ‘age’ and ‘foreign_worker’ with your chosen variable. In the US it’s illegal to discriminate based on marital status or property ownership. Is there any preference for specific groups? If so, how? Please provide some commentary.

# Taking a look at the "personal_status_sex" column, we see that there are values values contain both gender information as well as combined statuses: 
# 
# > $`famges = personal_status_sex`                              
#   1 : male : divorced/separated           
#   2 : female : non-single or male : single    
#   3 : male : married/widowed              
#   4 : female : single   
#  
# This makes it hard to analyze each gender and status separately so for this question I will be using the "housing" column which is much more clear and straightforward:
# 
# > $`wohn = housing`        
#   1 : for free    
#   2 : rent    
#   3 : own     

# Visualzing the breakdown:

# In[16]:


#### Free housing ####
# Total #
num_free_housing = df[df.housing.isin(['free'])].value_counts().sum()

# Good Credit #
free_housing_gc = df[df.housing.isin(['free']) & 
                     df.credit_risk.isin(['good'])].value_counts().sum()

# Bad Credit
free_housing_bc = df[df.housing.isin(['free']) & 
                     df.credit_risk.isin(['bad'])].value_counts().sum()

#############################################################################

#### Total number renting ####
# Total # 
num_renting = df[df.housing.isin(['rent'])].value_counts().sum()

# Good Credit # 
num_renting_gc = df[df.housing.isin(['rent']) & 
                    df.credit_risk.isin(['good'])].value_counts().sum()

# Bad Credit # 
num_renting_bc = df[df.housing.isin(['rent']) & 
                    df.credit_risk.isin(['bad'])].value_counts().sum()

#############################################################################

#### Total number who own house(s) ####
# Total # 
num_own = df[df.housing.isin(['own'])].value_counts().sum()

# Good Credit # 
num_own_gc = df[df.housing.isin(['own']) & 
                df.credit_risk.isin(['good'])].value_counts().sum()

# Bad Credit # 
num_own_bc = df[df.housing.isin(['own']) & 
                df.credit_risk.isin(['bad'])].value_counts().sum()

#########################  Graphs/ Plots  ###################################

# Creating Dataframe
housing_df = pd.DataFrame(
    {
        'Housing Types':['Free','Rented','Own'],
        'Good Credits':[free_housing_gc, num_renting_gc, num_own_gc],
        'Bad Credits':[free_housing_bc, num_renting_bc, num_own_bc]
    }
)

ax = housing_df.plot(x='Housing Types', y=['Good Credits','Bad Credits'],
                      kind='bar',color=['#99ff99','#ff9999'], figsize=(15,10))

# Labeling and general adjustments
plt.title("Credit Risk Breakdown by Housing Types \n", fontsize=25)
plt.xlabel("\n Housing Type", fontsize=20)
plt.xticks(fontsize=15, rotation=0)
plt.yticks(fontsize=15)
plt.ylabel("Number of People \n", fontsize=20)
plt.legend(fontsize=20)

# Showing values above each bar, respectively
for p in ax.patches:
    ax.annotate(p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='center', xytext=(0, 10), textcoords='offset points',
                fontsize=15)

# Show
plt.show()

# Grouped Pie Graph #


# Print numbers
print(
'Total number of people under free housing:', num_free_housing, '\n'
'Total number of people renting:', num_renting, '\n'
'Total number of people own (a/many) homes:', num_own, '\n'
)


# Looking further at the <b>percentage breakdown</b>, more people who rent are given the "good" credit risk label compared to the other two groups. 

# In[17]:


plt.rc('legend', fontsize=13)

# Creating DataFrame
housing_breakdown_df = pd.DataFrame(
    {'Free':[free_housing_gc, free_housing_bc],
     'Rented':[num_renting_gc, num_renting_bc],
     'Own':[num_own_gc, num_own_bc]},
    index=['Good Credit', 'Bad Credit']
)

housing_breakdown_df.plot.pie(subplots=True,
                              colors=['#99ff99','#ff9999'], autopct='%1.1f%%', 
                              explode=(0.03, 0.03), startangle=0, fontsize=15,
                              wedgeprops=dict(width=.3), pctdistance=.85,
                              shadow=True)

# Adjusting sizes
plt.subplots_adjust(wspace=1)

# Fits subplots cleanly
plt.tight_layout()
    
# Show    
plt.show()


# The ordering from <i>most risk</i> to <i>least risk</i> applicants (in terms of credit) are from the following housing situations:
# 
# - Own their own home/homes (41.1%)
# - Free housing (39.1%)
# - Rented housing (26.1%)

# From earlier, recall the "good" credit risk label does seem to preference for older people. It would be interesting to see next the breakdown of the age groups and how they fit into the housing situation here. 
# 
# Recall from [question 5](#Question-5), the order of <i>most risk</i> to <i>least risk</i> applicants (in terms of credit), the age group are as follows:
# 
# - Young Adults (41.3% Bad Credit)
# - Adults (28.9% Bad Credit)
# - Seniors (26.1% Bad Credit)
# - Middle Aged Adults (25% Bad Credit)

# Let's visualize how the "good" credit risk label is distributed by housing type, by age group.

# In[18]:


#### Young Adults (Ages 19-24) #### 
# Free housing # 
youngAdul_freeHouse_total = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['free'])].value_counts().sum()
youngAdul_freeHouse_gc = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
youngAdul_freeHouse_bc = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Renting # 
youngAdul_rent_total = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['rent'])].value_counts().sum()
youngAdul_rent_gc = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
youngAdul_rent_bc = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Own home(s) #
youngAdul_own_total = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['own'])].value_counts().sum()
youngAdul_own_gc = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
youngAdul_own_bc = df[df.age.isin(young_adults_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

#######################################################################################
#### Adults (Ages 25-44) #### 
# Free housing # 
Adult_freeHouse_total = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['free'])].value_counts().sum()
Adult_freeHouse_gc = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
Adult_freeHouse_bc = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Renting # 
Adult_rent_total = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['rent'])].value_counts().sum()
Adult_rent_gc = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
Adult_rent_bc = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Own home(s) #
Adult_own_total = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['own'])].value_counts().sum()
Adult_own_gc = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
Adult_own_bc = df[df.age.isin(adults_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

#######################################################################################
#### Middle Age Adults (Ages 45-64) #### 
# Free housing # 
MA_freeHouse_total = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['free'])].value_counts().sum()
MA_freeHouse_gc = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
MA_freeHouse_bc = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Renting # 
MA_rent_total = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['rent'])].value_counts().sum()
MA_rent_gc = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
MA_rent_bc = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Own home(s) #
MA_own_total = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['own'])].value_counts().sum()
MA_own_gc = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
MA_own_bc = df[df.age.isin(middle_aged_adults_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

#######################################################################################
#### Seniors (Ages 65+) #### 
# Free housing # 
seniors_freeHouse_total = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['free'])].value_counts().sum()
seniors_freeHouse_gc = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
seniors_freeHouse_bc = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['free']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Renting # 
seniors_rent_total = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['rent'])].value_counts().sum()
seniors_rent_gc = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
seniors_rent_bc = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['rent']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()

# Own home(s) #
seniors_own_total = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['own'])].value_counts().sum()
seniors_own_gc = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['good'])].value_counts().sum()
seniors_own_bc = df[df.age.isin(seniors_age_range) & 
                            df.housing.isin(['own']) & 
                            df.credit_risk.isin(['bad'])].value_counts().sum()


# In[19]:


#### Horizontal Stacked Bar Graph: Good Credit Only ####
# Creating dataframe
dataFrame = pd.DataFrame({"Age Groups": ['Young Adults\n(Ages 19-24)',
                                         'Adults\n(Ages 25-44)',
                                         'Middle Age Adults\n(Ages 45-64)',
                                         'Seniors\n(Ages 65+)'],
                          "Free Housing": [youngAdul_freeHouse_gc,
                                           Adult_freeHouse_gc,
                                           MA_freeHouse_gc,
                                           seniors_freeHouse_gc],
                          "Renting": [youngAdul_rent_gc, Adult_rent_gc,
                                      MA_rent_gc, seniors_rent_gc],
                          "Own": [youngAdul_own_gc, Adult_own_gc,
                                  MA_own_gc, seniors_own_gc]
})

# plotting stacked Horizontal Bar Chart with all the columns
#dataFrame.plot.barh(stacked=True, title='Car Specifications', color=("orange", "cyan"))
ax = dataFrame.plot(x="Age Groups", 
                    y=['Free Housing','Renting','Own'],
                      kind='barh', stacked=True,
                      figsize=(20,12), color=['#99ff99','#ff9999','#66b3ff'])

# Grid line adjustments
ax.xaxis.grid(color='grey', linestyle='dashed')

# Labeling and general adjustments
plt.title('Good Credit Breakdown of Housing Type by Age Group\n',
          fontsize=25)   
plt.legend(fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.ylabel('Age Groups\n', fontsize=23)
plt.xlabel('\nNumber of People', fontsize=23)
    
# display the plotted Horizontal Bar Chart
plt.show()

# Print Numbers
print(
'Total Number of Good Credit Seniors (Ages 65+) :', numSeniors_goodCredit, '\n\t'
    'Number of Free Housing:', seniors_freeHouse_gc, '|', 
                               round((seniors_freeHouse_gc/numSeniors_goodCredit)*100,2),'%','\n\t' 
    'Number Renting:', seniors_rent_gc, '|', 
                       round((seniors_rent_gc/numSeniors_goodCredit)*100,2),'%', '\n\t' 
    'Number Own:', seniors_own_gc, '|', 
                   round((seniors_own_gc/numSeniors_goodCredit)*100,2),'%', '\n'
'---------------------------------------------------------------------\n'
'Total Number of Good Credit Middle Aged Adults (Ages 45-64):', numMA_goodCredit, '\n\t'
    'Number of Free Housing:', MA_freeHouse_gc, '|', 
                               round((MA_freeHouse_gc/numMA_goodCredit)*100,2),'%', '\n\t' 
    'Number Renting:', MA_rent_gc, '|', 
                       round((MA_rent_gc/numMA_goodCredit)*100,2),'%', '\n\t' 
    'Number Own:', MA_own_gc, '|', 
                   round((MA_own_gc/numMA_goodCredit)*100,2),'%', '\n'
'---------------------------------------------------------------------\n'
'Total Number of Good Credit Adults (Ages 25-44):', numAdults_goodCredit, '\n\t'
    'Number of Free Housing:', Adult_freeHouse_gc, '|', 
                               round((Adult_freeHouse_gc/numAdults_goodCredit)*100,2),'%', '\n\t' 
    'Number Renting:', Adult_rent_gc, '|', 
                       round((Adult_rent_gc/numAdults_goodCredit)*100,2),'%', '\n\t' 
    'Number Own:', Adult_own_gc, '|', 
                   round((Adult_own_gc/numAdults_goodCredit)*100,2),'%', '\n'
'---------------------------------------------------------------------\n'
'Total Number of Good Credit Young Adults (Ages 19-24):', numYoungAdults_goodCredit, '\n\t'
    'Number of Free Housing:', youngAdul_freeHouse_gc, '|', 
                               round((youngAdul_freeHouse_gc/numYoungAdults_goodCredit)*100,2),'%', '\n\t' 
    'Number Renting:', youngAdul_rent_gc, '|', 
                       round((youngAdul_rent_gc/numYoungAdults_goodCredit)*100,2),'%', '\n\t' 
    'Number Own:', youngAdul_own_gc, '|', 
                   round((youngAdul_own_gc/numYoungAdults_goodCredit)*100,2),'%', '\n'
'---------------------------------------------------------------------\n'
)


# Although it initially looked like the "good" credit risk label is given to those who rent, it can be seen now that the majority of people who are renting (and have the respective good credit label) are adults aged 25-44 (80.99%). 
# 
# This is the same age group back in [question 5](#Question-5) where it is theorized people in this age group, people tend to have better credit. If good crediting ratings are given to those who rent, it cannot be denied that age might have something to do with it. 

# <br></br>

# ## Conclusion

# After solving the last 3 question, the question "which factor/ predictor has the strongest weight on determining credit risk" remained. To conclude this project, a correlation matrix can be used to give us a shortcut into answering the stated question.

# Some of the variables that have not been looked at before will be brought into a dataframe and correlated to one another. Note that not all factors can be looked at because they do not increase with respect to the values (labels) assigned to them - even if the values/ labels were remapped. 
# 
# For example, age and savings can be correlated, but age and personal_status_sex, not so much. We can also correlate qualitative columns too like credit_risk and credit_history. 

# In[20]:


# seaborn library
import seaborn as sns

# reimporting dataset
df_2 = pd.read_table('SouthGermanCredit.asc', sep = ' ')

# Mapping english names to columns
english_column_name_mappings = ["status", "duration", "credit_history",
                                "purpose", "amount", "savings",
                                "employment_duration", "installment_rate",
                                "personal_status_sex", "other_debtors",
                                "present_residence", "property",
                                "age", "other_installment_plans",
                                "housing", "number_credits", "job",
                                "people_liable", "telephone", "foreign_worker",
                                "credit_risk"]

df_2.columns = english_column_name_mappings

#### status column value replacement ####
df_2['status'] = df_2['status'].replace([1,2,3,4],[0,1,2,3]) # TIL- not actually needed

# New dataframe that only includes the following:
corr_df = df_2[['age','status','savings',
                'credit_history', 'number_credits', 'credit_risk']]

# Renaming columns in new dataframe
corr_df.rename(columns={"age": "Age", 
                        "status": "$ in Checking Acc.",
                        "savings": "Savings",
                        "credit_history": "Quality Credit History",
                        "number_credits": "Number of Credits",
                        "credit_risk": "Credit Risk (Bad: 0 | Good: 1)"}, inplace=True)

# Show
corr_df


# Let's take a look at the correlations as well as its heatmap using the seaborn library.

# In[21]:


# Creating a correlation matrix using 
corr_matrix = corr_df.corr()

# Show correlation matrix with the heatmap below it in output
display(corr_matrix)

# Spacing in output
print('\n')
print('\n')

# Seaborn heatmap
sns.set(font_scale=1.5)
plt.figure(figsize = (10,5))
corr_heatmap = sns.heatmap(corr_matrix, cmap = 'PiYG', annot = True, 
                           vmin = 0, vmax = 1)
corr_heatmap.set_xticklabels(corr_heatmap.get_xticklabels(), rotation=75)
plt.title('Correlations \n', fontsize = 30)

# Show
plt.show()


# It turns out that what was initially believed age to be the biggest factor in determining credit risk is <b>untrue</b>. The amount in a person's checking account with the bank is has the strongest, positive correlation here at 0.35, with the second largest factor being one's quality credit history with the bank. 

# ### Useful Links

# - <a href="https://datatofish.com/replace-values-pandas-dataframe/" target="_blank">Pandas DataFrame.replace method</a>
# 
# - <a href="https://datacommons.org/place/country/DEU?utm_medium=explore&mprop=lifeExpectancy&popt=Person&hl=en" target="_blank">Germany Life Expectancy</a>
# 
# - <a href="https://medium.com/@kvnamipara/a-better-visualisation-of-pie-charts-by-matplotlib-935b7667d77f" target="_blank">Better Visualizing Pie Charts (Medium Article)</a>
# 
# - <a href="https://www.schemecolor.com/" target="_blank">Color Schemes and Hex Codes</a>
# 
# - <a href="https://seaborn.pydata.org/generated/seaborn.heatmap.html" target="_blank">Seaborn Heatmap</a>
# 
# - <a href="https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.corr.html" target="_blank">Correlation Matrix</a>
# 
# - <a href="https://matplotlib.org/stable/tutorials/intermediate/tight_layout_guide.html" target="_blank">Tight Layout Guide</a>
# 
# - <a href="https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.subplots_adjust.html" target="_blank">Subplot Whitespace</a>
# 
# - <a href="https://stackoverflow.com/questions/57767463/drawing-multiple-donut-charts" target="_blank">wedgeprops parameter</a>
# 
# - <a href="https://stackoverflow.com/questions/23591254/python-pandas-matplotlib-annotating-labels-above-bar-chart-columns" target="_blank">Annotating Bar Graph Bars</a>

# <center><a href="#CIS-9650-Final-Project:-Group-3">Click here</a> to return to top of page.</center>

# <br></br>
<script>
  $(document).ready(function(){
    $('div.prompt').hide();
    $('div.back-to-top').hide();
    $('nav#menubar').hide();
    $('.breadcrumb').hide();
    $('.hidden-print').hide();
  });
</script>