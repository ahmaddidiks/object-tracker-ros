// Author   : Ahmad Didik Setiyadi
//Last Edit : 11 Jan 2021

#if (ARDUINO >= 100)
 #include <Arduino.h>
#else
 #include <WProgram.h>
#endif

#include <Servo.h> 
#include <ros.h>
#include <std_msgs/Int16.h>

ros::NodeHandle  nh;

Servo servoX;
Servo servoY;

unsigned int posX = 90;
unsigned int posY = 90;


void servo_x( const std_msgs::Int16& cmd_msg){
  posX += cmd_msg.data;
  servoX.write(posX); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}

void servo_y( const std_msgs::Int16& cmd_msg){
  posY += cmd_msg.data;
  servoY.write(posY); //set servo angle, should be from 0-180  
//  digitalWrite(13, HIGH-digitalRead(13));  //toggle led  
}


ros::Subscriber<std_msgs::Int16> sub1("servo_x", servo_x);
ros::Subscriber<std_msgs::Int16> sub2("servo_y", servo_y);

void setup(){
  pinMode(13, OUTPUT);

  nh.initNode();
  nh.subscribe(sub1);
  nh.subscribe(sub2);
  
  servoX.attach(9); //attach it to pin 9
  servoY.attach(10); //attach it to pin 10
  servoX.write(posX);
  servoY.write(posY);
}

void loop(){
  nh.spinOnce();
  
}
