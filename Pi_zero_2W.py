# pi_ai_predictor.py
import serial
import time
import smbus
import numpy as np
from tensorflow.lite.python.interpreter import Interpreter

# Serial to ESP32
ser = serial.Serial('/dev/ttyS0', 115200)

# Load TFLite model
interpreter = Interpreter(model_path="prosthetic_model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def read_mpu6050():
    # Replace with your I2C read code
    # Example: return [accX, accY, accZ, gyroX, gyroY, gyroZ]
    return [0.01, 0.2, 0.1, 0.1, 0.05, 0.02]  # Dummy for demo

def predict_gesture(features):
    input_data = np.array([features], dtype=np.float32)
    interpreter.set_tensor(input_details[0]['index'], input_data)
    interpreter.invoke()
    output_data = interpreter.get_tensor(output_details[0]['index'])
    return np.argmax(output_data)

while True:
    features = read_mpu6050()
    gesture = predict_gesture(features)

    if gesture == 0:
        ser.write(b"inflation\n")
    elif gesture == 1:
        ser.write(b"deflation\n")
    else:
        ser.write(b"idle\n")

    time.sleep(0.5)
