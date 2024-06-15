from mapmyClass import myVehicle    # Class
from firebase import firebase
import mapmy_2Functions_2
import time
import json
from publish_MQTT_2 import *

SignalHardware = ['signal1/relay1', 'signal2/relay1', 'signal3/relay1']
Signal_count = 0
Sig_Trigg_time = 5    # 5sec timer will be passed to ESP

running = True      # check if signals available 
_running = True     # check from app  : priority
defaultVariable = None
JourneyState = False
JourneyStarted = False
update_Status = True
FBS_Status = True
SignalsUpdated = False
condition1 = True

terminal_item_available = False
terminal_item = ''

response = {'EVID001': {'DESTIN': {'LAT': '23.501', 'LONG': '72.501'}, 'ORIGIN': {'LAT': '23.001', 'LONG': '72.001'}, 'PRIORITY': '1'}, 'EVID002': {'DESTIN': {'LAT': '23.881', 'LONG': '72.881'}, 'ORIGIN': {'LAT': '23.331', 'LONG': '72.331'}, 'PRIORITY': '3'}}
EVIDs = []
# id = ''
# priorty = 0
# presCord = []
# nextCord = []
# orign = []
# desti = []
 









################################### FIREBASE HANDLER ##################################

def Firebase_Handler():
    global response
    global EVIDs
    global FBS_Status
    
    FBS_Status = not FBS_Status

    try :
        fbs_app = firebase.FirebaseApplication('https://myserver-2b1a1-default-rtdb.firebaseio.com/', None)
        response = fbs_app.get('/NAV', None)
    except Exception as exception:
        print(exception)
        print("Internet Off (FBS)")
        
    
    EVIDs = list(response.keys())

    # OUTPUT
    # {'EVID001': {'DESTIN': {'LAT': '23.501', 'LONG': '72.501'}, 'ORIGIN': {'LAT': '23.001', 'LONG': '72.001'}, 'PRIORITY': '1'}, 'EVID002': {'DESTIN': {'LAT': '23.881', 'LONG': '72.881'}, 'ORIGIN': {'LAT': '23.331', 'LONG': '72.331'}, 'PRIORITY': '3'}}
    

    

    # fbs_app.delete('/NAV', EVIDs[3])

    # response = fbs_app.get('/NAV', None)
    # #### Exception_Handler() Function here
    # EVIDs = list(response.keys())
    
    return EVIDs, response

    
# Firebase_Handler()






###################################### ONLINE VEHICLE MANAGER ####################################
def online_vehicle_manager() :  
    global response
    global EVIDs  
    global defaultVariable
    global JourneyState
    global update_Status
    global _running

    # below call automatically writes global variables - EVIDs, response
    EVIDs, response = Firebase_Handler()
    
    # Firebase_Handler()

    # print(EVIDs)
    
    update_Status = not update_Status 
    
    # global GUI_flag
    
    
    # continously check for new variables and create new var if available
    if len(EVIDs) :  
        # defaultVariable = EVIDs[0]
        JourneyState = True
        globals_stored = set(globals())-mapmy_2Functions_2.not_my_data
        # print(list(globals_stored))
        for ele in EVIDs:
            if ele not in list(globals_stored)  and  ele == 'EVID003':
                # var = globals()[ele]

                # defaultVariable = var

                # print("\n\n\nNew Journey Started : ", end='')
                # print(var.ID, end="\n\n\n")

                #################  below line calls Firebase_Handler and updates global:[response, EVIDs] and returns:[id, origin, destin, presnt, priorty] 
                # READ DATA FROM FIREBASE
                id, orign, desti, prsnt, priorty = print_global_vars(ele)   
                #################  create an object of myVehicle Class
                globals()[id] = myVehicle(ID=id, origin=orign, destin=desti, presnt=prsnt, priority=priorty)
                var = globals()[id]
                print(f"\nNew variable created : {var.ID}")
                print()

                defaultVariable = var
                print(f"defaultVariable value : {defaultVariable.presnt}")
                print("\nNew Journey Started ")

        
        # break

    else :  
        JourneyState = False
        

    try : 
        #################  below line calls Firebase_Handler and updates global:[response, EVIDs] and returns:[id, origin, destin, presnt, priorty] 
        a, b, c, d, e = print_global_vars(defaultVariable.ID)
        defaultVariable.update_ClassVariables(b, c, d, e)
        print("Values sent to class")

    except Exception as exception:
        print(f"nothing updated from firebase  ->  Exception : {exception}")

        Terminal("online_vehicle_manager : FBS Error")
        pass

    
    
    try :
        if defaultVariable.priority == '1' :   
            print("\n\n Device manually stopped  Journey Paused")
            _running = False

            # Terminal("Pause command recieved from app")
        else :
            # print("\n\n Journey free running")
            _running = True
    except :
        pass

        # globals()[ele] = myVehicle(ID=ele, origin=[], destin=[], priority=3)
        # globals()[ele] = myVehicle(ID=id, origin=orign, destin=desti, presnt=prsnt, priority=priorty)
        # var = globals()[ele]
        # print(var.ID)
    # print(globals().keys())
    # update_variables

    return defaultVariable
    

# online_vehicle_manager()
# print("Hello MAXX")
 

# print(f"outside func defaultVariable value : {defaultVariable.presnt}")


'''global defaultVariable
    global JourneyState
    global EVIDs
    # global GUI_flag
    
    while (1) : 
        # EVIDs, response = Firebase_Handler()
        if len(EVIDs) :  
            defaultVariable = EVIDs[0]
            JourneyState = True
            break
        else :  
            JourneyState = False
            # print('No EVIDs available')
        time.sleep(0.1)
    
    # GUI_flag = True    # turn ON this flag only then program enters main GUI 

    print(f'{len(EVIDs)} EVIDs AVAILABLE !!!.. STARTING JOURNEY..')
    print(EVIDs)
    # print(len(EVIDs))
    # fb_app.delete('/users', '1')
    return EVIDs
'''
# check_available_vehicles()






def roundStr(val='') :
    return str(round(float(val), 5))






###################################### GLOBAL VAR PRINT ####################################

def print_global_vars(object_name = '') :
    global response
    global EVIDs
    EVIDs, response = Firebase_Handler()
    # id = ''
    priorty = 0
    orign = []
    desti = []
    prsnt = []

    for k, v in response.items() :
        # print(f"{k} = {v}")
        if k==object_name:
            for k2, v2 in v.items() :
                # print(f"{k2} = {v2}")    #to check items in dict
                if k2=='DESTIN' :
                    for k3, v3 in v2.items():
                        desti.append(v3)
                if k2=='ORIGIN' :
                    for k3, v3 in v2.items():
                        orign.append(v3)
                if k2=='PRESNT' :
                    for k3, v3 in v2.items():
                        prsnt.append(v3)
                if k2=='PRIORITY':
                    priorty = v2
                
    ''' Round off coordinates '''
    # orign = [round(orign[0]), round(orign[1])]
    orign = [roundStr(orign[0]), roundStr(orign[1])] 
    desti = [roundStr(desti[0]), roundStr(desti[1])] 
    prsnt = [roundStr(prsnt[0]), roundStr(prsnt[1])] 
    '''  '''
    print("Firebase Values :")
    print(f"ID: {object_name}   Orig: {orign}   Dest: {desti}   Pres: {prsnt}   Prir: {priorty}")

    return object_name, orign, desti, prsnt, priorty




 

#####################################  UPDATE OBJECT VARIABLES ####################################
#####  NOT USED
'''
def from_firebase_update_Object_variables(Object=None):
    global running
    while running:
        print("....parallel code running....")
        
        # online_vehicle_manager()

        global response
        global EVIDs
        EVIDs, response = Firebase_Handler()
        vehID = Object.ID
        priorty = 0
        orign = []
        desti = []
        prsnt = []

        for k, v in response.items() :
            # print(f"{k} = {v}")
            if k==vehID:
                for k2, v2 in v.items() :
                    # print(f"{k2} = {v2}")    #to check items in dict
                    if k2=='DESTIN' :
                        for k3, v3 in v2.items():
                            desti.append(v3)
                    if k2=='ORIGIN' :
                        for k3, v3 in v2.items():
                            orign.append(v3)
                    if k2=='PRESNT' :
                        for k3, v3 in v2.items():
                            prsnt.append(v3)
                    if k2=='PRIORITY':
                        priorty = v2

        # print("Got these values for firebase :")
        # print(f"veh_ID = {vehID}")
        # print(f"Origin = {orign}")
        # print(f"Destin = {desti}")
        # print(f"Presnt = {prsnt}")
        # print(f"Prirty = {priorty}")

        # Object.update_variables(origin=orign, destin=desti, presnt=prsnt, priority=priorty)
        Object.origin = orign
        Object.destin = desti
        Object.presnt = prsnt
        Object.priority = priorty
        
        time.sleep(0.2)

    return vehID, orign, desti, prsnt, priorty


'''




# send data to GUI Terminal
def Terminal(item = "") :
    global terminal_item_available
    global terminal_item

    terminal_item_available = True
    terminal_item = item




# online_vehicle_manager()
def Vehicle_Manager() :
    """  Mind that here we are reading data from Firebase so faster refreshing may lead to miss data (if code doesn't waits for recieve)  """
    while 1 :
        online_vehicle_manager()
        time.sleep(0.01)    

# print(f"outside func defaultVariable value : {defaultVariable.presnt}")







def start_journey_and_switch_signals_2(Object=None):
    global JourneyState
    global defaultVariable
    global SignalsUpdated
    global SignalHardware
    global Signal_count
    global Sig_Trigg_time
    global running
    global _running


    # sigSeq =  var.sigSeqJson
    signal_available = True    # if there are signals available in route
    crosedSig = False
    onRoute = True
    SignalJson = []
    safeDist = 500    # distance of signal to vehicle to make decision/ command lights

    while 1:
        if running  and  _running:
            
            if JourneyState and not SignalsUpdated:
                try :
                    # Below function automatically writes to myVehicle Class  ->  sigSeqJson, sigSeqList
                    SignalJson = defaultVariable.get_signals_in_route(btw_coords=True, _show=False)
                    # print("try 0000000000000000000000000000000000000000000  ok")
                except Exception as exception:
                    print(f"nothing updated  ->  Exception : {exception}")
                    time.sleep(2)
                    continue
                
            if len(SignalJson) :  
                SignalsUpdated = True
                signal_available = True
            else :
                signal_available = False

            print(f"len(SignalJson) : {len(SignalJson)}")
            print(f"signal_available : {signal_available}")

            
            # print(defaultVariable.sigSeqJson)
            # try :
            #     print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            #     print(defaultVariable.get_signals_in_route_func_was_run)
            # except :
            #     pass

            try :
                if defaultVariable.get_signals_in_route_func_was_run   and   len(SignalJson) == 0:
                    signal_available = False
                    print("signals not available~~~~~~~~~~~~~~~~~~~~~~~~~~")
                    time.sleep(2)
                    running = False

                    Terminal("Signals not available... pausing at start_journey.. func")
            except :            
                # time.sleep(2)
                # continue
                pass
            

            time.sleep(2)

            
            if signal_available :
                Terminal("signals available ..Starting Journey")
                # intransit = True
                ## Print all signal names
                print("\n\n    Signal Name              Coordinate")
                print("-----------------------------------------------")                
                for signal in SignalJson:
                    # print(signal)
                    name = signal[0]['name']
                    coord = signal[0]['end coordinates']
                    print("  {:<20}   {}".format(name, str(coord)))    
                print("\n\n\n")


                print("       Now Starting Journey ")
                print("-----------------------------------------------")  
                ## start loop for each signal
                for signal in SignalJson:
                    print("       Next Signal : ")
                    print("-----------------------------------------------") 
                    sig_name = signal[0]['name']
                    sig_coord = signal[0]['end coordinates']
                    print(f"Next Signal : {sig_name} \nCoordinates : {sig_coord}\n")
                    crosedSig = False
                    
                    defaultVariable.next_signal_name = sig_name

                    while not crosedSig  and  onRoute  :    # _running used for reading if manual pause was called
                        # to pause the code with mobile app
                        while not _running :   time.sleep(2)

                        # Find dist to next signal
                        # method 
                        #######################################################################################

                        sig_coord[0] = str(sig_coord[0])
                        sig_coord[1] = str(sig_coord[1])
                        
                        

                        #######################################################################################
                        print("\n\nInvokeing MMI url (short) for new values\n")                 
                        response = defaultVariable.ask_new_url(origin=defaultVariable.presnt, destin=sig_coord, steps=False)   
                        # response = {'routes': [{'legs': [{'steps': [], 'weight': 4087, 'distance': 3509.7, 'summary': '', 'duration': 811.2}], 'weight_name': 'routability', 'geometry': '_}|kCa}azLeEnCaAAcCbAqEgAq@RW]m@p@va@vUl@~A~p@cOhPuI`BP|FpClP|MbHoEdEvF', 'weight': 4087, 'distance': 3509.7, 'duration': 811.2}], 'code': 'Ok', 'Server': 'Adv-5400', 'waypoints': [{'hint': 'ZwStgYMErYHDAAAANQEAAF4JAAAAAAAAeiECQnkmTULwb8dDAAAAAMMAAAA1AQAAXgkAAAAAAACUAAAAxrpTBLxWYAEIvlMEyFhgAScAHwlQUDXe', 'distance': 103.296987, 'location': [72.596166, 23.090876], 'name': ''}, {'hint': 'p5KsgaqSrIEJAAAAlQEAAAAAAAAgCQAAdsXMP4OghkIAAAAASofCQwkAAACVAQAAAAAAACAJAACUAAAAq6pTBOgIYAGsq1MEiAdgAQAAzw5QUDXe', 'distance': 47.042135, 'location': [72.592043, 23.070952], 'name': ''}]}
                        # decode value of dist to signal from json recieved from above

                        output = json.dumps(response, indent=4)
                        output = json.loads(output)
                        # values = list(output.items())

                        try : 
                            distance = output['routes'][0]['legs'][0]['distance']
                            duration = output['routes'][0]['legs'][0]['duration']
                        except Exception as exce:
                            print(f"got Key Error : {exce}")
                            Terminal(f"got Key Error : {exce}")
                            pass

                        print(time.strftime("%H:%M:%S"))
                        print(f"distance = {distance} m")
                        print(f"duration = {round(duration/60, 2)} mins")
                        print()

                        
                        defaultVariable.exp_arrival_time = round(duration/60, 2)
                        defaultVariable.signal_distance = distance

                        if distance < safeDist :   #Command signal
                            # commnd_signal()
                            print("\n\n\t\t\tOhhh Snapp !! Signal Lights Changed\n\n")
                            # time.sleep(4)
                            crosedSig = True
                            Terminal(f"Signal {SignalHardware[Signal_count]} changed, time: {Sig_Trigg_time}")

                            
                            Send_MQTT_Message(SignalHardware[Signal_count], Sig_Trigg_time)
                            print(f"SignalHardware :  {SignalHardware[Signal_count]}")
                            print(f"Time :  {Sig_Trigg_time}")
                            

                            if Signal_count <= len(SignalHardware) :   # < 3:
                                Signal_count = Signal_count + 1
                            




                        time.sleep(2)      # wait for 2 sec before asking for new request
                        print("got out of while loop")
                    Terminal("ALL SIGNALS CROSSED  ")
                print("\n\n\t\t\t ALL SIGNALS CROSSED / REACHED DESTINATION !!")

                # global running
                running = False

        
        





######################################## SIGNAL COMMAND ####################################
# def commnd_signal(SigID='', dir='', time=20) :
    # time in seconds
    # density = 70  # %

    
    # return density















#############################################################################################
##  NOT USED FUNCTION
'''
def start_journey_and_switch_signals(Object=None):
    
    
    SignalJson = Object.get_signals_in_route(btw_coords=True, _show=False)

    # sigSeq =  var.sigSeqJson
    signal_available = True    # if there are signals available in route
    crosedSig = False
    onRoute = True
    safeDist = 500    # distance of signal to vehicle to make decision/ command lights

    print(Object.sigSeqJson)


    if len(SignalJson) == 0:
        signal_available = False


    if signal_available:
        # intransit = True
        ## Print all signal names
        print("\n\n    Signal Name              Coordinate")
        print("-----------------------------------------------")                
        for signal in SignalJson:
            # print(signal)
            name = signal[0]['name']
            coord = signal[0]['end coordinates']
            print("  {:<20}   {}".format(name, str(coord)))    
        print("\n\n\n")


        print("       Now Starting Journey ")
        print("-----------------------------------------------")  
        ## start loop for each signal
        for signal in SignalJson:
            print("       Next Signal : ")
            print("-----------------------------------------------") 
            sig_name = signal[0]['name']
            sig_coord = signal[0]['end coordinates']
            print(f"Next Signal : {sig_name} \nCoordinates : {sig_coord}\n")
            crosedSig = False
            
            Object.next_signal_name = sig_name

            while not crosedSig and onRoute :
                # Find dist to next signal
                # method 
                #######################################################################################

                sig_coord[0] = str(sig_coord[0])
                sig_coord[1] = str(sig_coord[1])
                
                

                # global EVIDs
                EVIDs, response = Firebase_Handler()
                vehID = var.ID
                priorty = 0
                orign = []
                desti = []
                prsnt = []

                for k, v in response.items() :
                    # print(f"{k} = {v}")
                    if k==vehID:
                        for k2, v2 in v.items() :
                            # print(f"{k2} = {v2}")    #to check items in dict
                            if k2=='DESTIN' :
                                for k3, v3 in v2.items():
                                    desti.append(v3)
                            if k2=='ORIGIN' :
                                for k3, v3 in v2.items():
                                    orign.append(v3)
                            if k2=='PRESNT' :
                                for k3, v3 in v2.items():
                                    prsnt.append(v3)
                            if k2=='PRIORITY':
                                priorty = v2

                print("Got these values for firebase :")
                print(f"veh_ID = {vehID}")
                print(f"Origin = {orign}")
                print(f"Destin = {desti}")
                print(f"Presnt = {prsnt}")
                print(f"Prirty = {priorty}")

                var.update_variables(origin=orign, destin=desti, presnt=prsnt, priority=priorty)
                
                

                #######################################################################################
                print("\n\nInvokeing MMI url (short) for new values\n")                 
                response = Object.ask_new_url(origin=Object.presnt, destin=sig_coord, steps=False)   
                # response = {'routes': [{'legs': [{'steps': [], 'weight': 4087, 'distance': 3509.7, 'summary': '', 'duration': 811.2}], 'weight_name': 'routability', 'geometry': '_}|kCa}azLeEnCaAAcCbAqEgAq@RW]m@p@va@vUl@~A~p@cOhPuI`BP|FpClP|MbHoEdEvF', 'weight': 4087, 'distance': 3509.7, 'duration': 811.2}], 'code': 'Ok', 'Server': 'Adv-5400', 'waypoints': [{'hint': 'ZwStgYMErYHDAAAANQEAAF4JAAAAAAAAeiECQnkmTULwb8dDAAAAAMMAAAA1AQAAXgkAAAAAAACUAAAAxrpTBLxWYAEIvlMEyFhgAScAHwlQUDXe', 'distance': 103.296987, 'location': [72.596166, 23.090876], 'name': ''}, {'hint': 'p5KsgaqSrIEJAAAAlQEAAAAAAAAgCQAAdsXMP4OghkIAAAAASofCQwkAAACVAQAAAAAAACAJAACUAAAAq6pTBOgIYAGsq1MEiAdgAQAAzw5QUDXe', 'distance': 47.042135, 'location': [72.592043, 23.070952], 'name': ''}]}
                # decode value of dist to signal from json recieved from above

                output = json.dumps(response, indent=4)
                output = json.loads(output)
                # values = list(output.items())

                distance = output['routes'][0]['legs'][0]['distance']
                duration = output['routes'][0]['legs'][0]['duration']
                
                print(time.strftime("%H:%M:%S"))
                print(f"distance = {distance} m")
                print(f"duration = {round(duration/60, 2)} mins")
                print()

                
                Object.exp_arrival_time = round(duration/60, 2)
                Object.signal_distance = distance

                if distance < safeDist :   #Command signal
                    # commnd_signal()
                    print("\n\n\t\t\tOhhh Snapp !! Signal Lights Changed\n\n")
                    # time.sleep(4)
                    crosedSig = True



                time.sleep(2)      # wait for 2 sec before asking for new request
            print("got out of while loop")

        print("\n\n\t\t\t ALL SIGNALS CROSSED / REACHED DESTINATION !!")

        global running
        running = False
  
'''
















