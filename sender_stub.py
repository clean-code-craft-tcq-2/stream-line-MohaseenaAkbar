import random

def get_Temp_sensor_data():
  return random.randint(-20,50) #rang is -20 to 50 degree celsius

def get_Current_sensor_data():
  return round(random.uniform(-2,2), 2) #current sensing sensor output voltage in range of -2 to 2V
