import re
from dataclasses import dataclass

@dataclass
class Blueprint:
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost: tuple
    geode_robot_cost: tuple

@dataclass
class Resources:
    ore: int
    clay: int
    obsidian: int
    geode: int

@dataclass
class Robots:
    ore: int
    clay: int
    obsidian: int
    geode: int

@dataclass
class Route:
    robots: Robots
    resources: Resources
    def __hash__(self):
        return hash(repr(self))
    

def get_blueprints(real=False):
    if real:
        data_path = '../data.txt'
    else:    
        data_path = '../test_data.txt'
    with open(data_path, 'r') as f:
        data = f.read().splitlines()
    numbers = [
        list(map(
            int,
            re.findall(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", l)[0]
        )) for l in data
        ]
    blueprints = [Blueprint(x[1], x[2], (x[3],x[4]), (x[5],x[6])) for x in numbers]
    return blueprints

