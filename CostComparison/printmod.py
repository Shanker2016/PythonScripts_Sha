from datamod import *
from funcmod import *

def print_district_rate():
    print('\n')
    print('Morang District Rate')
    print('-'*30)
    
    print('Cement:'.ljust(15), 'Rs. '+str(cement_cost_rate_bag)+'/bag')
    print('Sand:'.ljust(15), 'Rs. '+str(sand_cost_rate)+'/m3')
    print('Aggregate:'.ljust(15), 'Rs. '+str(agg_cost_rate)+'/m3')

def print_concrete_det():
    print('\n')
    print('Concrete Details')
    print('-'*30)

    print('Type:'.ljust(15), concrete_type)
    print('Ratio:'.ljust(15), concrete_ratio)

def print_monument_det(vol, cement_vol, sand_vol, agg_vol, \
                       cement_cost, sand_cost, agg_cost,\
                       tot_cost, type_type = 'Type1'): 
    print('\n')
    if type_type == 'Type1':
        headline = 'Monument Type 1 Details'
        shape = 'Shape'.ljust(15) + 'Cube'
        dimension_line = 'Dimension:'.ljust(15) + str(length)+' m' + ' x ' + str(breadth)+' m' + \
                         ' x ' + str(height)+' m'
        survey_marker_line = 'Brass mark cost:'.ljust(20) + 'Rs. '+str(round(brass_mark_cost, 2))
    else:
        headline = 'Monument Type 2 Details'
        shape = 'Shape'.ljust(20) + 'Cylinder'
        dimension_line1 = 'Top Cylinder:'.ljust(20) + 'radius: ' + str(rad_top)+' m' + \
                         ' '*2 + 'height: ' + str(height_top)+' m'
        dimension_line2 = 'Bottom cylinder:'.ljust(20) + 'radius: ' + str(rad_bot)+' m' + \
                         ' '*2 + 'height: ' + str(height_bot)+' m'
        dimension_line = dimension_line1 + '\n' + \
                         dimension_line2
        survey_marker_line = 'Steel rod cost:'.ljust(20) + 'Rs. '+str(round(steel_rod_cost, 2))
                         
    

    print(headline)
    print('-'*30)

    print(shape)
    print(dimension_line) 
    print('Volume:'.ljust(20), str(round(vol,3))+' m3')
    
    print('Cement volume:'.ljust(20), str(round(cement_vol,3))+' kg')
    print('Sand volume:'.ljust(20), str(round(sand_vol,3))+' m3')
    print('Aggregate volume:'.ljust(20), str(round(agg_vol,3))+' m3')

    print('Cement cost:'.ljust(20), 'Rs. '+str(round(cement_cost, 2)))
    print('Sand cost:'.ljust(20), 'Rs. '+str(round(sand_cost, 2)))
    print('Aggregate cost:'.ljust(20), 'Rs. '+str(round(agg_cost, 2)))

    print(survey_marker_line)
    #print('Brass mark cost:'.ljust(20), 'Rs. '+str(round(brass_mark_cost, 2)))
    print('Total cost:'.ljust(20), 'Rs. '+str(round(tot_cost, 2)))
    

def print_monument_type1_det():
    vol = compute_volume_cube(length, breadth, height)
    cost_tup = compute_cost(vol, cement_vol_rate, sand_vol_rate, agg_vol_rate,\
                            cement_cost_rate, sand_cost_rate, agg_cost_rate)
    cement_vol, sand_vol, agg_vol = cost_tup[0], cost_tup[2], cost_tup[4]
    cement_cost, sand_cost, agg_cost = cost_tup[1], cost_tup[3], cost_tup[5]
    tot_cost = cement_cost + sand_cost + agg_cost + brass_mark_cost

    print_monument_det(vol, cement_vol, sand_vol, agg_vol, \
                       cement_cost, sand_cost, agg_cost,\
                       tot_cost, type_type = 'Type1')
    

def print_monument_type2_det():
    vol1 = compute_volume_cylinder(rad_top, height_top)
    vol2 = compute_volume_cylinder(rad_bot, height_bot)
    vol = vol1 + vol2
    cost_tup = compute_cost(vol, cement_vol_rate, sand_vol_rate, agg_vol_rate,\
                            cement_cost_rate, sand_cost_rate, agg_cost_rate)
    cement_vol, sand_vol, agg_vol = cost_tup[0], cost_tup[2], cost_tup[4]
    cement_cost, sand_cost, agg_cost = cost_tup[1], cost_tup[3], cost_tup[5]
    tot_cost = cement_cost + sand_cost + agg_cost + steel_rod_cost

    print_monument_det(vol, cement_vol, sand_vol, agg_vol, \
                       cement_cost, sand_cost, agg_cost,\
                       tot_cost, type_type = 'Type2')


def print_details():
    print_district_rate()
    print_concrete_det()
    print_monument_type1_det()
    print_monument_type2_det()
    

if __name__ == '__main__':
    print_details()
    






