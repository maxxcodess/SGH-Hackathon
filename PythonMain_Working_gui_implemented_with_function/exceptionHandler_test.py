from firebase import firebase
from requests.exceptions import ConnectionError

'''
try:
    print("Value of b = ", b)

except(ZeroDivisionError, NameError):
    print("Error Occurred and Handled")



try :
    fbs_app = firebase.FirebaseApplication('https://myserver-2b1a1-default-rtdb.firebaseio.com/', None)    
    print("FBS run")

except(ConnectionError) :
    print("Firebase Error")


try :
    response = fbs_app.get('/NAV', None)
    print("response run")

except ValueError as e:
    print("Firebase response Error")
    raise Exception('Invalid json: {}'.format(e)) from None
    
# except(ConnectionError) :
#     print("Firebase response Error")
'''


'''
# importing required module
import http.client as httplib


# function to check internet connectivity
def checkInternetHttplib(url="www.google.com", timeout=3):
	connection = httplib.HTTPConnection(url, timeout=timeout)
	try:
		# only header requested for fast operation
		connection.request("HEAD", "/")
		connection.close() # connection closed
		print("Internet On")
		return True
	except Exception as exep:
		print(f"Internet Off, ErrorCode : {exep}")
		return False


# checkInternetHttplib("www.geeksforgeeks.org", 3)
checkInternetHttplib()

'''





'''###  FUNC1 : INTERNET AVAILABLITY EXCEPTION HANDLER   '''
# importing requests module
import requests

try:
    # requesting URL
    fbs_app = firebase.FirebaseApplication('https://myserver-2b1a1-default-rtdb.firebaseio.com/', None) 
    response = fbs_app.get('/NAV', None)
    print("Internet On (FBS)")
  
    # catching exception
    # except (requests.ConnectionError, requests.Timeout) as exception:
except ConnectionError as e:
    print("Internet Off (FBS)")



Internet_Flag = True





Base_url = 'https://apis.mapmyindia.com/advancedmaps/v1/'
# api_key = 'fz1nncw4me3rmxyz82o6j1pvdi3n5t9j'
api_key = 'szk7s7qdvg6qve7912d7beoqifrdnucs'
resource1 = '/distance_matrix/driving/'
resource2 = '/distance_matrix_eta/driving/'
resource3 = '/distance_matrix_traffic/driving/'
resource4 = '/route_adv/driving/'

coordinates = '72.58488960564135,23.10914206647773;72.57953524589539,23.022107639882453' + '?'
# coordinates = origin[1]+','+origin[0]+';'+destin[1]+','+destin[0]+'?'
# _steps = 'true' if steps==True else 'false'

try:
    response = requests.get(Base_url + api_key + resource4 + coordinates + 'alternatives=3' +'&'+'steps='+'false')
    print("Internet On (MMI)")
# print(Base_url + api_key + resource4 + coordinates + 'alternatives=2')

# except Exception as exception:
#     print("Internet Off (MMI)")
#     Internet_Flag = False
except ConnectionError:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print("Internet Off (MMI)")
            # self.Internet_Flag = False
            raise ConnectionError

except  :
    if response["responsecode"] == '403':
        print(response["responsecode"] + response["error_code"])

    print ("keys exhausted")
    









# try :
#     mmi_resp = response.json()

# except Exception :
#     print("Error")

# response = requests.get(Base_url + api_key + resource4 + coordinates + 'alternatives=3' +'&'+'steps='+'false')

keyList = ['100', '200', '300', '400']
currentKey = 0

def MMI_KeyError_EXception_Handler() :
    global keyList
    global currentKey

    '''###  FUNC 2.1 : API REQUESTS AVAILABLITY EXCEPTION HANDLER   '''

    if Internet_Flag :
        # print("Internet is ON now checking if any key error is there ")
        mmi_resp = response.json()
        # print(mmi_resp)

        ### Exhausted keys should give this Error
        if 'responsecode' in mmi_resp.keys():
            print("API requests Exhausted")
            # print(f"Response Code : {mmi_resp['responsecode']}" +      
            #       f"Error Code : {mmi_resp['error_code']}")
            print(f"Response Code : {mmi_resp['responsecode']}", end='      ')        
            print(f"Error Code : {mmi_resp['error_code']}")
            print()
            print(f"prev key was : {keyList[currentKey]}")
            currentKey =+ 1
            print(f"next key was : {keyList[currentKey]}")
            

        else :
            print("API requests Available")

    
    

        '''###  FUNC 2.2 : API REQUESTS AVAILABLITY EXCEPTION HANDLER   ''' 
        # if mmi_resp["responsecode"] == '403':
        #     print(mmi_resp["error_code"] + '1')
        
        try :
            if mmi_resp["responsecode"] == '403':
                print(mmi_resp["responsecode"] + mmi_resp["error_code"])
            # else :
            #     print(mmi_resp + '2')

        except Exception as excep:
            print(f"Not Found key {excep}")
            print("API requests Available")
    


MMI_KeyError_EXception_Handler()