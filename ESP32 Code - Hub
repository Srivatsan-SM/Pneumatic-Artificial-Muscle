#include <WiFi.h>
#include <esp_now.h>

#define RXD2 16
#define TXD2 17

uint8_t pamNode[] = {0xAC, 0x67, 0xB2, 0xXX, 0xXX, 0xXX};  // ESP8266 MAC

void setup() {
  Serial.begin(115200);
  Serial2.begin(115200, SERIAL_8N1, RXD2, TXD2); // UART with Pi

  WiFi.mode(WIFI_STA);
  if (esp_now_init() != ESP_OK) {
    Serial.println("ESP-NOW init failed");
    return;
  }

  esp_now_add_peer(pamNode, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}

void loop() {
  if (Serial2.available()) {
    String command = Serial2.readStringUntil('\n');
    Serial.println("From Pi: " + command);

    if (command == "inflation") {
      esp_now_send(pamNode, (uint8_t *)"inflate", 8);
    } else if (command == "deflation") {
      esp_now_send(pamNode, (uint8_t *)"deflate", 8);
    } else {
      esp_now_send(pamNode, (uint8_t *)"idle", 4);
    }
  }
}
