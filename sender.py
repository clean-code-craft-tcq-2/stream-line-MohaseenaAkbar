import sender_stub

def A2D_conversion(raw_data):
  return ((raw_data*5)/1024) #10 bit ADC and 5V system

def CelsiustoFarenheit(TempInCelsius):
  return (((TempInCelsius*9)/5)+32)

def Preprocess(raw_data,Temp_celsius):
  A2D_Out=A2D_conversion(raw_data)
  Temp_Farenheit=CelsiustoFarenheit(Temp_celsius)
  return A2D_Out,Temp_Farenheit
  
def Sensor_reading_to_receiver(No_of_readings):
  Sensor_readings=[]
  for i in range(No_of_readings)
    Temp_data=sender_stub.get_Temp_sensor_data()
    Output_Current=sender_stub.get_Current_sensor_data()
    Temp_Output=Preprocess(Output_Current,Temp_data)
    Sensor_readings.append(Output_CurrentTemp_Output)
    print(Output_Current,Temp_Output)
  return Sensor_readings

if __name__ == '__main__':
  Sensor_reading_to_receiver(50)
  
