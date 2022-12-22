from helper import get_blueprints, Resources, Robots, Route
from dataclasses import dataclass
from copy import deepcopy

blueprints = get_blueprints()
# for b in blueprints:
#     print(b)

def can_buy(blueprint, resources):
    can_buy = []
    if resources.ore > blueprint.ore_robot_cost:
        can_buy.append('ore_robot')
    if resources.ore > blueprint.clay_robot_cost:
        can_buy.append('clay_robot')
    if resources.ore > blueprint.obsidian_robot_cost[0] \
     and resources.clay > blueprint.obsidian_robot_cost[1]:
        can_buy.append('obsidian_robot')
    if resources.ore > blueprint.geode_robot_cost[0] \
     and resources.obsidian > blueprint.geode_robot_cost[1]:
        can_buy.append('geode_robot')
    return can_buy

def get_resources(resources, robots):
    resources.ore += robots.ore
    resources.clay += robots.clay
    resources.obsidian += robots.obsidian
    resources.geode += robots.geode
    return resources

def buy(robot_type, blueprint, resources, robots):
    if robot_type == 'ore_robot':
        resources.ore -= blueprint.ore_robot_cost
        robots.ore += 1
        return resources, robots
    if robot_type == 'clay_robot':
        resources.ore -= blueprint.clay_robot_cost
        robots.clay += 1
        return resources, robots
    if robot_type == 'obsidian_robot':
        resources.ore -= blueprint.obsidian_robot_cost[0]
        resources.clay -= blueprint.obsidian_robot_cost[1]
        robots.obsidian += 1
        return resources, robots
    if robot_type == 'geode_robot':
        resources.ore -= blueprint.geode_robot_cost[0]
        resources.obsidian -= blueprint.geode_robot_cost[1]
        robots.geode += 1
        return resources, robots
    raise ValueError
    
def max_geode_possible(route, minutes_remaining):

    geode_now = route.resources.obsidian
    geode_robots_now = route.robots.obsidian
    max_geode = geode_now + geode_robots_now * minutes_remaining
    while minutes_remaining > 0:
        minutes_remaining -= 1
        max_geode += minutes_remaining
    return max_geode


print(Resources(0,0,0,0))
routes = [Route(
    Robots(1,0,0,0),
    Resources(0,0,0,0)
)]

max_so_far = 6
blueprint = blueprints[0]
for m in range(24):
    print(f"Round {m+1}")
    new_routes = []
    for r in routes:
        r.resources = get_resources(r.resources, r.robots)
        new_routes.append(deepcopy(r))
        can_buy_ = can_buy(blueprint, r.resources)
        for robot_type in can_buy_:
            new_r = deepcopy(r)
            new_r.resources, new_r.robots = buy(robot_type, blueprint, new_r.resources, new_r.robots)
            if max_geode_possible(new_r, 24-m) > max_so_far:
                new_routes.append(new_r)
    # for r in new_routes:
    #     print(r)
    routes = set(new_routes)
    print(len(routes))

print(max([r.resources.geode for r in routes]))