from  unittest import TestCase
import sender
import sender_stub

class sender_test(unittest.Testcase):
  
  def test_temp_A2D_conversion(self):
    self.assertEqual(CelsiustoFarenheit(50),122.00)
    self.assertEqual(CelsiustoFarenheit(0),32.00)
    self.assertEqual(CelsiustoFarenheit(-20),-4.00)
    
if __name__ == '__main__':
  unittest.main()
