import json
from math import sin, cos, sqrt, atan2, radians
import polyline
# from shapely.geometry import Point, Polygon, MultiPoint, MultiPolygon

not_my_data = set(globals())


# not required function
def swapCoords(x):
    out = []
    for iter in x:
        if isinstance(iter, list):
            out.append(swapCoords(iter))
        else:
            return [x[1], x[0]]
    return out  


def round_off(lst, deci=5):
    lst[0] = round(lst[0], deci)
    lst[1] = round(lst[1], deci)
    return lst



def round_off_string(lst, deci=5):
    lst[0] = round(float(lst[0]), deci)
    lst[1] = round(float(lst[1]), deci)

    lst[0] = str(lst[0])
    lst[1] = str(lst[1])
    return lst



def calc_distance(coord1, coord2) :
    R = 6373.0
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    calc_distance = R * c
    return round(calc_distance, 5)

    # print("Result:", calc_distance)
    # print("Should be:", 278.546, "km")


api_response = []
sig_response = []

'''  

f1 = open('Signal_Coords_1.json', encoding='UTF8')
sig_response = json.loads(f1.read())
f1.close()

f2 = open('mapmyIndia_1(steps)_Indented.json', encoding='UTF8')
# f2 = open('mapmyIndia_1(alternatives+steps).json', encoding='UTF8')
api_response = json.loads(f2.read())
f2.close()

'''  





def initialise_coord(api_response, show = False):
    global origin_coord, destin_coord, next_coord
    next_coord = [0, 0]
    origin_coord = swapCoords(api_response['waypoints'][0]['location'])
    destin_coord = swapCoords(api_response['waypoints'][1]['location'])
    if show:
        print(origin_coord)
        print(destin_coord)
        print(next_coord)
    return origin_coord, destin_coord

# initialise_coord(api_response)




## FIND DISTANCE OF A POINT FROM A LINE SEGMENT

# Python3 implementation of the approach
# from math import sqrt
 
# Function to return the minimum distance
# between a line segment AB and a point E
def minSegDistance(A, B, E) :
 
    # vector AB
    AB = [None, None]
    AB[0] = B[0] - A[0]
    AB[1] = B[1] - A[1]
 
    # vector BP
    BE = [None, None]
    BE[0] = E[0] - B[0]
    BE[1] = E[1] - B[1]
 
    # vector AP
    AE = [None, None]
    AE[0] = E[0] - A[0]
    AE[1] = E[1] - A[1]
 
    # Variables to store dot product
 
    # Calculating the dot product
    AB_BE = AB[0] * BE[0] + AB[1] * BE[1]
    AB_AE = AB[0] * AE[0] + AB[1] * AE[1]
 
    # Minimum distance from
    # point E to the line segment
    reqAns = 0
 
    # Case 1
    if (AB_BE > 0) :
 
        # Finding the magnitude
        y = E[1] - B[1]
        x = E[0] - B[0]
        reqAns = sqrt(x * x + y * y)
 
    # Case 2
    elif (AB_AE < 0) :
        y = E[1] - A[1]
        x = E[0] - A[0]
        reqAns = sqrt(x * x + y * y)
 
    # Case 3
    else:
 
        # Finding the perpendicular distance
        x1 = AB[0]
        y1 = AB[1]
        x2 = AE[0]
        y2 = AE[1]
        mod = sqrt(x1 * x1 + y1 * y1)
        if mod > 0:
            reqAns =  (round(abs((x1 * y2 - y1 * x2)/mod), 12))
        else :
            reqAns = 0
     
    return reqAns






## Signals in the JSON file extracted and returned   input:: Loaded JSON file from request/file (type <List>)
def SignalJSON_Initialise(sig_response = [], show=False) :
    for feature in sig_response['features']:
        feature['geometry']['coordinates'] = swapCoords(feature['geometry']['coordinates'])


    signals = []
    sig_names = []

    for feature in sig_response['features'] :
        if feature['geometry']['type'] == 'Point' :
            signals.append(round_off(feature['geometry']['coordinates'], 5))        #pass the decimal roundoff
            sig_names.append(feature['properties']['name'])

    #print all the Coordintates of the Signals //Uncomment for Testing
    if show :
        # print(signals)
        print("\nSignal names in the List :")
        print(sig_names)
        print()

    return signals, sig_names



## Coordinates of MayMy extracted and returned   input:: Loaded JSON file from request/file (type <List>)
def MapMyJSON_Initialise(api_response = [], show=False) :
    poly_lines = []
    # poly_list = []
    polyline_points = []

    for step in api_response["routes"][0]["legs"][0]["steps"] :
        p = step["geometry"]
        
        poly_lines.append(p)
        # print(p)
        poly = polyline.decode(p)
        # print(poly)
        for ele in poly:
            polyline_points.append(list(ele))
        
        # print()

    if show :
        print()
        print()
        print(polyline_points)

    return polyline_points




## Coordinates of MayMy extracted and returned   input:: Loaded JSON file from request/file (type <List>)
def MapMyJSON_InitialiseJSON(api_response = [], show=False) :
    poly_lines = []
    #poly_dict ={}
    poly_list = []
    polyline_points = []

    for step in api_response["routes"][0]["legs"][0]["steps"] :
        p = step["geometry"]
        
        temp_dict = {}
        temp_list =[]
        
        temp_dict['polyline'] = p
        temp_dict['distance'] = step['distance']
        temp_list.append(temp_dict)
        poly_list.append(temp_list)
        
        poly_lists = json.dumps(poly_list)
        
        poly_lines.append(p)
        # print(p)
        poly = polyline.decode(p)
        # print(poly)
        for ele in poly:
            polyline_points.append(list(ele))
        # print()

    if show :
        print()
        print()
        # print(polyline_points)
        print(poly_list)

    return polyline_points, poly_lists

'''

points, jsn = MapMyJSON_InitialiseJSON(api_response, True)
print  ()
print(json.loads(jsn)[0])
print(json.loads(jsn)[0][0]['distance'])

'''




## Join all polylines  --> Subfunction of MapMyJSON_Initialise   input::  Loaded JSON file from request/file (type <List>)
def polylines_Joined(api_response = [], show=False) :
    polyline_points = MapMyJSON_Initialise(api_response)
    polylines_joined = polyline.encode(polyline_points)

    if show :
        print(polylines_joined)
        print()
        print()

    return polylines_joined



'''  

## Find the Signals Sequence coming in the route of the  MapMyJSON input 
def Signal_Sequence_in_Route(sig_response=[], api_response = [], show=True) :
    signals, sig_names = SignalJSON_Initialise(sig_response)
    polyline_points = MapMyJSON_Initialise(api_response)

    sig_poly_gap = 5
    n = ""

    sig_dict = {}
    sig_list =[]    

    if show :
        print("  Distance         Sig Coordinates          Poly Coordinates             Sig Name")
        print("-------------------------------------------------------------------------------------")

    for c2 in polyline_points :
        for i in range(len(signals)) :
            c1 = signals[i]
            name = sig_names[i]
    
            km = distance(c1, c2)        
            if km < sig_poly_gap :
                if show :
                    print("{:10} {:>25} {:>25}      {:20}".format(km, str(c1), str(c2), name))              
                if(n != name) :
                    ## Make a JSON file and add features of all the signals   
                    # Temp Dict req to club different types of data types together               
                    temp_dict = {}
                    temp_dict['name'] = name
                    temp_dict['coordinates'] = c1    
                    # Temp List req to :  #1. Separate all dict (else all dict values will be updated togeter in above step as all will have dict named ['name'] & ['coord'])
                                          #2. so that we can read all elements one by one via one loop
                    # Why append Temp Dict req inside list, why not append as :  list(temp_dict)
                    # Bcz then the dict will lose it's values and only keys will be stored in resultant list
                    temp_list = []
                    temp_list.append(temp_dict)
                    # sig_list will be main bucket tthat holds all the above list[dicts]
                    sig_list.append((temp_list))
                    n = name
                break
    

    sig_dict['Signals'] = sig_list     # not very much req step, if I'm not clubbing any other type of data
    Signal_Sequence = json.dumps(sig_dict)
    # This JSON object will hold coordinates of only the first coordinate which comes in the path

    if show :
        print("\nSequence of signals :")
        print(Signal_Sequence)
        print()

    return Signal_Sequence
         
            


Signal_Sequence_in_Route(sig_response, api_response)



'''   









'''    '''

## Find the Signals Sequence coming in the route of the  MapMyJSON input 
def Signal_Sequences_in_Route(sig_response=sig_response, api_response = api_response, show=True, btw_coords = True) :
    signals, sig_names = SignalJSON_Initialise(sig_response)
    polyline_points = MapMyJSON_Initialise(api_response)

    sig_poly_gap = 5
    n = ""
    x = 0

    sig_dict = {}
    sig_list =[]    
    temp_sigs_list = []     
    # s_temp = signals [0]
    # s_temp = polyline_points[0]
    # print (s_temp)

    if show :
        print()
        print("   Distance        Sig Coordinates          Poly Coordinates             Sig Name")
        print("---------------------------------------------------------------------------------------")

    for pp in polyline_points :
    	
        if btw_coords :
        	'''temp_dict2 ={}
        	temp_list2 = []
        	temp_dict2['coords'] = pp
        	#temp_dict2['dist'] = distance (s_temp, pp)
        	# temp_list2.append(temp_dict2)
        	# s_temp = pp
        	# temp_sigs_list.append(temp_list2)  '''
        	temp_sigs_list.append(pp)
            	
        else :
            x = x +1
            temp_sigs_list = [x]
  
       
        for i in range(len(signals)):
            ss = signals[i]
            name = sig_names[i]
            
          
    
            km = calc_distance(ss, pp)        
            if km < sig_poly_gap :
                if show :
                    print("   {:<10}   {:<25} {:<25}  {}".format(km, str(ss), str(pp), name))              
                
                    # print("   {}      {}      {}      {:20}".format('', km, str(ss), str(pp), name))              
                if(n != name) :
                    ## Make a JSON file and add features of all the signals   
                    # Temp Dict req to club different types of data types together               
                    temp_dict = {}
                    temp_dict['name'] = name
                    if btw_coords : temp_sigs_list + [ss]
                    temp_dict['btw coordinates'] = temp_sigs_list 
                    # if btw_coords = true  => len(btw coordinates) = len(temp_sigs_list) + 1    bcz if btw_coords is true then we are adding [end coordinate], just to faciliate easy use of the resultant jsonfile, so that user need not to deserialise [end coordinates] key also
                    temp_dict['end coordinates'] = ss
                    # Temp List req to :  #1. Separate all dict (else all dict values will be updated togeter in above step as all will have dict named ['name'] & ['coord'])
                                          #2. so that we can read all elements one by one via one loop
                    # Why append Temp Dict req inside list, why not append as :  list(temp_dict)
                    # Bcz then the dict will lose it's values and only keys will be stored in resultant list
                    temp_list = []
                    temp_list.append(temp_dict)
                    # sig_list will be main bucket tthat holds all the above list[dicts]
                    sig_list.append((temp_list))
                    n = name
                    
                    temp_sigs_list = []
                    x = 0
                    
                break


    sig_dict['Signals'] = sig_list     # not very much req step, if I'm not clubbing any other type of data
    Signal_Sequence = json.dumps(sig_dict)
    # Signal_Sequence = json.dumps(sig_list)
    
    # This JSON object will hold coordinates of only the first coordinate which comes in the path

    if show :
        print("\nSequence of signals :")
        print(Signal_Sequence)
        print()

    return Signal_Sequence
    
    

# Signal_Sequences_in_Route()
    
'''    
j= json.loads (Signal_Sequences_in_Route(sig_response, api_response, False, True))
# print (j['Signals'][1])
    



for i in j ['Signals'] : 
	print (i)
	print ()
#	print () 

'''     




## function closest() used to find closest value from L1 list for L2 coordinate 
def dist(c1, c2):
	X = c1[0] - c2[0]
	Y = c1[1] - c2[1]
	
	return abs(sqrt (X*X + Y*Y))


def closest(L1, L2):
	return min(L1, key=lambda i : dist(i, L2))
	
# print(closest2(L1, L2))




'''

## Find the Signals Sequence coming in the route of the  MapMyJSON input 
def Signal_Sequencess_in_Route(sig_response = sig_response, api_response = api_response, show=False, show2=False, btw_coords = True) :
    signals, sig_names = SignalJSON_Initialise(sig_response)
    polyline_points = MapMyJSON_Initialise(api_response)

    sig_poly_gap = 5
    n = ""
    x = 0

    sig_dict = {}
    sig_list =[]    
    temp_sigs_list = []     
    # s_temp = signals [0]
    # s_temp = polyline_points[0]
    # print (s_temp)

    if show :
        print("  Distance         Sig Coordinates          Poly Coordinates             Sig Name")
        print("-------------------------------------------------------------------------------------")

    for pp in polyline_points :
    	
        if btw_coords :
        	temp_sigs_list.append(pp)
            	
        else :
            x = x +1
            temp_sigs_list = [x]
  
       
        for i in range(len(signals)):
            ss = signals[i]
            name = sig_names[i]
            
          
    
            km = calc_distance(ss, pp)        
            if km < sig_poly_gap :
                if show :
                    print("{:10} {:>25} {:>25}      {:20}".format(km, str(ss), str(pp), name))              
                if(n != name) :
                    ## Make a JSON file and add features of all the signals   
                    # Temp Dict req to club different types of data types together               
                    temp_dict = {}
                    temp_dict['name'] = name
                    temp_dict['btw coordinates'] = temp_sigs_list + [ss]
                    temp_dict['end coordinates'] = ss
                    # Temp List req to :  #1. Separate all dict (else all dict values will be updated together in above step as all will have dict named ['name'] & ['coord'])
                                          #2. so that we can read all elements one by one via one loop
                    # Why append Temp Dict req inside list, why not append as :  list(temp_dict)
                    # Bcz then the dict will lose it's values and only keys will be stored in resultant list
                    temp_list = []
                    temp_list.append(temp_dict)
                    # sig_list will be main bucket tthat holds all the above list[dicts]
                    sig_list.append((temp_list))
                    n = name
                    
                    temp_sigs_list = []
                    x = 0
                    
                break


    sig_dict['Signals'] = sig_list     # not very much req step, if I'm not clubbing any other type of data
    Signal_Sequence = json.dumps(sig_dict)
    # Signal_Sequence = json.dumps(sig_list)   ##Test done to eliminate the requirement of using the above lines but not fruitful bcz still then we need 2 for loops
    # This JSON object will hold coordinates of only the first coordinate which comes in the path

    if show2 :
        print("\nSequence of signals :")
        print(Signal_Sequence)
        print()

    return Signal_Sequence
    
'''
    






myCoordinates = [23.026453, 72.5819]
closestCoords = []


def findClosestDist(coordinate=myCoordinates, api_response=api_response, show=False) :
    CONSTANT_1 = 110824.1179097812
    geometry = api_response['routes'][0]['geometry']
    print(geometry)
    lst = polyline.decode(geometry)
    print(lst)
    lst = [list(ele) for ele in lst]
    print(lst)
    coord1, coord2 = lst[0], lst[1] #[lst[i] for i in (0, 1)]
    minDist = CONSTANT_1*minSegDistance(coord1, coord2, myCoordinates)
    # print(minDist)
    
    for coord in lst :
        coord1 = coord
        if show: print("{:20}        {:>20}".format(str(coord2), str(coord1)), end="       ")
        distance = minSegDistance(coord1, coord2, myCoordinates)
        if show: print("{:.12f}".format(round(distance, 12)), end="       ")
        distance = CONSTANT_1*minSegDistance(coord1, coord2, myCoordinates)
        if show: print("{:<20}".format(distance))          #CONSTANT_1 = 110824...  ,94.46222735*
        # coord2 = coord1

        if (distance < minDist) : 
            minDist = distance 
            closestCoords = [coord2, coord1]    

        coord2 = coord1

    if show:
        print()
        print(minDist)
        print(closestCoords)

    '''
    SignalSequence = json.loads(Signal_Sequencess_in_Route())
    closestDist = 99999999
    for signal in SignalSequence['Signals']:
        # print(signal)
        # for coord in signal[0]['btw coordinates']:
            # print(coord, end=", ")
        signal = signal[0]['btw coordinates']
        closerDist = closest(signal, closestCoords[0])
        if closerDist < closestDist : 
            closestDist = closerDist
        
        print(signal)
        if signal.count(closestCoords[0])>0: 
            index = signal.index(closestCoords[0])
            print(index)
            print()
        if signal.count(closestCoords[1])>0: 
            index = signal.index(closestCoords[1])
            print(index)
            print()
        '''
    
# [[23.02641, 72.58137], [23.02645, 72.5819]]

    # for poly_coord in sig_seq['Signals'] :
    #     for coord in poly_coord[0]['btw coordinates']:




# findClosestDist(0)










'''
### CONSTANT_1 : calcualtion method used :-


taking following coordinates :
Coordinate 1  = [23.026453, 72.5819]
Coordinate 2  = [23.0812, 72.59356]

1. find original distance from    https://gps-coordinates.org/distance-between-coordinates.php
2. find 2D distance     https://www.calculatorsoup.com/calculators/geometry-plane/distance-two-points.php

now divide the 2 values and what we have is CONSTANT_1

##ASSUMPTION : 
output of function, findClosestDist() used where,
Coordinate 1 = [23.026453, 72.5819]  ~=  *[23.02645, 72.5819]
as distance between [23.026453, 72.5819] & *[23.02645, 72.5819]  =  0.000003000000 
and distance between *[23.02645, 72.5819] & [23.0812, 72.59356]  =  0.055974901599  (~=  0.055975, from 2nd link)


(* mark used above for easier identification)

'''

'''
Chandkheda Circle      [23.10914, 72.58489]
[23.026453, 72.5819]    [23.10914, 72.58492]     9199.55999965
[23.10914, 72.58492]    [23.10914, 72.58489]     32983.267467061596



Visat Circle      [23.09821, 72.5883]
[23.10914, 72.58489]    [23.10915, 72.58479]     250044.03446353538
[23.10915, 72.58479]    [23.10915, 72.58479]     0.0
[23.10915, 72.58479]    [23.10922, 72.58477]     1053917.3342180685
[23.10922, 72.58477]    [23.10921, 72.58495]     603891.11684659
[23.10921, 72.58495]    [23.10913, 72.58497]     368622.36937728
[23.10913, 72.58497]     [23.1087, 72.58512]     394908.9536743206
[23.1087, 72.58512]     [23.10827, 72.58526]     3833953.8191868756
[23.10827, 72.58526]    [23.10763, 72.58546]     7439545.252993016
[23.10763, 72.58546]    [23.10715, 72.58562]     12795779.989654694
[23.10715, 72.58562]    [23.10667, 72.58578]     16842561.33137663
[23.10667, 72.58578]    [23.10629, 72.58589]     20889629.594597038
[23.10629, 72.58589]    [23.10563, 72.58609]     24050363.757275708
[23.10563, 72.58609]    [23.10497, 72.58629]     29564617.29102902
[23.10497, 72.58629]    [23.10432, 72.58649]     35079683.17147661
[23.10432, 72.58649]    [23.10364, 72.58671]     40519161.32690611
[23.10364, 72.58671]     [23.1029, 72.58695]     46236499.29032295
[23.1029, 72.58695]     [23.10237, 72.58713]     52459766.59811916
[23.10237, 72.58713]     [23.10177, 72.5873]     56937069.273315854
[23.10177, 72.5873]     [23.10129, 72.58745]     61922204.55203349
[23.10129, 72.58745]     [23.1009, 72.58756]     65944974.4213197
[23.1009, 72.58756]     [23.10056, 72.58767]     69184443.46008648
[23.10056, 72.58767]    [23.09999, 72.58786]     72043106.79858033
[23.09999, 72.58786]    [23.09939, 72.58806]     76849238.27794762
[23.09939, 72.58806]    [23.09878, 72.58825]     81908362.1674191
[23.09878, 72.58825]     [23.09821, 72.5883]     87019136.77817038



AMTS Building      [23.09015, 72.59063]
[23.09821, 72.5883]     [23.09858, 72.58832]     88713678.31187004
[23.09858, 72.58832]    [23.09841, 72.58837]     88713678.31187004
[23.09841, 72.58837]    [23.09841, 72.58837]     0.0
[23.09841, 72.58837]    [23.09839, 72.58841]     90130761.8741287
[23.09839, 72.58841]    [23.09838, 72.58844]     90381388.28480908
[23.09838, 72.58844]    [23.09835, 72.58847]     90531814.21479745
[23.09835, 72.58847]    [23.09833, 72.58849]     90834659.30387872
[23.09833, 72.58849]     [23.0983, 72.58851]     91036699.28015707
[23.0983, 72.58851]     [23.09824, 72.58852]     91314788.7527296
[23.09824, 72.58852]    [23.09821, 72.58852]     91795606.77319995
[23.09821, 72.58852]    [23.09817, 72.58851]     92023516.86005738
[23.09817, 72.58851]     [23.09814, 72.5885]     92302578.15876265
[23.09814, 72.5885]     [23.09811, 72.58848]     92505901.75914045
[23.09811, 72.58848]    [23.09808, 72.58845]     92684865.48462659
[23.09808, 72.58845]    [23.09808, 72.58845]     0.0
[23.09808, 72.58845]     [23.0977, 72.58857]     92840023.784359
[23.0977, 72.58857]     [23.09745, 72.58866]     96027833.99793716
[23.09745, 72.58866]    [23.09667, 72.58889]     98151985.8488338
[23.09667, 72.58889]    [23.09613, 72.58906]     104655700.99794997
[23.09613, 72.58906]    [23.09593, 72.58912]     109184479.07906446
[23.09593, 72.58912]    [23.09543, 72.58927]     110854620.27982758
[23.09543, 72.58927]    [23.09468, 72.58948]     115030002.24313483
[23.09468, 72.58948]     [23.09424, 72.5896]     121257000.56977737
[23.09424, 72.5896]     [23.09379, 72.58973]     124902660.10509966
[23.09379, 72.58973]    [23.09311, 72.58992]     128648720.95165868
[23.09311, 72.58992]     [23.0927, 72.59002]     134294177.54683906
[23.0927, 72.59002]     [23.09227, 72.59013]     137663606.4705167
[23.09227, 72.59013]    [23.09181, 72.59025]     141209820.1432851
[23.09181, 72.59025]    [23.09134, 72.59038]     145009150.06068802
[23.09134, 72.59038]    [23.09077, 72.59054]     148908595.73864684
[23.09077, 72.59054]    [23.09015, 72.59063]     153643292.5122358



Modi Circle      [23.08873, 72.59111]
[23.09379, 72.58973]    [23.09311, 72.58992]     128648720.95165868
[23.09311, 72.58992]     [23.0927, 72.59002]     134294177.54683906
[23.0927, 72.59002]     [23.09227, 72.59013]     137663606.4705167
[23.09227, 72.59013]    [23.09181, 72.59025]     141209820.1432851
[23.09181, 72.59025]    [23.09134, 72.59038]     145009150.06068802
[23.09134, 72.59038]    [23.09077, 72.59054]     148908595.73864684
[23.09077, 72.59054]    [23.09015, 72.59063]     153643292.5122358

'''