/*
 * Face Tracking Turret servo motor control
 * July 24th, 2019
 */
#include <Servo.h>
Servo turret;

const int servoPinNum = 9;
int angle, prevAngle, turretAng;
int input;


void setup() {
  Serial.begin(9600);
  turret.attach(servoPinNum);
  turret.write(90); //90 deg as an initial position
  delay(1000);
}

void pos() {
  if(prevAngle != angle) {
    prevAngle = angle;

    turretAng = map(angle, 0, 1000, 0, 180);
    turretAng = min(turretAng, 180);
    turretAng = max(turretAng, 0);

    turret.write(turretAng);
  }
}

void loop() {
  if(Serial.available() > 0) {
    if(input == 'X'){
      angle = Serial.parseInt();
      pos();
    }
  }

   while(Serial.available() > 0) {
    input = Serial.read();
  }
}
