// we will be using pin 13 inorder to put our led light.
// it will get on and off on one sec delay.
int led=13;
void setup(){
    pinMode(led,OUTPUT);
}
void loop(){
    digitalWrite(led,HIGH);
    delay(1000);
    digitalWrite(led,LOW);
    delay(1000);
}