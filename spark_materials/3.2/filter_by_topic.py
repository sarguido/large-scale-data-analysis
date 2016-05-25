# Type this into the PySpark shell. 

# Filtering by agency

# Top links with Library of Congress agency
agencies_links.filter(agencies_links['Agency'] == 'Library of Congress').groupBy('g').count().sort('count', ascending=False).show()

# Top countries with Department of Education agency
agencies_links.filter(agencies_links['Agency'] == 'Department of Education').groupBy('c').count().sort('count', ascending=False).show()