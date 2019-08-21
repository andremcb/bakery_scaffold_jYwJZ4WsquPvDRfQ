import unittest
import re
   
class TestSubmission(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestSubmission, self).__init__(*args, **kwargs)
        with open('order.html', 'r') as file_descriptor:
            self.dom_str = file_descriptor.read()

    def test_1(self):
        return True
        
    def test_cancelUrl(self):
        self.assertRegex(self.dom_str, r'cancelUrl: \'https:\/\/[a-z]*\.com/order\.html\'', 'No order.html redirect found on checkout cancel.')
    def test_successUrl(self):
        self.assertRegex(self.dom_str, r'successUrl: \'https:\/\/[a-z]*\.com/order_success\.html\'', 'No order_success.html redirect found on checkout success.')
    def test_redirect_to_checkout(self):
        self.assertNotEqual(self.dom_str, '.redirectToCheckout', 'No stripe redirect call found!')
    
            
if __name__ == '__main__':
    unittest.main()
