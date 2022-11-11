import unittest
import receiver

class receiver_test(unittest.TestCase):

   
  def test_read_data_from_console(self):
    self.assertTrue(receiver.read_data_from_console(50)!=0)
    
