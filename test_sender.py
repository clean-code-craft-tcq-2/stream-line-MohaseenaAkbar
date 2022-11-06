import unittest
import sender
import sender_stub

class sender_test(unittest.Testcase):
  
  def test_CelsiustoFarenheit(self):
    self.assertEqual(sender.CelsiustoFarenheit(50),122.00)
    self.assertEqual(sender.CelsiustoFarenheit(0),32.00)
    self.assertEqual(sender.CelsiustoFarenheit(22),71.6)
    
if __name__ == '__main__':
  unittest.main()
