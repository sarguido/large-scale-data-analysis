# Type this into the PySpark shell. 

# Top links and countries

# Top countries per link
df.groupBy('g', 'c').count().show()

# Top links per country
df.groupBy('c', 'g').count().show()

