# Type this into the PySpark shell. 

# Top links and countries

# Top countries per link
df.groupBy('g', 'c').count().sort('count', ascending=False).show()

# Top links per country
df.groupBy('c', 'g').count().sort('count', ascending=False).show()

