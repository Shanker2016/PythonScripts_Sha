
import pandas as pd

# File paths
template_csv = '3a9efa22f6410ea4980f2f8fe59ea5ce.csv'
data_csv = 'AbsoluteGravityValue.csv'
add_csv = 'GravityStationLocalAddress.csv'
gwas_csv = 'AbsoluteGravityValue_gwas.csv'

# Read the template CSV file to get header
template_df = pd.read_csv(template_csv, nrows = 0) # Read only the header
header = template_df.columns.tolist()

# Create an empty DataFrame using the header
empty_df = pd.DataFrame(columns=header)

# Take absolute gravity value csv and local address csv and merge them
def merge_csv():
    df1 = pd.read_csv(data_csv)
    df1_sorted = df1.sort_values(by='StationID', ascending = True)
    
    df2 = pd.read_csv(add_csv)
    df2_sorted = df2.sort_values(by='StationId', ascending = True)

    merged_df = pd.merge(df1_sorted, df2_sorted, left_on = 'StationID', right_on = 'StationId')
    
    
    return merged_df

def populate_template_csv():

    data_df = merge_csv()

    column_mapping = {
        'StationID':'point_name',
        'ProvinceCode':'province',
        'DistrictCode':'district',
        'PalikaCode':'local_level',
        'Latitude(DD)':'tentative_lat_wgs',
        'Longitude(DD)':'tentative_lon_wgs',
        'EllipsoidalHeight(m)':'tentative_elev_wgs',
        'AbsoluteGravityValue(mgal)':'gravity_value',
        'StandardDeviation(mgal)':'n_seperation'
        }

    # Create a dictionary to store the data for the new DataFrame
    gwas_data = {col: [] for col in header}

    # Populate the data dic with corresponding columns from merged_df
    for col in column_mapping:
        if column_mapping[col] in header and col in data_df.columns:
            gwas_data[column_mapping[col]] = data_df[col].tolist()

    for col in header:
        if not gwas_data[col]:
            gwas_data[col] = [''] * len(data_df)

    
    gwas_data['grid_no'] = [value[:3] for value in gwas_data['point_name']]
    #gwas_data['point_no'] = [value[4:8] for value in gwas_data['point_name']]
    gwas_data['point_no'] = [int(value[4:6]) - 10 + 10000 for value in gwas_data['point_name']]
    gwas_data['sub_grid_no'] = [0] * len(data_df)
    gwas_data['data_type'] = ['GRP'] * len(data_df)
    gwas_data['order'] = ['sixth_order_point'] * len(data_df)
    
    

    pop_df = pd.DataFrame(gwas_data)

    pop_df.to_csv(gwas_csv, index = False)

def run():
    #merge_csv()
    populate_template_csv()

if __name__ == '__main__':
    run()
    


