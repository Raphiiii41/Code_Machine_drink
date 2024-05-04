#include "HX711.h"

// Déclaration des broches pour l'HX711
const int DOUT_PIN = 2;
const int CLK_PIN = 3;

HX711 scale;

void setup() {
  Serial.begin(9600);
  scale.begin(DOUT_PIN, CLK_PIN);

  // Effectuer la tare au début
  tare();
}

void loop() {
  if (scale.is_ready()) {
    float weight = (getWeight())/1000;
    
    if (weight > -10 && weight < 10) {
    weight = 0;
    Serial.print("Poids : ");
    Serial.print(weight, 2);
    Serial.println("g");
    delay(1000);
    }
    else{
    Serial.print("Poids : ");
    Serial.print(weight, 2);
    Serial.println("g");
    delay(1000);
    }
    
  } else {
    Serial.println("Erreur de communication avec HX711. Vérifiez les connexions.");
  }
}

void tare() {
  Serial.println("Calibrating. Please wait...");

  // Attendre que l'HX711 soit prêt
  while (!scale.is_ready()) {
    delay(100);
  }

  // Effectuer la tare
  scale.tare();

  Serial.println("Tare effectuée. Placez l'objet à peser.");
}

float getWeight() {
  // Lire le poids après la tare
  return scale.get_units(10);
}