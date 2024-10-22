import time
from tqdm import tqdm
for i in tqdm(range(1,11), desc='Processing'):
    time.sleep(0.5)
with tqdm(total=10, desc='Manual') as pbar:
    for i in range(1,11):
        time.sleep(0.5)
        pbar.update(1)