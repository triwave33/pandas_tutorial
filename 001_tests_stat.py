import pandas as pd
import numpy as np

N = 40
columns = ['phys', 'math', 'chem', 'bio', 'en']

### test sample
scores = np.random.randint(0,100, (N,len(columns)))
scores = pd.DataFrame(scores, columns=columns)

# stat
total_scores = scores.sum(axis=1)
mean_score_subjects = scores.mean()

# result
print("total_scores")
print(total_scores.head())

print("mean_score_subjects")
print(mean_score_subjects)

