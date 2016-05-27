# These exercises will be done inside of the PySpark shell.
# To launch the PySpark shell, type `pyspark` in the shell.

# Count total clicks
# RDD

filename = 'hdfs:///user/vagrant/sample_data/1usagov_data'
data = sc.textFile(filename)

# What does the data look like?
data.first()

# Number of total clicks
data.count()

# DataFrame

df = sqlContext.read.json(filename)

#What does the data look like?
df.show()

# Number of total clicks
df.count()

# Count clicks by hash
df.groupBy('g').count().show()

# To get only the top 20:
df.groupBy('g').count().sort('count', ascending=False).show()

# To get only decodes with a particular user hash, use square brackets to
# access the column
df.filter(df['g'] == '20fb21D').show()

# To get the decodes with a particular hash and particular country, filter twice
df.filter(df['g'] == '20fb21D').filter(df['c'] == 'US').show()

# To filter by multiple values in the same column, use .isin()
df.filter(df['g'].isin(['20fb21D', '1N8VwTx'])).show()

# To group by more than one column. Here we're grouping by the link hash
# as well as the user hash, and retreiving the top 20 counts.
df.groupBy('g', 'h').count().sort('count', ascending=False).show()

# To sort by multiple fields:
df.groupBy('g', 'h').count().sort(['g', 'count'], ascending=False).show()

# Join to topics data
agency_file = 'hdfs:///user/vagrant/sample_data/agency_map'
agency_df = sqlContext.read.json(agency_file)

# Only join links where we have the topics - hence `inner`. To join everything,
# even where topics may not exist, use `outer`.
agencies_links = df.join(agency_df, df['g'] == agency_df['Global Hash'], 'inner')

agencies_links.show()