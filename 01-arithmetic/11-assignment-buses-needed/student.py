# write your code here
import math
def buses_needed(people_count, bus_capacity):
    buses_requered = people_count/bus_capacity
    return math.ceil(buses_requered)