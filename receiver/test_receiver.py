import unittest
import receiver

class receiver_test(unittest.TestCase):

   
  def test_read_data_from_console(self):
    self.assertTrue(receiver.len(read_data_from_console())==100)
      
  def test_Find_Min_Max(self):
    Min_val_expected = readings[0]
    Max_val_expected = readings[0]
    for val in readings:
        if val < Min_val_expected:
            Min_val_expected = val
    for value in readings:
        if value < Max_val_expected:
            Max_val_expected = value
    Min_Value_received,Max_Value_received=receiver.test_Find_Min_Max()
    self.assertTrue(Min_Value_received==Min_val_expected)
    self.assertTrue(Max_Value_received==Max_val_expected)
    
