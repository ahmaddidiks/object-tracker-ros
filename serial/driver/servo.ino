void servo_setup(){
    
}

void servo_cb( const std_msgs::UInt16& sudut){
  servox.write(sudut.x); //set servo angle, should be from 0-180  
  servoy.write(sudut.y); //set servo angle, should be from 0-180  
  digitalWrite(13, HIGH-digitalRead(13));  //toggle led
}
