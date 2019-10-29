#!/usr/bin/env python
# coding: utf-8

# https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/causesofdeath/datasets/alcoholspecificdeathsintheukmaindataset

# In[1]:


from gssutils import *
scraper = Scraper('https://www.ons.gov.uk/peoplepopulationandcommunity/healthandsocialcare/causesofdeath/datasets/alcoholspecificdeathsintheukmaindataset')
scraper


# In[3]:


next_table = pd.DataFrame()
sheet = scraper.distributions[0].as_databaker()


# In[4]:


get_ipython().run_cell_magic('capture', '', '%run "Tab1.ipynb"\nnext_table = pd.concat([next_table, Final_table])\n\n%run "Tab2.ipynb"\nnext_table = pd.concat([next_table, Final_table])\n\n%run "Tab3.ipynb"\nnext_table = pd.concat([next_table, Final_table])\n\n%run "Tab4.ipynb"\nnext_table = pd.concat([next_table, Final_table])\n\n%run "Tab5.ipynb"\nnext_table = pd.concat([next_table, Final_table])\n\n%run "Tab6.ipynb"\nnext_table = pd.concat([next_table, Final_table])\n\n%run "Tab7.ipynb"\nnext_table = pd.concat([next_table, Final_table])\n\n%run "Tab8.ipynb"\nnext_table = pd.concat([next_table, Final_table])')


# In[5]:


next_table['Age'] = next_table['Age'].map(
    lambda x: {
        'All' : 'all', 
        '01-04' : 'agq/1-4',
        '05-09': 'agq/5-9' ,
        '10-14': 'agq/10-14',
        '15-19': 'agq/15-19',
        '20-24': 'agq/20-24',
        '25-29': 'agq/25-29',
        '30-34': 'agq/30-34',
        '35-39': 'agq/35-39',
        '40-44': 'agq/40-44',
        '45-49': 'agq/45-49',
        '50-54': 'agq/50-54',
        '55-59': 'agq/55-59',
        '60-64': 'agq/60-64',
        '65-69': 'agq/65-69',
        '70-74': 'agq/70-74',
        '75-79': 'agq/75-79',
        '80-84': 'agq/80-84',
        '85+'  : 'agq/85-plus',
        '<1'  :  'agq/under-1'
        
        }.get(x, x))


# In[6]:


next_table.rename(index= str, columns= {'Upper 95% confidence limit':'CI Upper','Lower 95% confidence limit':'CI Lower'}, inplace = True)


# In[7]:


next_table = next_table[['Age', 'Geography', 'CI Lower', 'Measure Type', 'Sex', 'Unit', 'CI Upper', 'Value', 'Year']]


# In[8]:


from pathlib import Path
out = Path('out')
out.mkdir(exist_ok=True)
next_table.to_csv(out / 'observations.csv', index = False)


# In[10]:


scraper.dataset.family = 'health'
with open(out / 'dataset.trig', 'wb') as metadata:
    metadata.write(scraper.generate_trig())
    

csvw = CSVWMetadata('https://gss-cogs.github.io/ref_alcohol/')
csvw.create(out / 'observations.csv', out / 'observations.csv-schema.json')


# In[ ]:




