const int measureSoilSensor = A0; // Analog pin
// const int measureSoilSensor = 10; //Digital pin 
 
void setup()
{
   Serial.begin(9600);
   //pinMode(measureSoilSensor, INPUT);
}
 
void loop()
{
   int humidity = analogRead(measureSoilSensor); //analog read
   //int humidity = digitalRead(measureSoilSensor); //digital read
   
   Serial.println(humidity);
   
   
   if (humidity == HIGH || humidity < 500){
       Serial.println("wet");  
   }
   else{
       Serial.println("NOT wet");
   }
   
   delay(1000);
}
