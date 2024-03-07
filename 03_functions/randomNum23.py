## generate 3 random integers, sleep for 5 seconds
import time
from datetime import datetime
import numpy as np
    
count = 0
while True:
    current_time = datetime.now()
    rng = np.random.default_rng()
    random_integers = rng.integers(low=0, high=10 ** 6, size=3)
    print(f"{current_time}: {random_integers}")
    count += 1
    if count == 10:
        print(f"Script completed")
        break
    time.sleep(5)