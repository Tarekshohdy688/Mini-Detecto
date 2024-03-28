#include <ros.h>
#include <std_msgs/Bool.h>
#include <Servo.h>

ros::NodeHandle nh;

Servo servoMotor;

void bananaOrangeCallback(const std_msgs::Bool& msg) {
  if (msg.data) {  // If true (orange)
    servoMotor.attach(9);
    servoMotor.write(-180);
    delay(200);
    servoMotor.detach();      
    delay(2000);

  } else {  // If false (banana)
    servoMotor.attach(9);
    servoMotor.write(180);
    delay(200);
    servoMotor.detach();
    delay(2000);

    }
}

ros::Subscriber<std_msgs::Bool> sub("banana_orange_topic", &bananaOrangeCallback);

void setup() {
  nh.initNode();
  nh.subscribe(sub);
  
  servoMotor.attach(9);
  delay(10);
}

void loop() {
  servoMotor.detach();
  nh.spinOnce();
  delay(10);
}
