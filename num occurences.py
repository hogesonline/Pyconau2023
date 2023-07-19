# Count the Number of Occurrences in a Python list using Counter
from collections import Counter
items = ['a', 'b', 'a', 'c', 'd', 'd', 'd', 'c', 'a', 'b']

counts = Counter(items)
print(counts)