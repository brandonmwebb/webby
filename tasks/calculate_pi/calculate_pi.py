from mpmath import mp
import json

mp.dps = 1000
pi_str = str(mp.pi).replace('.', '')

try:
    with open('pi_state.json', 'r') as f:
        state = json.load(f)
        pos = state['position']
except:
    pos = 0

digit = pi_str[pos]
pos += 1

print(json.dumps({'digit': digit, 'position': pos}))
