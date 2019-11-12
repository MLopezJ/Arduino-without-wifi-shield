const int measureSoilSensor = A0; //10;
 
void setup()
{
   Serial.begin(9600);
   //pinMode(measureSoilSensor, INPUT);
}
 
void loop()
{
   int humidity = analogRead(measureSoilSensor); //digitalRead(measureSoilSensor);
   Serial.println(humidity);
   
   //if (humidity == HIGH)
   /*
   if (humidity < 500)
   {
      Serial.println("wet");   
   }
   else{
    Serial.println("NOT wet");
   }
   */
   delay(1000);
}
