#include <NewPing.h> // Installer la librairie NewPing 

// Définir les pins et la distance maximale
#define TRIGGER_PIN 11
#define ECHO_PIN 12
#define MAX_DISTANCE 20

// Créer l'instance de la classe Newping "sonar"
NewPing sonar(TRIGGER_PIN, ECHO_PIN, MAX_DISTANCE);


void setup() {
  Serial.begin(9600);

}

void loop() {
  delay(50);
  unsigned int distance = sonar.ping_cm();
  Serial.print(distance);
  Serial.println("cm");

}