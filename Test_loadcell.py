#include "HX711.h"

const int LOADCELL_DOUT_PIN = 2;
const int LOADCELL_SCK_PIN = 3;

HX711 scale;


void setup() {
  Serial.begin(9600);
  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);
}

void loop() {
  if (scale.is_ready()){
    scale.set_scale(); // Changer le code après cette ligne là
    long reading = scale.get_units(40);
    Serial.println(reading);
    delay(100);
  }
  else{
    Serial.println("HX711 not found.");
  }
}