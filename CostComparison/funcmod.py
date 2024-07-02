from math import pi

def compute_volume_cube(l, b, h):
    vol = l * b* h
    return vol

def compute_volume_cylinder(r, h):
    vol = pi * r**2 * h
    return vol

def compute_cost(vol_tot, cement_vol_rate, sand_vol_rate, agg_vol_rate,\
                 cement_cost_rate, sand_cost_rate, agg_cost_rate):

    cement_vol = vol_tot * cement_vol_rate
    cement_cost = cement_vol * cement_cost_rate

    sand_vol = vol_tot * sand_vol_rate
    sand_cost = sand_vol * sand_cost_rate

    agg_vol = vol_tot * agg_vol_rate
    agg_cost = agg_vol * agg_cost_rate

    cost_tuple = (cement_vol, cement_cost, sand_vol, sand_cost, agg_vol, agg_cost)
    
    return cost_tuple







