from dataclasses import dataclass
import re

with open('../test_data.txt', 'r') as f:
# with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()

@dataclass
class Valve:
    goto: list
    flow_rate: int

@dataclass
class Route:
    me_pos: str
    elephant_pos: str
    valves_opened: list
    pressure: int


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

flow_rates = list(reversed(sorted(
    [(k, v.flow_rate) for k, v in valves.items()], key=lambda x: x[1]
)))

print(flow_rates)
# # print(flow_rates)
def max_possible(minutes, route):
    pressure = route.pressure
    valves_opened = route.valves_opened
    mp = pressure
    available_flow_rates = [f for f in flow_rates if f[0] not in valves_opened]
    mp += (available_flow_rates.pop(0)[1] * (minutes-1)) + (available_flow_rates.pop(0)[1] * (minutes-1))
    for minutes_ in range(minutes-3, 0, -2):
        if not available_flow_rates:
            break
        mp += (available_flow_rates.pop(0)[1] * minutes_) + (available_flow_rates.pop(0)[1] * minutes_)
    return mp

print(max_possible(30, Route(me_pos='AA', elephant_pos='AA', pressure=0, valves_opened=[])))
        

    
# print(max_possible)


current_pos = 'AA'
valves_visited = []
valves_opened = []
pressure = 0

# for minute in range(30, 0, -1):
#     current_valve = valves[current_pos]
#     valves_visited.append(current_pos)
#     if current_valve.flow_rate > 0 and current_pos not in valves_opened:
#         valves_opened.append(current_pos)
#         pressure += (minute - 1) * current_valve.flow_rate
#     else:
#         unvisited = sorted([v for v in current_valve.goto if v not in valves_visited])
#         if unvisited:
#             move_to = min(unvisited)
#         current_pos = move_to
# print(pressure)
max_so_far = 1600


start = Route(me_pos='AA', elephant_pos='AA', valves_opened=[], pressure=0)
routes = [start]
for minute in range(30, 0, -1):
    new_routes = []
    for route in routes:
        pressure = route.pressure
        if pressure > max_so_far:
            print(f'NEW MAX! {pressure}')
            max_so_far = pressure
        valves_opened = route.valves_opened
        me_pos = route.me_pos
        elephant_pos = route.elephant_pos
        current_valve = valves[current_pos]
        if current_valve.flow_rate > 0 and current_pos not in valves_opened:
            new_route = Route(
                current_pos=current_pos,
                pressure=pressure + (current_valve.flow_rate*(minute-1)),
                valves_opened=valves_opened+[current_pos]
            )
            mp = max_possible(minutes=minute-1, route=new_route)
            if mp > max_so_far and new_route not in new_routes:
                    new_routes.append(new_route)
        for next_pos in current_valve.goto:
            new_route = Route(
                current_pos=next_pos,
                pressure=pressure,
                valves_opened=valves_opened
            )
            mp = max_possible(minutes=minute-1, route=new_route)
            if mp > max_so_far and new_route not in new_routes:
                new_routes.append(new_route)
    routes=new_routes
    print(minute-1, len(routes))
# print(len(routes))


