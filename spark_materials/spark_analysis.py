# PySpark material

from pyspark import SparkContext

f = 'path/to/file'
sc = SparkContext('local', 'counting')

data = sc.textFile(f)

# prints number of lines in file, a.k.a. number of decodes
print data.count()

from pyspark.sql import SQLContext

sqlContext = SQLContext(sc)

df = sqlContext.read.json(f)

df.show()

# number of rows in the dataframe
df.count()

# count by country

df.groupBy('c').count().alias('count').show()

# top 20 countries ordered

df.groupBy('c').count().alias('count').orderBy('count', ascending=False).show()

# topics

topics_df = df.join(topics, df.u == topics.u, 'inner').collect()

#filter

topics_df.filter(topics_df.topic == 'technology')

