import random

def Console_output():
  Temperature,Current = Generate_readings(50)
  while Current:
      temp=Current.pop()
      Temperature.append(temp)
  BMS_readings=Temperature
  return BMS_readings

def Generate_readings(No_of_readings):
  Temperature = (random.sample(range(0,50),No_of_readings))
  Current = []
  for i in range(No_of_readings):
      Current.append(round(random.uniform(0, 5),2))
  return Temperature,Current

