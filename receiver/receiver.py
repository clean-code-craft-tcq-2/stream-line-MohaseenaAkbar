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

def Processed_Receiver_output(BMS_reading):
  Min_Value,Max_Value=Find_Min_Max(BMS_reading)
  Moving_Average=Simple_Moving_Average(BMS_reading)
  return Min_Value,Max_Value,Moving_Average

def Display_receiver_output(Min_Val,Max_Val,Simp_Moving_Avg)
  print("Minimum value is:",Min_Val)
  print("Maximum value is:",Max_Val)
  print("Simple moving average value is:",Simp_Moving_Avg)
  
if __name__ == '__main__':
  BMS_reading=read_data_from_console()
  Min_Val,Max_Val,Simp_Moving_Avg=Processed_Receiver_output(BMS_reading)
  Display_receiver_output(Min_Val,Max_Val,Simp_Moving_Avg)
  
