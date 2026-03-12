from decimal import Decimal, getcontext
import json

getcontext().prec = 100

def calculate_pi(digits):
    getcontext().prec = digits + 10
    return sum(1/Decimal(16)**k * (Decimal(4)/(8*k+1) - Decimal(2)/(8*k+4) - Decimal(1)/(8*k+5) - Decimal(1)/(8*k+6)) for k in range(digits))

with open('pi_state.json', 'r') as f:
    state = json.load(f)

position = state['position']
pi_value = str(calculate_pi(position + 1)).replace('.', '')
digit = pi_value[position]

state['position'] = position + 1
state['current_digit'] = digit

with open('pi_state.json', 'w') as f:
    json.dump(state, f)

with open('pi_calculation.txt', 'a') as f:
    f.write(f"Position {position + 1}: {digit}\n")

print(f"Digit at position {position + 1}: {digit}")
