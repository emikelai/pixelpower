import unittest

from allcolors import *

class AllCollorsTest(unittest.TestCase):

	def test_color_mode(self):
		self.assertEqual(color_mode(1), '1')
		self.assertEqual(color_mode(8), 'L')
		self.assertEqual(color_mode(24), 'RGB')

	#def test_return_num_pixel_values(self):







if __name__ == '__main__':
	unittest.main()