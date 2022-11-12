import unittest
import receiver
import receiver_stub

class receiver_test(unittest.TestCase):
   
  def test_read_data_from_console(self):
    self.assertTrue(len(receiver.read_data_from_console())==100)
      
  def test_Find_Min_Max(self):
    Readings=[2.5,8,10,50,49.9,50.1]
    Min_Value,Max_Value=receiver.Find_Min_Max(Readings)
    self.assertTrue(Min_Value==2.5)
    self.assertTrue(Max_Value==50.1)
   
  def test_Simple_Moving_Average(self):
    Readings=[2.5,8,10,50,49.9,50.1,12,65.5,98,16.8,19,0,22,23.5]
    self.assertEqual(receiver.Simple_Moving_Average(Readings),16.26)
   
  def test_Console_output(self):
    self.assertTrue(len(receiver_stub.Console_output)==100)
  
  def test_Generate_readings(self):
    self.assertEqual(len(receiver_stub.Generate_readings(10)),10)
   
if __name__ == '__main__':
  unittest.main()
    
