import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

start_time = "0:00:00"
end_time = "1:24:52"
freq = 'min'

time = pd.date_range(start=start_time, end=end_time, freq=freq)

N = len(time)

# data 
ar = np.random.rand(N)
df = pd.DataFrame(ar, columns=['s1'], index=time)

print("df")
print(df.head())

df.plot()
plt.show()
