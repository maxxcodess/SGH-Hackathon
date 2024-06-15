

//#include"signal1. h"   //signal 1 
#include"signal2.h"   //signal 2
//#include"signal3.h"   //signal 3   


void setup() 
{  
  Serial.begin(115200);

  lights_init();
  mqtt_init();

}

void loop() {
  // put your main code here, to run repeatedly:
//  test_millis();

    if (!client.connected())
  {
    reconnect();
  }
  client.loop();


}
