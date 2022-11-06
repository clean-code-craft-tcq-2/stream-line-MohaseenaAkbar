import unittest
import sender
import sender_stub

class sender_test(unittest.TestCase):
  
  def test_CelsiustoFarenheit(self):
    self.assertEqual(sender.CelsiustoFarenheit(50),122.0,'0')
    self.assertEqual(sender.CelsiustoFarenheit(0),32.0,'0')
    self.assertEqual(sender.CelsiustoFarenheit(22),71.6,'0')
    
  def test_A2D_conversion(self):
    self.assertEqual(sender.A2D_conversion(0),0,'0')
    self.assertEqual(sender.A2D_conversion(0.1),20,'0')
    self.assertEqual(sender.A2D_conversion(2.5),512,'0')
    self.assertEqual(sender.A2D_conversion(4.9),1003,'0')
    
  def test_Sensor_reading_to_receiver(self):
    current,tempertaure=sender.Sensor_reading_to_receiver(2)
    self.assertTrue((len(current)+len(tempertaure))==4)
  
  def test_Preprocess(self):
    self.assertEqual(sender.Preprocess(0,0),(0,32.0),'0')
    self.assertEqual(sender.Preprocess(1.2,32),(246,89.6),'0')
    
  def test_print_sensor_readings(self):
    str= "No_of_readings  Current  Temperature"
    test_readings=[]
    self.assertTrue(sender.print_sensor_readings(test_readings,test_readings)==str[])
  
  def test_get_Temp_sensor_data(self):
    self.assertTrue(sender_stub.get_Temp_sensor_data()<=50)
    
  def test_get_Current_sensor_data(self):
    self.assertTrue(sender_stub.get_Current_sensor_data()<=5.0)
        
if __name__ == '__main__':
  unittest.main()
