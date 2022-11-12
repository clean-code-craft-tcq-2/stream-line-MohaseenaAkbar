import receiver_stub

def read_data_from_console():
  return receiver_stub.Console_output()

def Find_Min_Max(readings):
  return min(readings),max(readings)

def Simple_Moving_Average(readings):
  window=readings[-5:]
  SMA=0
  for i in window:
      SMA+=i
  SMA/=5
  return round(SMA,2)

BMS_reading=read_data_from_console()
Min_Value,Max_Value=Find_Min_Max(BMS_reading)
Moving_Average=Simple_Moving_Average(BMS_reading)
