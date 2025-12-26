
from collections import defaultdict

def aggregate(daily):
    table = defaultdict(lambda: defaultdict(int))
    for date, topics in daily.items():
        for t in topics:
            table[t][date] += 1
    return table
