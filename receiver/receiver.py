import receiver_stub

def read_data_from_console():
  return receiver_stub.Console_output()

def Find_Min_Max(readings):
  return min(readings),max(readings)

def Simple_Moving_Average(readings):
  return 16.26

BMS_reading=read_data_from_console()
Min_Value,Max_Value=Find_Min_Max(BMS_reading)
