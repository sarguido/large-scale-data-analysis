# Spark solution!
# Please run this material in the PySpark shell.

# To filter down to China (CN), Denmark (DE), and France (FR).
filtered_countries = agencies_links.filter(agencies_links['c'].isin(['DE', 'CN', 'FR']))

# Now, let's pick some agencies.
agency_list = ['Department of Health And Human Services', 'The Legislative Branch (Congress)', 'Department of Commerce']

# Let's once again filter down that dataframe of countries.
c_agency = filtered_countries.filter(filtered_countries['Agency'].isin(agency_list))

# Okay, let's take a look! Let's start with China and the Department of Commerce.
c_agency.filter(c_agency['c'] == 'CN').filter(c_agency['Agency'] == 'Department of Commerce').groupBy('g').count().sort('count', ascending=False).show()

# What about Denmark and the Chamber of Commerce?
c_agency.filter(c_agency['c'] == 'DE').filter(c_agency['Agency'] == 'Department of Commerce').groupBy('g').count().sort('count', ascending=False).show()

# What about Denmark and the Legislative Branch?
c_agency.filter(c_agency['c'] == 'DE').filter(c_agency['Agency'] == 'The Legislative Branch (Congress)').groupBy('g').count().sort('count', ascending=False).show()

# By now you get the picture. You could write a function, if you wanted to:
def spark_exercise(df, country, agency):
    return df.filter(df['c'] == country).filter(df['Agency'] == agency).groupBy('g').count().sort('count', ascending=False).show()

# Or, you could break out the countries into separate dataframes and work with them that way:
denmark = agencies_links.filter(agencies_links['c'] == 'DE')
china = agencies_links.filter(agencies_links['c'] == 'CN')
france = agencies_links.filter(agencies_links['c'] == 'FR')

denmark.filter(c_agency['Agency'] == 'Department of Commerce').groupBy('g').count().sort('count', ascending=False).show()
