import random

def Stub_to_generate_console_output():
  No_of_readings=50
  BMS_readings = []
  Temperature = (random.sample(range(0,50),No_of_readings))
  Current = []
  for i in range(No_of_readings):
      Current.append(round(random.uniform(0, 5),2))
  BMS_readings.append(Temperature)
  BMS_readings.append(Current)
  return BMS_readings
