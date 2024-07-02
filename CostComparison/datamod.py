from math import pi

# info of district wage rate

cement_cost_rate_bag = 850 # Rs 850 per 1 bag (1 bag = 50kg)
cement_cost_rate = 850 / 50 # per kg
sand_cost_rate = 1150 # Rs 1150 per 1 m3
agg_cost_rate = 1390 # Rs 1390 per 1m3

# info concrete details
concrete_type = 'M20'
concrete_ratio = '1:1.5:3'
# 1 m3 volume requires 8 bags of cement, 0.41 m3 of sand, and 0.81 m3 of aggregate

# volume of each component per m3 volume
cement_vol_rate = 8 * 50 # 8 bags per 1 m3 and 50 kg per bag
sand_vol_rate = 0.41 # 0.41 m3 sand per 1 m3 volume
agg_vol_rate = 0.81  # 0.81 m3 agg per 1 m3 volume

# monument type 1 dimension
length, breadth, height = 0.6, 0.6, 0.6

# monument type 2 dimension
# top part has 2 ft dia and 1 ft depth
rad_top, height_top = 1 * 0.3048, 1 * 0.3048 # in meter units

# bottom part has 6 inch dia and 2 ft depth
rad_bot, height_bot =  3/12 * 0.3048, 2 * 0.3048 # in meter units

# brass mark cost details
brass_mark_cost = 500 # Rs 500 per brass mark (source: Narayan Subedi)

# steel rod cost details
# 4ft long steel rod
steel_rod_cost = 2000 # Rs 3000 per 10 ft steel rod + Rs 500 (leth and grinding cost) + Rs 500 (VAT etc)





