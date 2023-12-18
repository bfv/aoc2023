from typing import List
from dataclasses import dataclass

@dataclass
class Mapping:
    source: int
    dest: int
    len: int


class MappingChart:
    
    def __init__(self):
        self.name = ""
        self.mappings: List[Mapping] = []

    def get(self, frm: int) -> int:
        for m in self.mappings:
            if m.source <= frm and frm < m.source + m.len:
                return frm + (m.dest - m.source)
        return frm

    def map(self, source, dest, length):
        self.mappings.append(Mapping(source=source, dest=dest, len=length))

    def add(self, map: Mapping):
        self.mappings.append(map)

def main():

    lines = open(file="day05/input.txt", mode="r").read().split("\n")

    seeds: List[int] = []
    charts: List[MappingChart] = []
    chart: MappingChart
    for line in lines:
        if line.startswith("seeds:"):
            seeds = list(map(int, line.split(':')[1].split()))
        elif line == "":
            chart = MappingChart()
            charts.append(chart)
        elif line.endswith("map:"):
            chart.name = line.replace(" map:", "")
        else:
            vals = list(map(int, line.split()))
            chart.map(source=vals[1], dest=vals[0], length=vals[2])
    
    a = 2**128
    for seed in seeds:
        val = seed
        for c in charts:
            val = c.get(val)
        a = min(a, val)
    
    b = 2**128
    for i, _ in enumerate(seeds):
        if i % 2 == 0:
            for seed in range(seeds[i], seeds[i] + seeds[i+1]):
                val = seed
                for c in charts:
                    val = c.get(val)
                b = min(b, val)

    print(f"day 05; a: {a}, b: {b}")

main()