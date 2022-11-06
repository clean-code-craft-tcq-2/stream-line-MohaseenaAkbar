import sender_stub

def temp_A2D_conversion(Analog_Volt):
  TempInVolt=((Analog_Volt*1023)/5) #10 bit ADC and 5V system
  TempInCelsius=TempInVolt*100
  return TempInCelsius

def CelsiustoFarenheit(TempInCelsius):
  return (((TempInCelsius*9)/5)+32)

def temp_preprocess(rew_Temp_data):
  Temp_celsius=temp_A2D_conversion(rew_Temp_data)
  Temp_Farenheit=CelsiustoFarenheit(Temp_celsius)
  return Temp_Farenheit
  
def Sensor_reading_to_receiver(No_of_readings):
  sensor_readings=[]
  for i in range(No_of_readings)
    rew_Temp_data=sender_stub.get_Temp_sensor_data()
    Temp_Output=temp_preprocess(rew_Temp_data)
    sensor_readings.append(Temp_Output)
    print(Temp_Output)
  return sensor_readings

if __name__ == '__main__':
  Sensor_reading_to_receiver(50)
  
