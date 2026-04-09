
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>


Adafruit_PWMServoDriver pca = Adafruit_PWMServoDriver();


#define SERVOMIN  100
#define SERVOMAX  500


void setup() {
 Serial.begin(115200);
 pca.begin();
 pca.setPWMFreq(50);
}


int angleToPulse(int angle) {
 return map(angle, 0, 180, SERVOMIN, SERVOMAX);
}


void loop() {
 if (Serial.available()) {
   String data = Serial.readStringUntil('\n');


   int ch, angle;
   sscanf(data.c_str(), "%d,%d", &ch, &angle);


   int pulse = angleToPulse(angle);
   pca.setPWM(ch, 0, pulse);
 }
}
