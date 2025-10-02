# write your code here
import math
def pizza(n_people, slices_per_pizza):
    pizza_needed = n_people/slices_per_pizza
    return math.ceil(pizza_needed)