from dataclasses import dataclass
import re

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()
with open('../min_dists.txt', 'r') as f:
    min_dists = eval(f.read())

@dataclass
class Valve:
    goto: list
    flow_rate: int

@dataclass
class Route:
    current_pos: str
    valves_opened: list
    pressure: int
    minutes: int

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
    
routes = [Route('AA', [], 0, 30)]


max_ = 0 
for round in range(1):
    if not routes:
        break
    new_routes = []
    for route in routes:
        for dest, dist in valves[route.current_pos].goto:
            if dest not in route.valves_opened:
                minutes = route.minutes - dist - 1
                if minutes > 0:
                    new_route = Route(dest, route.valves_opened+[dest], route.pressure+(valves[dest].flow_rate*minutes), minutes)
                    new_routes.append(new_route)
                else:
                    max_ = max(max_, route.pressure)
    routes = new_routes
    print(f'Completed round {round+1}')
print(max_)