from dataclasses import dataclass
from typing import List
from copy import deepcopy
import re

with open('../test_data.txt', 'r') as f:
# with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()
with open('../min_dists2.txt', 'r') as f:
    min_dists = eval(f.read())

@dataclass
class Valve:
    goto: list
    flow_rate: int

@dataclass
class Route:
    current_pos: List[str]
    valves_opened: list
    pressure: int
    minutes: List[int]
    mover: int
    def __eq__(self, other):
        if sorted(self.current_pos) == sorted(other.current_pos):
            if sorted(self.valves_opened) == sorted(other.valves_opened):
                if self.pressure <= other.pressure:
                    if self.minutes[0] < other.minutes[0] and self.minutes[1] < other.minutes[1]:
                        return True
        return False
    def __hash__(self):
        return hash(repr(self))


valves = {}
for l in lines:
    valve_names = re.findall(r'[A-Z]{2}', l)
    flow_rate = re.findall(r'flow rate=(\d+);', l)
    this_valve = Valve(goto=valve_names[1:], flow_rate=int(flow_rate[0]))
    valves[valve_names[0]] = this_valve

flow_rates = list(reversed(sorted(
    [(k, v.flow_rate) for k, v in valves.items()], key=lambda x: x[1]
)))

valves = {n: v for n, v in valves.items() if (v.flow_rate > 0 or n == 'AA')}
for n in valves.keys():
    valves[n].goto=[(x, min_dists[n][x]) for x in valves.keys()]
print(valves.keys())
    
routes = [Route(['AA', 'AA'], [], 0, [26, 26], 0)]

max_ = 0 
for round in range(10):
    if not routes:
        break
    new_routes = []
    for route in routes:
        mover = route.mover
        valves_opened = route.valves_opened
        pos_mover = route.current_pos[mover]
        minutes_mover = route.minutes[mover]
        goto_mover = valves[pos_mover].goto
        goto_mover = [g for g in goto_mover if g[0] not in valves_opened and valves[g[0]].flow_rate > 0]
        goto_minutes = [(g, minutes_mover-g[1]-1) for g in goto_mover]
        goto_minutes = [g for g in goto_minutes if g[1] > 0]
        if goto_minutes:
            for g in goto_minutes:
                g, minutes_ = g
                new_route = deepcopy(route)
                new_route.current_pos[mover] = g[0]
                new_route.minutes[mover] = minutes_
                new_route.pressure += minutes_ * valves[g[0]].flow_rate
                new_route.valves_opened.append(g[0])
                new_routes.append(new_route)
        elif mover == 0:
            new_route = deepcopy(route)
            new_route.mover = 1
            new_routes.append(new_route)
        # else:
        max_ = max(max_, route.pressure)
    routes = set(new_routes)
    for r in routes:
        print(r)
    print(f'Completed round {round+1} ({len(routes)} routes to reconcile)')
    print(max_)
print(max_)
print(valves['AA'])