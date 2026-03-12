import json

pi = "31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

with open('pi_state.json', 'r') as f:
    state = json.load(f)
    pos = state['position']

next_pos = pos + 1
next_digit = pi[next_pos]

state['position'] = next_pos
state['digit'] = next_digit

with open('pi_state.json', 'w') as f:
    json.dump(state, f)

print(f"Position: {next_pos}, Digit: {next_digit}")
