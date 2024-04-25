import pandas as pd
import matplotlib.pyplot as plt             ## python3 -m pip install -U matplotlib
ted = pd.read_csv('05_pandas23/ted11.csv')
ted.comments.plot()
plt.show()