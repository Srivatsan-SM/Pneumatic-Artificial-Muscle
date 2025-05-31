// ESP8266 - PAM Actuator Node
#include <ESP8266WiFi.h>
#include <espnow.h>

#define PAM_PWM D1
#define VALVE_CONTROL D2

uint8_t masterAddress[] = {0x24, 0x6F, 0x28, 0xXX, 0xXX, 0xXX}; // ESP32 MAC here

void setup() {
  Serial.begin(9600);
  pinMode(PAM_PWM, OUTPUT);
  pinMode(VALVE_CONTROL, OUTPUT);

  WiFi.mode(WIFI_STA);
  if (esp_now_init() != 0) {
    Serial.println("ESP-NOW Init Failed");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_SLAVE);
  esp_now_add_peer(masterAddress, ESP_NOW_ROLE_CONTROLLER, 1, NULL, 0);
  esp_now_register_recv_cb(onDataRecv);
}

void onDataRecv(uint8_t *mac, uint8_t *incomingData, uint8_t len) {
  String cmd = String((char*)incomingData);

  if (cmd == "inflate") {
    digitalWrite(VALVE_CONTROL, HIGH);
    analogWrite(PAM_PWM, 200);
  } else if (cmd == "deflate") {
    digitalWrite(VALVE_CONTROL, LOW);
    analogWrite(PAM_PWM, 0);
  } else {
    analogWrite(PAM_PWM, 0);
  }

  Serial.println("Received command: " + cmd);
}

void loop() {
  // Passive node, responds to ESP32 commands
}
