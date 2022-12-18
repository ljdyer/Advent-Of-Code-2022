from dataclasses import dataclass
import re

with open('../test_data.txt', 'r') as f:
# with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()

@dataclass
class Valve:
    goto: list
    flow_rate: int

valves = {}
for l in lines:
    valve_names = re.findall(r'[A-Z]{2}', l)
    assert len(valve_names) > 1
    flow_rate = re.findall(r'flow rate=(\d+);', l)
    assert len(flow_rate) == 1
    this_valve = Valve(
        goto=valve_names[1:],
        flow_rate=int(flow_rate[0])
    )
    valves[valve_names[0]] = this_valve

# print(valves.keys())

valve1 = 'SY'
valve2 = 'TS'

def min_dist(valve1, valve2) -> int:
    can_go_to = [valve1]
    for i in range(50):
        if valve2 in can_go_to:
            break
        # print(can_go_to)
        can_go_to = [g for v in can_go_to for g in valves[v].goto]
    return i

dists = {x: {y: min_dist(x, y) for y in valves.keys()} for x in valves.keys()}
print(dists)


# print(min_dist('AA', 'AJ'))