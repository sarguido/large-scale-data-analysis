# Type this into the PySpark shell. 

# Filtering by topic

# Top links with X topic
topics_df.filter(topics_df.topic == 'technology').groupBy('g').count().sort('count', ascending=False).show()

# Top countries with Xother topic
topics_df.filter(topics_df.topic == 'zombies').groupBy('g').count().sort('count', ascending=False).show()