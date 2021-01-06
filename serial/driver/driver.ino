
#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <ros.h>
//#include <std_msgs/Uint16.h>
#include <std_msgs/Empty.h>
#include <Servo.h>
Servo servox;
Servo servoy;


ros::NodeHandle nh;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(57600);
  ROS_setup();
  servo_setup();

}

void loop() {
  // put your main code here, to run repeatedly:

}
