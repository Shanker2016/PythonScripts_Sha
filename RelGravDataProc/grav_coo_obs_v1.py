
fname = 'cg6_grav_surv_2024.dat'
stn_id_num = {}
stn_coord = {}
#dates = []

def gen_stnid_num():
    """
    docstring goes here
    """

    #stn_id_num = {}
    with open(fname, 'r') as fin:
        data = fin.readlines()
        n = 0
        for record in data[21:]:
            record1 = record.split()
            stnid = "G"+record1[0]
            if stnid not in stn_id_num:
                n = n + 1
                stn_id_num[stnid] = n

    #return stn_id_num

def gen_stn_coord():
    """
    docstring goes here
    """
    with open(fname, 'r') as fin:
        data = fin.readlines()

        for record in data[21:]:
            record = record.split()
            station = "G"+record[0]
            latgps, longps, elevgps = record[20], record[21], record[22]
            #print(station, latgps, longps, elevgps)

            if station not in stn_coord:
                stn_coord[station] = [stn_id_num[station], latgps, longps, elevgps, station]

def gen_stn_coord_file():
    """
    docstring goes here
    """
    with open('grav.coo', 'w') as fcoord:
        for station in stn_coord:
            stn_num = str(stn_coord[station][0])
            coord_lst = stn_coord[station][1:]
            fcoord.write("\t".join([stn_num] + coord_lst) + "\n")

def gen_loopwise_grav_obs():
    """
    docstring goes here
    """

    with open(fname, 'r') as fin:
        data = fin.readlines()

    dates = []
    for record in data[21:]:
        record = record.split()
        year, month, day = map(int, record[1].split("-"))
        date1 = f"{day:02}{month:02}{year-2000:02}"
        if date1 not in dates:
            dates.append(date1)

    with open('loopwise_grav_obs.dat', 'w') as floopobs:
        for daydate in dates:
            floopobs.write(f"\n# S-000000019030158 {daydate}\n")
            for record in data[21:]:
                record = record.split()
                
                station = "G"+record[0]
                corrgrav, stddev, rawgrav= record[3], record[5], record[7]
                latgps, longps, elevgps = record[20], record[21], record[22]
                
                date_parts = record[1].split("-")
                year, month, day = map(int, date_parts)
                formatted_date = f"{day:02}{month:02}{year-2000:02}"

                if daydate == formatted_date:
                    hh, mm, ss = map(int, record[2].split(":"))
                    formatted_time = f"{hh + mm/100:05.2f}"

                    totcorr = sum(map(float, [record[11], record[12], record[13],record[14]]))

                    grav_obs_rec = [station, str(stn_id_num[station]), formatted_date, formatted_time,\
                               rawgrav, stddev, f"{totcorr:.2f}", corrgrav,\
                               latgps, longps, elevgps]

                    floopobs.write("\t".join(grav_obs_rec) + "\n")

def gen_grav_obs():
    """
    docstring goes here
    """
    with open('loopwise_grav_obs_edited.dat') as fin, open('grav.obs', 'w') as fobs:
        for line in fin:
            record = line.split()
            if record:
                if record[0] == "#":
                    fobs.write(f"\n{' '.join(record[:3])}\n")
                else:
                    stn, date, time, rawgrav, stddev = record[0], record[2], record[3], \
                                                       record[4], record[5]
                    gravobs = [str(stn_id_num.get(stn, 'UNKNOWN')),date, time, rawgrav, stddev, stn]
                    fobs.write("\t".join(gravobs) + "\n")
                
        
def print_stn_id_num():
    for stn in stn_id_num:
        print(stn, stn_id_num[stn])

def print_stn_coord():
    for stn in stn_coord:
        print(stn, stn_coord[stn])


def run():
    gen_stnid_num()
    #print_stn_id_num()
    
    #gen_stn_coord()
    #print_stn_coord()

    #gen_stn_coord_file()

    #gen_loopwise_grav_obs()

    gen_grav_obs()


if __name__=='__main__':
    run()
