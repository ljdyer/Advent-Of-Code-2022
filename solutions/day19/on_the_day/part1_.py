from helper import get_blueprints, Resources, Robots, Route
from dataclasses import dataclass
from copy import deepcopy
from math import ceil

blueprints = get_blueprints()
blueprint = blueprints[0]

new_route = {
    'ore': 0,
    'clay': 0,
    'obsidian': 0,
    'geode': 0,
    'ore_robots': 1,
    'clay_robots': 0,
    'obsidian_robots': 0,
    'geode_robots': 0,
    'time': 0,
    'history': []
}

def finish(route):

    minutes_to_go = 24 - route['time']
    route['geode'] = route['geode'] + (route['geode_robots'] * minutes_to_go)
    return route['geode']



def buy(route, robot_type):
    if robot_type == 'ore_robot':
        if route['ore_robots'] == 0:
            return None
        minutes_until_purchase = ceil((blueprint.ore_robot_cost - route['ore']) / route['ore_robots'])
    elif robot_type == 'clay_robot':
        if route['ore_robots'] == 0:
            return None
        minutes_until_purchase = ceil((blueprint.clay_robot_cost - route['ore']) / route['ore_robots'])
    elif robot_type == 'obsidian_robot':
        if route['ore_robots'] == 0 or route['clay_robots'] == 0:
            return None
        minutes_until_purchase = max(
            ceil((blueprint.obsidian_robot_cost[0] - route['ore']) / route['ore_robots']),
            ceil((blueprint.obsidian_robot_cost[1] - route['clay']) / route['clay_robots'])
        )
    elif robot_type == 'geode_robot':
        if route['ore_robots'] == 0 or route['geode_robots'] == 0:
            return None
        minutes_until_purchase = max(
            ceil((blueprint.geode_robot_cost[0] - route['ore']) / route['ore_robots']),
            ceil((blueprint.geode_robot_cost[1] - route['obsidian']) / route['obsidian_robots'])
        )
    if robot_type == 'ore_robot':
        minutes_until_purchase = ceil((blueprint.ore_robot_cost - route['ore']) / route['ore_robots'])
    elif robot_type == 'clay_robot':
        minutes_until_purchase = ceil((blueprint.clay_robot_cost - route['ore']) / route['ore_robots'])
    elif robot_type == 'obsidian_robot':
        minutes_until_purchase = max(
            ceil((blueprint.obsidian_robot_cost[0] - route['ore']) / route['ore_robots']),
            ceil((blueprint.obsidian_robot_cost[1] - route['clay']) / route['clay_robots'])
        )
    elif robot_type == 'geode_robot':
        minutes_until_purchase = max(
            ceil((blueprint.geode_robot_cost[0] - route['ore']) / route['ore_robots']),
            ceil((blueprint.geode_robot_cost[1] - route['obsidian']) / route['obsidian_robots'])
        )
    minutes_elapsed = minutes_until_purchase + 1
    route['time'] += minutes_elapsed
    if route['time'] > 24:
        return finish(route)
    route['ore'] = route['ore'] + (route['ore_robots'] * minutes_elapsed)
    route['clay'] = route['clay'] + (route['clay_robots'] * minutes_elapsed)
    route['obsidian'] = route['obsidian'] + (route['obsidian_robots'] * minutes_elapsed)
    route['geode'] = route['geode'] + (route['geode_robots'] * minutes_elapsed)
    if robot_type == 'ore_robot':
        route['ore'] -= blueprint.ore_robot_cost
    elif robot_type == 'clay_robot':
        route['ore'] -= blueprint.clay_robot_cost
    elif robot_type == 'obsidian_robot':
        route['ore'] -= blueprint.obsidian_robot_cost[0]
        route['clay'] -= blueprint.obsidian_robot_cost[1]
    elif robot_type == 'geode_robot':
        route['ore'] -= blueprint.geode_robot_cost[0]
        route['obsidian'] -= blueprint.geode_robot_cost[1]
    else:
        raise ValueError
    route[f"{robot_type}s"] += 1
    route['history'] = route['history'] + [robot_type]
    return route

# route = new_route.copy()
# print(route)

# # Buy a clay robot
# route = buy(route, 'clay_robot')
# print(route)
# # Buy a clay robot
# route = buy(route, 'clay_robot')
# print(route)
# # Buy a clay robot
# route = buy(route, 'clay_robot')
# print(route)
# # Buy an obsidian robot
# route = buy(route, 'obsidian_robot')
# # Buy a clay robot
# route = buy(route, 'clay_robot')
# # Buy an obsidian robot
# route = buy(route, 'obsidian_robot')
# # Buy a geode robot
# route = buy(route, 'geode_robot')
# # Buy a geode robot
# route = buy(route, 'geode_robot')
# print(finish(route))

routes = [new_route.copy()]

amounts = []

for i in range(2):
    new_routes = []
    for r in routes:
        new_routes_ = [buy(r.copy(), robot_type) for robot_type in ['ore_robot', 'clay_robot', 'obsidian_robot', 'geode_robot']]
        amounts.extend([r_ for r_ in new_routes_ if isinstance(r_, int)])
        new_routes_ = [r_ for r_ in new_routes_ if isinstance(r_, dict)]
        new_routes.extend(new_routes_)
        # for r_ in new_routes_:
        #     print(r_)
        # print(new_routes)
    routes = new_routes
    for r in routes:
        print(r)
    print()
print(amounts)