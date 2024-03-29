import sender_stub

def A2D_conversion(raw_data):
  return round(((raw_data*1023)/5)) #10 bit ADC and 5V system

def CelsiustoFarenheit(TempInCelsius):
  return round(((TempInCelsius*1.8)+32),1)

def Preprocess(raw_data,Temp_celsius):
  A2D_Out=A2D_conversion(raw_data)
  Temp_Farenheit=CelsiustoFarenheit(Temp_celsius)
  return A2D_Out,Temp_Farenheit
  
def Sensor_reading_to_receiver(No_of_readings):
  Current_readings=[]
  Temperature_readings=[]
  for i in range(No_of_readings):
    Temp_data=sender_stub.get_Temp_sensor_data()
    Current_reading=sender_stub.get_Current_sensor_data()
    Current,Temperature=Preprocess(Current_reading,Temp_data)
    Current_readings.append(Current)
    Temperature_readings.append(Temperature)
  return Current_readings,Temperature_readings
 
def print_sensor_readings(Current_readings,Temperature_readings):
  print("No_of_readings  Current  Temperature")
  for i in range(len(Current_readings)):
    print(i+1,Current_readings[i], Temperature_readings[i],sep='\t\t')

if __name__ == '__main__':
  Current_readings,Temperature_readings=Sensor_reading_to_receiver(50)
  print_sensor_readings(Current_readings,Temperature_readings)
