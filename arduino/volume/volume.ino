void setup() {
  // put your setup code here, to run once:
  Serial.begin(500000);
}

void loop() {
  String packet = "^";
  packet.concat("vol:");
  packet.concat(String(analogRead(A0), DEC));
  packet.concat(";");
  Serial.println(packet);
}
