void setup() {
  // put your setup code here, to run once:
  Serial.begin(500000);
}

String formpacket(String name, String value)
{
  String packet = "";
  packet.concat(name);
  packet.concat(":");
  packet.concat(value);
  packet.concat(";");
  return packet;
}

void loop() {
  String packet = "^";
  packet.concat(formpacket("vol", String(analogRead(A0), DEC)));
  Serial.println(packet);
}
