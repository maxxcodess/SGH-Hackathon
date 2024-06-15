#ifdef ESP8266
#include <ESP8266WiFi.h>
#elif defined(ESP32)
#include <WiFi.h>
#else
#error "Board not found"
#endif

#include <PubSubClient.h>


// Update these with values suitable for your network.
const char* ssid = "pratyush123";
const char* password =  "12345678";
const char* mqtt_server = "broker.emqx.io";
const int mqtt_port = 1883;


/*

{// Subscribed Topics   COMMENTED
//#define sub1 "device1/relay1"//-----------------1st topic---------------------  NOT IN DEMO CODE
//#define sub2 "device2/relay1"//-----------------2nd topic---------------------
//#define sub3 "device3/relay1"//-----------------3rd topic---------------------
//#define sub4 "device4/relay1"//-----------------4th topic---------------------

//SIGNAL 1
//#define sub1 "signal1/relay1"//-----------------1st topic---------------------
//#define sub2 "signal1/relay2"//-----------------2nd topic---------------------
//#define sub3 "signal1/relay3"//-----------------3rd topic---------------------
//#define sub4 "signal1/relay4"//-----------------4th topic---------------------

//SIGNAL 2
//#define sub1 "signal2/relay1"//-----------------1st topic---------------------
//#define sub2 "signal2/relay2"//-----------------2nd topic---------------------
//#define sub3 "signal2/relay3"//-----------------3rd topic---------------------
//#define sub4 "signal2/relay4"//-----------------4th topic---------------------

//SIGNAL 3
//#define sub1 "signal3/relay1"//-----------------1st topic---------------------
//#define sub2 "signal3/relay2"//-----------------2nd topic---------------------
//#define sub3 "signal3/relay3"//-----------------3rd topic---------------------
//#define sub4 "signal3/relay4"//-----------------4th topic---------------------
}

*/



WiFiClient espClient;
PubSubClient client(espClient);
unsigned long lastMsg = 0;
#define MSG_BUFFER_SIZE  (50)
char msg[MSG_BUFFER_SIZE];
int value = 0;




// Connecting to WiFi Router6

void setup_wifi()
{

  delay(10);
  // We start by connecting to a WiFi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  randomSeed(micros());

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}




// Connecting to MQTT broker

void reconnect()
{
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Create a random client ID
    String clientId = "ESP8266Client-";
    clientId += String(random(0xffff), HEX);
    // Attempt to connect
    if (client.connect(clientId.c_str())) {
      Serial.println("connected");
      // Once connected, publish an announcement...
      client.publish("outTopic", "hello world");
      // ... and resubscribe
      client.subscribe(sub1);
      client.subscribe(sub2);
      client.subscribe(sub3);
      client.subscribe(sub4);
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}






void MQTT_Callback_Event(char* topic, int _time)
{  
//  int _time;
  
  //compare message with subjects
  if (strstr(topic, sub1))
    {
      Serial.println();
      Serial.println("-------device1/relay1-------------");
  
//      digitalWrite(LED_BUILTIN, 0);
//      delay(1000 * _time);
//      digitalWrite(LED_BUILTIN, 1);

        allred();
        d1green();
  
    }
  else if (strstr(topic, sub2)) 
    {
      Serial.println();
      Serial.println("-------device1/relay2-------------");
  
//      digitalWrite(LED_BUILTIN, 0);
//      delay(1000 * _time);
//      digitalWrite(LED_BUILTIN, 1);

        allred();

        d2green();
    }
  else if (strstr(topic, sub3)) 
    {
      Serial.println();
      Serial.println("-------device1/relay3-------------");
  
//      digitalWrite(LED_BUILTIN, 0);
//      delay(1000 * _time);
//      digitalWrite(LED_BUILTIN, 1);

        allred();

        d3green();
    }
  else if (strstr(topic, sub4)) 
    {
      Serial.println();
      Serial.println("-------device1/relay4-------------");
  
//      digitalWrite(LED_BUILTIN, 0);
//      delay(1000 * _time);
//      digitalWrite(LED_BUILTIN, 1);

        allred();

        d4green();
    }
}





void callback(char* topic, byte* payload, unsigned int length)
{
  Serial.print("Message arrived [");
  Serial.print(topic);
  Serial.print("] ");

  String message;          //----------device1/relay1/6
  String timeString;
  int _time;

  //Extract time from message
  for (int i = 0; i < length; i++)
    {
      Serial.print((char)payload[i]);
      message = message + (char)payload[i];
    }
    Serial.print(message);

    timeString = message.substring(0);
    _time = timeString.toInt();

    Serial.print("  Time : ");
    Serial.println(_time);

  //do callback function
  MQTT_Callback_Event(topic, _time);
    
}
  




void mqtt_init()
{
  setup_wifi();

  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}
