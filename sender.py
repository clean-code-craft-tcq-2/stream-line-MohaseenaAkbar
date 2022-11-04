import sender_stub

def temp_A2D_conversion(rew_Temp_data):
  TempInVolt=((rew_Temp_data/1024)*5)-0.5
  TempInCelsius=TempInVolt*100
  return TempInCelsius

def CelsiustoFarenheit(TempInCelsius):
  return (((TempInCelsius*9)/5)+32)

def temp_preprocess(rew_Temp_data):
  Temp_celsius=temp_A2D_conversion(rew_Temp_data)
  Temp_Farenheit=CelsiustoFarenheit(Temp_celsius)
  return temp_Farenheit
  
def Sensor_reading_to_receiver():
  rew_Temp_data=get_Temp_sensor_data()
  Temp_Output=temp_preprocess(rew_Temp_data)
  print(Temp_Output)
  
Sensor_reading_to_receiver()
  
