friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

import random

num = random.randint(0, (len(friends)-1))
print(friends[num])

print(random.choice(friends))