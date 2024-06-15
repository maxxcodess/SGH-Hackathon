import time
import requests
from requests.exceptions import ConnectionError
from mapmy_2Functions_2 import *


###################################### CLASS ####################################

class myVehicle:

    #class variables
    ID = ""
    priority = 0
    nextCoord = []
    origin = []
    destin = []    
    presnt = []
    class_Status = True


    signal_distance = 0
    next_signal_name = ''
    exp_arrival_time = 0


    
    mapmyResponse = {}     # json data from origin to destin with steps
    signlResponse = {}     # json data from presCo to signal   no steps
    sigSeqJson = {}
    sigSeqList = []
    # sigSeqList = ['Ashram Circle, (23.0663, 72.58313)', 'RTO Circle, (23.06858, 72.5817)', 'Torrent Circle, (23.07345, 72.59201)', 'Modi Circle, (23.0867, 72.5917)', 'AMTS Building, (23.09015, 72.59063)']

    MMI_request_counter = 0

    Internet_Flag = True
    MMIKeyFlag = True
    SignalsAvailableOnRoute = False
    get_signals_in_route_func_was_run = False
    

    keyList =  [
                'fz1nncw4me3rmxyz82o6j1pvdi3n5t9j',     # Key 0
                'szk7s7qdvg6qve7912d7beoqifrdnucs',     # Key 1
                '7578206cf8965d28e56a6b43a7ef89ec',     # Key 2
                'a2e03f10b2aa67d9ffc07138b064c1ef',     # Key 3  yashwant
                'd4f4b79613a3baca4f08b60b2f15635a',     # Key 4  pratyush
                'ea868ef3b23d6f833e3c69cd16394321',     # Key 5     "
                '17ffec72d7beee9d1562385170710894'      # Key 6     "
                ]     
     

    currentKey = 0



    #init func
    def __init__(self, ID="", origin=[], destin=[], presnt=[], priority=0) :
        self.ID = ID
        self.origin = origin
        self.destin = destin
        self.presnt = presnt
        self.priority = priority

        # print(self.ID)
        # print(self.origin)
        # print(self.destin)
        # print(self.presnt)
        # print(self.priority)
        




    # https://apis.mapmyindia.com/advancedmaps/v1/fz1nncw4me3rmxyz82o6j1pvdi3n5t9j/route_adv/driving/72.58488960564135,23.10914206647773;72.57953524589539,23.022107639882453?alternatives=3&steps=false

    def ask_new_url(self, origin=[], destin=[], steps=False):
       # url variable store 
        # print(f"\nrecieved origin : {origin}")
        # print(f"recieved destin : {destin}\n")

        # keyList =  ['fz1nncw4me3rmxyz82o6j1pvdi3n5t9j',     # Key 0
        #             'szk7s7qdvg6qve7912d7beoqifrdnucs',     # Key 1
        #             '7578206cf8965d28e56a6b43a7ef89ec']     # Key 2

        # self.currentKey = 0

        response = ''
        
        Base_url = 'https://apis.mapmyindia.com/advancedmaps/v1/'
        # api_key = 'fz1nncw4me3rmxyz82o6j1pvdi3n5t9j'
        # api_key = 'szk7s7qdvg6qve7912d7beoqifrdnucs'
        # api_key = '7578206cf8965d28e56a6b43a7ef89ec'
        api_key = self.keyList[self.currentKey]
        resource1 = '/distance_matrix/driving/'
        resource2 = '/distance_matrix_eta/driving/'
        resource3 = '/distance_matrix_traffic/driving/'
        resource4 = '/route_adv/driving/'

        # coordinates = '72.58488960564135,23.10914206647773;72.57953524589539,23.022107639882453' + '?'
        coordinates = origin[1]+','+origin[0]+';'+destin[1]+','+destin[0]+'?'
        _steps = 'true' if steps==True else 'false'
        
        try:
            response = requests.get(Base_url + api_key + resource4 + coordinates + 'alternatives=3' +'&'+'steps='+_steps)
        # print(Base_url + api_key + resource4 + coordinates + 'alternatives=2')
        except ConnectionError:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Internet Off (MMI)")
            self.Internet_Flag = False
            # raise ConnectionError
        
        
        #### Exception Handler here     Check KeyError
        #######################################################################################
        ############# Exception Handler here   check if KeyError
        localvarJson = response.json()
        if 'error' in localvarJson.keys() :
            self.ChangeCurrentKey()
            pass



        # count how many times url was called
        self.MMI_request_counter += 1

        # assumption : if I'm asking steps in response then it is only for  origin to destin   else  it is only for  presCord to signal
        if steps:
            self.mapmyResponse = response.json()
            # print(f"ask_new_url()  self.mapmyResponse : \n{self.mapmyResponse}")
            return self.mapmyResponse
        else:
            self.signlResponse = response.json()
            # print(f"ask_new_url()  self.signalResponse : \n{self.signlResponse}")        
            return self.signlResponse
        
        





    
    def get_signals_in_route(self, steps=True, btw_coords=False, _show=False):
        f1 = open('Signal_Coords_1.json', encoding='UTF8')
        sig_response = json.loads(f1.read())
        f1.close()

        # below code calls saved Json file
        '''  
        f2 = open('mapmyIndia_1(alternatives+steps).json', encoding='UTF8')
        api_response = json.loads(f2.read())
        f2.close()
        '''  
        # below code calls MapMyIndia.com
        self.ask_new_url(origin=self.origin, destin=self.destin, steps=steps)    #automatically set value of mapmyResponse
        api_response = self.mapmyResponse
        print("\nask_new_url() json response Recieved from URL :")
        print(api_response)

     

        '''   '''

        sigSeq = Signal_Sequences_in_Route(sig_response=sig_response, api_response = api_response, show=_show, btw_coords = btw_coords)

        # deserialise segSeq to get list of signal coordinates
        output = json.loads(sigSeq)
        self.sigSeqJson = list(output.values())[0]    # output is itself a list in a list so to get the internal list i have palced [0]
        lenth = len(self.sigSeqJson)
        print(f"\nnumber of signals = {lenth} \n")
        self.get_signals_in_route_func_was_run = True
        print("get_signals_in_route_func_was_run   was called output : ")
        print(self.get_signals_in_route_func_was_run)

        for i in range(len(self.sigSeqJson)):
            # print(self.sigSeqJson[i][0]['name']+' '+str(tuple(self.sigSeqJson[i][0]['end coordinates'])))
            self.sigSeqList.append(str(self.sigSeqJson[i][0]['name'] + ', ' + str(tuple(self.sigSeqJson[i][0]['end coordinates']))))
            self.SignalsAvailableOnRoute = True

    
        # print(output)
        '''
        for signal in self.sigSeqJson:
            print(self.sigSeqList.append(signal))
            # output.append(signal[0]['end coordinates'])
            # output.append(signal[0]['name'])
        # print()
        # print(output)
        '''
        # sigSeq = local var (str) = stores output of  Signal_Sequences_in_Route()
        # output = local var (json)= stores json output of sigSeq (used just for display/print data)
        #        = class var (list)= stores actual list of all siganls with their details
        # ^ self.sigSeqJson

        return self.sigSeqJson





    def update_ClassVariables(self, origin=[], destin=[], presnt=[], priority=0) :
        self.class_Status = not self.class_Status
        self.origin = origin
        self.destin = destin
        self.presnt = presnt
        self.priority = priority

        # print("Object attributes updated : ")
        # print(f"veh_ID = {self.ID}")
        # print(f"Origin = {self.origin}")
        # print(f"Destin = {self.destin}")
        # print(f"Presnt = {self.presnt}")
        # print(f"Prirty = {self.priority}")








    ##################################  KEY EXCEPTION HANDLER  #########################################
    def ChangeCurrentKey(self) : 
            # if response["responsecode"] == '403':
        #     print(response["responsecode"] + response["error_code"])

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print(f"Key{self.currentKey} exhausted !!")
        if self.currentKey <= len(self.keyList) :  
            self.currentKey = self.currentKey + 1
            print(f"~~~~~~~~~~~~ new Key started : key {self.currentKey} ~~~~~~~~~~~~~~")
        self.MMIKeyFlag = False
        time.sleep(1)
        self.MMIKeyFlag = True
        # raise Exception("Key Exhausted")











# V = myVehicle(ID="EVID00x", origin=['27.5445', '72.5445'], destin=['27.6445', '72.6445'], presnt=['27.5445', '72.5445'], priority=0)
# # V.ask_new_url(steps=True)
# V.get_signals_in_route()







##################################### ONLINE VEHICLE MANAGER ####################################
'''
def online_vehicle_manager() :
    # global EVIDs
    EVIDs, response = Firebase_Handler()
    # print(EVIDs)
    i = 0

    for ele in EVIDs:
        # if ele not in globals():
        id, orign, desti, prsnt, priorty = print_global_vars(ele)
        i+=1
        print(f"new variable created : ", end= " ")
            # globals()[ele] = myVehicle(ID=ele, origin=[], destin=[], priority=3)
        globals()[id] = myVehicle(ID=id, origin=orign, destin=desti, presnt=prsnt, priority=priorty)
        var = globals()[id]
        print(var.ID)
        print()
    # print(globals().keys())
    
'''
# online_vehicle_manager()


'''
id, orign, desti, prsnt, priorty = print_global_vars("EVID003")
globals()[id] = myVehicle(ID=id, origin=orign, destin=desti, presnt=prsnt, priority=priorty)
var = globals()[id]
print(f"New variable created : {var.ID}")
print()
'''





# var.get_signals_in_route()

# var=myVehicle








# def start_journey_and_switch_signals(Object=None):
    
#     # check_available_vehicles()

#     SignalJson = Object.get_signals_in_route(btw_coords=True, _show=False)

#     # sigSeq =  var.sigSeqJson
#     signal_available = True    # if there are signals available in route
#     crosedSig = False
#     onRoute = True
#     safeDist = 500    # distance of signal to vehicle to make decision/ command lights

#     print(Object.sigSeqJson)


#     if len(SignalJson) == 0:
#         signal_available = False


#     if signal_available:
#         # intransit = True
#         ## Print all signal names
#         print("\n\n    Signal Name              Coordinate")
#         print("-----------------------------------------------")                
#         for signal in SignalJson:
#             # print(signal)
#             name = signal[0]['name']
#             coord = signal[0]['end coordinates']
#             print("  {:<20}   {}".format(name, str(coord)))    
#         print("\n\n\n")


#         print("       Now Starting Journey ")
#         print("-----------------------------------------------")  
#         ## start loop for each signal
#         for signal in SignalJson:
#             print("       Next Signal : ")
#             print("-----------------------------------------------") 
#             sig_name = signal[0]['name']
#             sig_coord = signal[0]['end coordinates']
#             print(f"Next Signal : {sig_name} \nCoordinates : {sig_coord}\n")
#             crosedSig = False
            
#             Object.next_signal_name = sig_name

#             while not crosedSig and onRoute :
#                 # Find dist to next signal
#                 # method 
#                 #######################################################################################

#                 sig_coord[0] = str(sig_coord[0])
#                 sig_coord[1] = str(sig_coord[1])
                
#                 '''
#                 # global EVIDs
#                 EVIDs, response = Firebase_Handler()
#                 vehID = var.ID
#                 priorty = 0
#                 orign = []
#                 desti = []
#                 prsnt = []

#                 for k, v in response.items() :
#                     # print(f"{k} = {v}")
#                     if k==vehID:
#                         for k2, v2 in v.items() :
#                             # print(f"{k2} = {v2}")    #to check items in dict
#                             if k2=='DESTIN' :
#                                 for k3, v3 in v2.items():
#                                     desti.append(v3)
#                             if k2=='ORIGIN' :
#                                 for k3, v3 in v2.items():
#                                     orign.append(v3)
#                             if k2=='PRESNT' :
#                                 for k3, v3 in v2.items():
#                                     prsnt.append(v3)
#                             if k2=='PRIORITY':
#                                 priorty = v2

#                 print("Got these values for firebase :")
#                 print(f"veh_ID = {vehID}")
#                 print(f"Origin = {orign}")
#                 print(f"Destin = {desti}")
#                 print(f"Presnt = {prsnt}")
#                 print(f"Prirty = {priorty}")

#                 var.update_variables(origin=orign, destin=desti, presnt=prsnt, priority=priorty)
#                 '''

#                 #######################################################################################
#                 print("\n\nInvokeing MMI url (short) for new values\n")                 
#                 response = Object.ask_new_url(origin=Object.presnt, destin=sig_coord, steps=False)   
#                 # response = {'routes': [{'legs': [{'steps': [], 'weight': 4087, 'distance': 3509.7, 'summary': '', 'duration': 811.2}], 'weight_name': 'routability', 'geometry': '_}|kCa}azLeEnCaAAcCbAqEgAq@RW]m@p@va@vUl@~A~p@cOhPuI`BP|FpClP|MbHoEdEvF', 'weight': 4087, 'distance': 3509.7, 'duration': 811.2}], 'code': 'Ok', 'Server': 'Adv-5400', 'waypoints': [{'hint': 'ZwStgYMErYHDAAAANQEAAF4JAAAAAAAAeiECQnkmTULwb8dDAAAAAMMAAAA1AQAAXgkAAAAAAACUAAAAxrpTBLxWYAEIvlMEyFhgAScAHwlQUDXe', 'distance': 103.296987, 'location': [72.596166, 23.090876], 'name': ''}, {'hint': 'p5KsgaqSrIEJAAAAlQEAAAAAAAAgCQAAdsXMP4OghkIAAAAASofCQwkAAACVAQAAAAAAACAJAACUAAAAq6pTBOgIYAGsq1MEiAdgAQAAzw5QUDXe', 'distance': 47.042135, 'location': [72.592043, 23.070952], 'name': ''}]}
#                 # decode value of dist to signal from json recieved from above

#                 output = json.dumps(response, indent=4)
#                 output = json.loads(output)
#                 # values = list(output.items())

#                 distance = output['routes'][0]['legs'][0]['distance']
#                 duration = output['routes'][0]['legs'][0]['duration']
                
#                 print(time.strftime("%H:%M:%S"))
#                 print(f"distance = {distance} m")
#                 print(f"duration = {round(duration/60, 2)} mins")
#                 print()

                
#                 Object.exp_arrival_time = round(duration/60, 2)
#                 Object.signal_distance = distance

#                 if distance < safeDist :   #Command signal
#                     # commnd_signal()
#                     print("\n\n\t\t\tOhhh Snapp !! Signal Lights Changed\n\n")
#                     # time.sleep(4)
#                     crosedSig = True



#                 time.sleep(2)      # wait for 2 sec before asking for new request
#             print("got out of while loop")

#         print("\n\n\t\t\t ALL SIGNALS CROSSED / REACHED DESTINATION !!")

#         global running
#         running = False
   

                  
# get_dist(var)





