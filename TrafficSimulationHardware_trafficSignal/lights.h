int previousmillis = 0, _time, interval = 1500, n = 1;
//const byte greenLED = 12 ;
//const byte redLED = 8 ;



void lightsoff()
{
  digitalWrite(dir1red, 1);
  digitalWrite(dir1green, 1);
  digitalWrite(dir1blue, 1);
//  digitalWrite(dir1red, 1);
//  digitalWrite(dir1green, 1);
//  digitalWrite(dir1blue, 1);
//  digitalWrite(dir1red, 1);
//  digitalWrite(dir1green, 1);
//  digitalWrite(dir1blue, 1);

  digitalWrite(dir2red, 1);
  digitalWrite(dir2green, 1);
  digitalWrite(dir2blue, 1);
//  digitalWrite(dir2red, 1);
//  digitalWrite(dir2green, 1);
//  digitalWrite(dir2blue, 1);
//  digitalWrite(dir2red, 1);
//  digitalWrite(dir2green, 1);
//  digitalWrite(dir2blue, 1);

  digitalWrite(dir3red, 1);
  digitalWrite(dir3green, 1);
  digitalWrite(dir3blue, 1);
//  digitalWrite(dir3red, 1);
//  digitalWrite(dir3green, 1);
//  digitalWrite(dir3blue, 1);
//  digitalWrite(dir3red, 1);
//  digitalWrite(dir3green, 1);
//  digitalWrite(dir3blue, 1);
  digitalWrite(dir4red, 1);
  digitalWrite(dir4green, 1);
  digitalWrite(dir4blue, 1);
  //    Serial.println("lightsoff");
}





void lights_init() 
  {
      pinMode(dir1red, OUTPUT);//4 signals red light
      pinMode(dir2red, OUTPUT);
      pinMode(dir3red, OUTPUT);
      pinMode(dir4red, OUTPUT);
    
      pinMode(dir1green, OUTPUT);//4 signals green light
      pinMode(dir2green, OUTPUT);
      pinMode(dir3green, OUTPUT);
      pinMode(dir4green, OUTPUT);
    
      pinMode(dir1blue, OUTPUT);//4 signals blue light
      pinMode(dir2blue, OUTPUT);
      pinMode(dir3blue, OUTPUT);
      pinMode(dir4blue, OUTPUT);
      
      lightsoff();
  }

/*
////#define dir1red 21    //pinouts  of sample esp 32
////#define dir1green 19
////#define dir1blue 23
////
////#define dir2red 22
////#define dir2green 33
////#define dir2blue 32
////
////#define dir3red 27
////#define dir3green 26
////#define dir3blue 25
////
////#define dir4red 10
////#define dir4green 11
////#define dir4blue 12
////
////#define dir1red 18//---------signal3 NEW--------------------
////#define dir1green 19
////#define dir1blue 21
////
////#define dir2red 32
////#define dir2green 23
////#define dir2blue 22
////
////#define dir3red 5
////#define dir3green 16
////#define dir3blue 4
////
////#define dir4red 0
////#define dir4green 2
////#define dir4blue 15
//
//
////#define dir1red 12//---------signal2--------------------
////#define dir1green 14
////#define dir1blue 27
////
////#define dir2red 23
////#define dir2green 22
////#define dir2blue 21
////
////#define dir3red 5
////#define dir3green 18
////#define dir3blue 19
////
////#define dir4red 4
////#define dir4green 2
////#define dir4blue 15
////
////#define dir1red 12//-------------------signal 1-----------
////#define dir1green 2
////#define dir1blue 15
////
////#define dir2red 32
////#define dir2green 33
////#define dir2blue 25
////
////#define dir3red 22
////#define dir3green 21
////#define dir3blue 219
////
////#define dir4red 4
////#define dir4green 5
////#define dir4blue 16
//
//
////String message;
////inline void d1red()
////{
////  digitalWrite(dir1red, 1);
////  digitalWrite(dir1green, 0);
////  digitalWrite(dir1blue, 0);
////}
////inline void d1green()
////{
////  digitalWrite(dir1red, 0);
////  digitalWrite(dir1green, 1);
////  digitalWrite(dir1blue, 0);
////}
////
////inline void d1blue()
////{
////  digitalWrite(dir1red, 0);
////  digitalWrite(dir1green, 0);
////  digitalWrite(dir1blue, 1);
////}
////
////
////inline void d2red()
////{
////  digitalWrite(dir2red, 1);
////  digitalWrite(dir2green, 0);
////  digitalWrite(dir2blue, 0);
////}
////inline void d2green()
////{
////  digitalWrite(dir2red, 0);
////  digitalWrite(dir2green, 1);
////  digitalWrite(dir2blue, 0);
////}
////
////inline void d2blue()
////{
////  digitalWrite(dir2red, 0);
////  digitalWrite(dir2green, 0);
////  digitalWrite(dir2blue, 1);
////}
////
////
////inline void d3red()
////{
////  digitalWrite(dir3red, 1);
////  digitalWrite(dir3green, 0);
////  digitalWrite(dir3blue, 0);
////}
////inline void d3green()
////{
////  digitalWrite(dir3red, 0);
////  digitalWrite(dir3green, 1);
////  digitalWrite(dir3blue, 0);
////}
////
////inline void d3blue()
////{
////  digitalWrite(dir3red, 0);
////  digitalWrite(dir3green, 0);
////  digitalWrite(dir3blue, 1);
////}
////
////
////
////inline void d4red()
////{
////  digitalWrite(dir4red, 1);
////  digitalWrite(dir4green, 0);
////  digitalWrite(dir4blue, 0);
////}
////inline void d4green()
////{
////  digitalWrite(dir4red, 0);
////  digitalWrite(dir4green, 1);
////  digitalWrite(dir4blue, 0);
////}
////
////inline void d4blue()
////{
////  digitalWrite(dir4red, 0);
////  digitalWrite(dir4green, 0);
////  digitalWrite(dir4blue, 1);
////}
*/


inline void d1red()
{
  digitalWrite(dir1red, 0);
  digitalWrite(dir1green, 1);
  digitalWrite(dir1blue, 1);
}
inline void d1blue()
{
  digitalWrite(dir1red, 1);
  digitalWrite(dir1green, 1);
  digitalWrite(dir1blue, 0);
}
inline void d1green()
{
//    d1blue();
//    delay(interval / 4);
  digitalWrite(dir1red, 1);
  digitalWrite(dir1green, 0);
  digitalWrite(dir1blue, 1);
}



inline void d2red()
{
  digitalWrite(dir2red, 0);
  digitalWrite(dir2green, 1);
  digitalWrite(dir2blue, 1);
}
inline void d2blue()
{
  digitalWrite(dir2red, 1);
  digitalWrite(dir2green, 1);
  digitalWrite(dir2blue, 0);
}
inline void d2green()
{
  //  unsigned long currentmillis = millis();
  //  if (currentmillis - previousmillis > 500)
  //  {
  //    previousmillis = currentmillis;
  //    d1blue();
  //  }
//  d2blue();
//  delay(interval / 4);
  digitalWrite(dir2red, 1);
  digitalWrite(dir2green, 0);
  digitalWrite(dir2blue, 1);
}



inline void d3red()
{
  digitalWrite(dir3red, 0);
  digitalWrite(dir3green, 1);
  digitalWrite(dir3blue, 1);
}

inline void d3blue()
{
  digitalWrite(dir3red, 1);
  digitalWrite(dir3green, 1);
  digitalWrite(dir3blue, 0);
}

inline void d3green()
{
//  d3blue();
//  delay(interval / 4);
  digitalWrite(dir3red, 1);
  digitalWrite(dir3green, 0);
  digitalWrite(dir3blue, 1);
}

inline void d4red()
{
  digitalWrite(dir4red, 0);
  digitalWrite(dir4green, 1);
  digitalWrite(dir4blue, 1);
}
inline void d4blue()
{
  digitalWrite(dir4red, 1);
  digitalWrite(dir4green, 1);
  digitalWrite(dir4blue, 0);
}
inline void d4green()
{
//  d4blue();
//  delay(interval / 4);
  digitalWrite(dir4red, 1);
  digitalWrite(dir4green, 0);
  digitalWrite(dir4blue, 1);
}



inline void alert()    //yellow light
{
  digitalWrite(dir1red, 1);
  digitalWrite(dir1green, 1);
  digitalWrite(dir1blue, 0);

  digitalWrite(dir2red, 1);
  digitalWrite(dir2green, 1);
  digitalWrite(dir2blue, 0);

  digitalWrite(dir3red, 1);
  digitalWrite(dir3green, 1);
  digitalWrite(dir3blue, 0);

  digitalWrite(dir4red, 1);
  digitalWrite(dir4green, 1);
  digitalWrite(dir4blue, 0);
}


inline void allred() 
{
    d1red();
    d2red();
    d3red();
    d4red();
}


/*  void pattern()
//  {
//    d1green();
//    d2red();
//    d3red();
//    d4red();
//    delay(1000);
//    d1red();
//    d2green();
//    d3red();
//    d4red();
//    delay(1000);
//    d1red();
//    d2red();
//    d3green();
//    d4red();
//    delay(1000);
//    d1red();
//    d2red();
//    d3red();
//    d4green();
//    delay(1000);
//    Serial.println("pattern");
//  }  */



void test_millis()
{
  //    Serial.println("test_millis");
  unsigned long currentmillis = millis();
  if (currentmillis - previousmillis > interval)
  {
    previousmillis = currentmillis;
    if (n == 1)
    {
      d1green();
      d2red();
      d3red();
      d4red();
      Serial.println("n==1");
    }
    if (n == 2)
    {
      d1red();
      d2green();
      d3red();
      d4red();
      Serial.println("n==2");
    }
    if (n == 3)
    {
      d1red();
      d2red();
      d3green();
      d4red();
      Serial.println("n==3");
    }
    if (n == 4)
    {
      d1red();
      d2red();
      d3red();
      d4green();
      n = 0;
      Serial.println("n==4");
    }
    n++;
  }
}

void time_millis()
{
  unsigned long previousmillis = millis();
  for (int i = 0; i <= _time; i++)
  {
    unsigned long currentmillis = millis();
    if (currentmillis - previousmillis > 1000)
    {
      previousmillis = currentmillis;
      Serial.print(".");
      Serial.print(previousmillis);
    }
  }
  Serial.println(_time);
}


void Time()
{
  for (int i = 0; i <= _time; i++)
  {
    delay(1000);
    Serial.print(".");

  }
  Serial.println(_time);
}
