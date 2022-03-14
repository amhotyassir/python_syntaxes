import pandas as pd
import numpy as np
#################################
#initializing variables to not have errors
n=0
dataframe=[]
number_of_lines_in_the_dataframe=0
df=0
df2=0
default_value=0
dictionnary={}
value=''
line_function=0
#################################
# there are two types: Series and Dataframes; Series are one column dataframes

pd.read_csv('filePath')    # opens the csv file and adding an indexing columns, acting as id and starting from 0.
pd.read_csv('filePath',n)  # does the same thing without creating the additionnal column. It uses the n-th column asthe indexing column
len(dataframe)==number_of_lines_in_the_dataframe

#from now on, we'll consider a dataframe called 'df' with many columns and lines; which 'cities' and 'countries' are two columns

df.head() # prints the whole dataframe
df.head(n) # prints the first n lines

df.set_index('cities') # we set the 'cities' column as the indexing column
df.set_index(['cities','countries']) # we set the combination ('cities','countries')  as the indexing column
df.reset_index() 

df[df['cities']=='Tetouan']
df[(df['cities']=='Tetouan') & (df['countries']=='Morocco')]  

section=df['cities']
section=df[['cities','countries']]

df.fillna(default_value) # returns df but replacing the NaN values by the 'default_value'
                         #!!! this does note change the original dataframe
df.fillna(default_value,inplace=True) # does the same thing but the original dataframe is also changed
df.fillna(method='method_of filling') # see documentation

pd.DataFrame(dictionnary) # Dataframe is basically an object; We can transform any dictionnary into a dataframe
pd.Series(dictionnary)

df.loc[value] # return the lines with index=value. Wether it's 1 column or more ; len(value)==number_of_index_columns
df.iloc[n] # returns the n-th line type(n)=int 

np.sum(df['cities'])

df.rename(columns={'cities':'ct','countries':'ctrs'}) # renames the columns, We ONLY need to insert the columns we seek to rename
df.columns=['column1','column2',...,'column_n'] #renames the columns to 'column1',...,'column_n'
df.rename(mapper=str.strip,axis='columns') # CLEANNING THE DATA: this removes the spaces, if exists, in the end of every columns' name; sp if a column is called 'birthday  ' it will become 'birthday' 
df.columns # returns the names of the dataframe's columns

df.dropna() # removes the lines with NaN values

df.replace(to_replace='.*.html$', value='webpage',regex=True) #REGEX: replaces every text ending with '.html' to 'webpage'

pd.merge(df, df2, how='outer',left_index=True, right_index=True) # This is basically the Union between the two dataframes; the missing values are set to NaN
pd.merge(df,df2,how="inner",left_index=True,right_index=True) # This is the interception of the two datasets
pd.merge(df,df2,how='left',left_index=True,right_index=True) # LEFT JOIN: this returns returns the Union BUT with removing the the lines of the right dataframe 'df2' which are not defined in the left dataframe 'df'
pd.merge(df,df2,how='right',left_index=True,right_index=True) # RIGHT JOIN

pd.merge(df,df2,how='left',on='indexing_column')
pd.merge(df,df2,how='left',on=['indexing_column_1','indexing_column_2',...])

pd.concat([df,df2]) # !!! 'df' and 'df2' should have the same columns
                    # This is basically a Union of the two datasets
pd.concat([df,df2], keys=['grp1','grp2'])

(df.where(df['cities']=='Tetouan')
    .dropna()
    .set_index('countries')
    ) # The '()' state that our code is multi-line
      # !!! takes more time

df.apply(line_function, axis='columns') # this applies the function on every line

