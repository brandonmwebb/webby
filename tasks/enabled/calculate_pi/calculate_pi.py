from mpmath import mp
import json
from datetime import datetime

mp.dps = 1000
pi_str = str(mp.pi).replace('.', '')

try:
    with open('pi_state.json', 'r') as f:
        pos = json.load(f)['position']
except:
    pos = 0

digit = pi_str[pos]
pos += 1

with open('pi_state.json', 'w') as f:
    json.dump({'position': pos, 'digit': digit}, f)

with open('pi_calculation.txt', 'a') as f:
    f.write(f"Position {pos}: {digit} ({datetime.now().isoformat()})\n")

print(f"Position {pos}: {digit}")
