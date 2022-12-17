from dataclasses import dataclass
import re

# with open('../test_data.txt', 'r') as f:
with open('../data.txt', 'r') as f:
    lines = f.read().splitlines()

@dataclass
class Valve:
    goto: list
    flow_rate: int

@dataclass
class Route:
    positions: list
    valves_opened: list
    pressure: int
    def __eq__(self, other):
        if self.pressure == other.pressure:
            if sorted(self.valves_opened) == sorted(other.valves_opened):
                if sorted(self.positions) == sorted(other.positions):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


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
        elif len(available_flow_rates) == 1:
            mp += (available_flow_rates.pop(0)[1] * minutes_)
        else:    
            mp += (available_flow_rates.pop(0)[1] * minutes_) + (available_flow_rates.pop(0)[1] * minutes_)
    return mp

print(max_possible(30, Route(positions=['AA', 'AA'], pressure=0, valves_opened=[])))
        

    
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
max_so_far = 3000


start = Route(positions=['AA', 'AA'], valves_opened=[], pressure=0)
routes = [start]
for minute in range(26, 0, -1):
    new_routes = []
    for route in routes:
        pressure = route.pressure
        if pressure > max_so_far:
            print(f'NEW MAX! {pressure}')
            print(route)
            max_so_far = pressure
        valves_opened = route.valves_opened
        positions = route.positions
        position1 = positions[0]
        position2 = positions[1]
        valve1 = valves[position1]
        valve2 = valves[position2]
        # 1st person opens a valve
        if valve1.flow_rate > 0 and position1 not in valves_opened:
            # and 2nd person does too
            if valve2.flow_rate > 0 and position2 not in valves_opened and position1 != position2:
                new_route = Route(
                    positions=[position1, position2],
                    pressure=pressure + (valve1.flow_rate*(minute-1)) + (valve2.flow_rate*(minute-1)),
                    valves_opened=valves_opened+[position1, position2]
                )
                mp = max_possible(minutes=minute-1, route=new_route)
                if mp > max_so_far and new_route not in new_routes:
                    new_routes.append(new_route)
            # and 2nd person moves
            for next_pos in valve2.goto:
                new_route = Route(
                    positions=[position1, next_pos], 
                    pressure=pressure + (valve1.flow_rate*(minute-1)),
                    valves_opened=valves_opened+[position1]
                )
                mp = max_possible(minutes=minute-1, route=new_route)
                if mp > max_so_far and new_route not in new_routes:
                    new_routes.append(new_route)
        # 2nd person opens a valve and 1st person moves
        elif valve2.flow_rate > 0 and position2 not in valves_opened:
            for next_pos in valve1.goto:
                new_route = Route(
                    positions=[next_pos, position2], 
                    pressure=pressure + (valve2.flow_rate*(minute-1)),
                    valves_opened=valves_opened+[position2]
                )
                mp = max_possible(minutes=minute-1, route=new_route)
                if mp > max_so_far and new_route not in new_routes:
                    new_routes.append(new_route)
        # Both move
        for next_pos1 in valve1.goto:
            for next_pos2 in valve2.goto:
                if next_pos1 != next_pos2:
                    new_route = Route(
                        positions=[next_pos1, next_pos2], 
                        pressure=pressure,
                        valves_opened=valves_opened
                    )
                    mp = max_possible(minutes=minute-1, route=new_route)
                    if mp > max_so_far and new_route not in new_routes:
                        new_routes.append(new_route)
                
    routes=new_routes
    # print(routes)
    print(minute-1, len(routes))
    # if minute<30:
    #     break
# print(len(routes))


print(max_so_far)