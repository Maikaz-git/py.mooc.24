# tee ratkaisu tänne
# Write your solution here
import math

def read_data(data_txt:str)-> dict:
    with open(data_txt) as new_file:
        citys = {}
        lst = []
        for line in new_file:
            
            parts = line.split(';')
            
            if parts[0] == 'Longitude':
                continue       #Longitude;      Latitude;            FID;      name;        total_slot;   operative;id
            citys[parts[3]] = [float(parts[0]), float(parts[1]),int(parts[2]),int(parts[4]), parts[5], parts[6].replace("\n", "") ]
    return citys

def get_station_data(filename:str)->dict:
    result = {}
    dic = read_data(filename)
    
    for k,v in dic.items():
        result[k] = (v[0], v[1])
    
    return result

def distance(stations: dict, station1: str, station2: str):
    #stations = get_station_data(stations)
    longitude1 = 0
    latitude1 = 0
    longitude2 = 0
    latitude2 = 0

    for k,v in stations.items():
        if k == station1:
            longitude1 = v[0]
            latitude1 = v[1]
        if k == station2:
            longitude2 = v[0]
            latitude2 = v[1]

    x_km = (longitude1-longitude2) * 55.26
    y_km = (latitude1-latitude2) * 111.2

    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km








def greatest_distance(stations: dict)-> tuple:
    #stations = get_station_data(stations) 
    dis = 0
    location1 = ""
    location2 = ""
    for key,va in stations.items():
        for k,v in stations.items():
            if dis < distance(stations, key, k):
                dis = distance(stations, key, k)
                location1 = key
                location2 = k

    return (location1, location2, dis)


if __name__=="__main__":

    stations = get_station_data('stations2.csv')
    for k,v in stations.items():
        print(f"{k}:{v}")
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)

    stations = get_station_data('stations1.csv')
    res = greatest_distance(stations)
    print(res)

    # for k,v in res.items():
    #     print(f"{k}:{v}")
    # for k,v in citys.items():
    #     print(f"{k} : {v[0], v[1]}")
        


