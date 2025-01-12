import math

def cal_distance(lat1,long1,lat2,long2):
    # approximate radius of earth in km
    R = 6373.0

    r = 200

    lat1 = math.radians(lat1)
    long1 = math.radians(long1)
    lat2 = math.radians(lat2)
    long2 = math.radians(long2)

    dlong = long2 - long1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlong / 2)**2
    distance = 2 * R * math.asin(a**0.5)

    print(distance)
    return distance <= r

print(cal_distance(23.8103, 90.4125, 26.3477, 88.6300)) 