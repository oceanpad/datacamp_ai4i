import numpy as np

np.random.seed(43)
random_numbers = np.random.random(size=100)
print(random_numbers)
heads = random_numbers < 0.5
print(heads)
print(np.sum(heads))
