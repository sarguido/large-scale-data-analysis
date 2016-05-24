# These exercises will be done inside of the PySpark shell.
# To launch the PySpark shell, type `pyspark` in the shell.

# Count total clicks
# RDD

filename = 'path/to/file'
data = sc.textFile(f)

# What does the data look like?
data.first()

# Number of total clicks
data.count()

# DataFrame

df = sqlContext.read.json(f)

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
df.filter(df['g'] == '1WmFuVA').show()

# To group by more than one column. Here we're grouping by the link hash
# as well as the user hash, and retreiving the top 20 counts.
df.groupBy('g', 'h').count().sort('count', ascending=False).show()

# Join to topics data
topics_file = 'path/to/topics'
topics_df = sqlContext.read.json(topics_file)

# Only join links where we have the topics - hence `inner`. To join everything,
# even where topics may not exist, use `outer`.
topics_links = df.join(topics_df, df.u == topics.u, 'inner').collect()

topics_links.show()