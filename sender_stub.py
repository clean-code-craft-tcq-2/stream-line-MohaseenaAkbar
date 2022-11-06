import random

def get_Temp_sensor_data():
  return random.randint(0,50) #rang is -20 to 50 degree celsius

def get_Current_sensor_data():
  return round(random.uniform(0,10), 2) #current sensing sensor output voltage in range of 0 to 10V
