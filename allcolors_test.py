import unittest

from allcolors import *

class AllCollorsTest(unittest.TestCase):

	def test_rgb_int2tuple(self):
		self.assertEqual(rgb_int2tuple(63410),(0, 247, 178))
		self.assertEqual(rgb_int2tuple(15635330), (238,147,130))

	def test_color_mode(self):
		self.assertEqual(color_mode(1), '1')
		self.assertEqual(color_mode(8), 'L')
		self.assertEqual(color_mode(24), 'RGB')

	def test_return_num_pixel_values(self):
		self.assertEqual(return_num_pixel_values(1,'test_images/allcolors3x3.png'), [(5301312, 1)])
		#self.assertEqual(return_num_pixel_values(1,'test_images/1x1white.png'), [(255,1)])
		#self.assertEqual(return_num_pixel_values(1,'test_images/1x1black.png'), [(0,1)])
		#self.assertEqual(return_num_pixel_values(4,'test_images/allcolors1000x768.png'), [(4307214, 4), (10909426, 4), (9669749, 4), (14200181, 4)])
		#self.assertEqual(return_num_pixel_values(2,'test_images/allcolors1000x768.png'), [(4307214, 4), (10909426, 4)])
		self.assertEqual(return_num_pixel_values(4,'test_images/nes-classic-edition-controller.png'), [(0, 25270), (64, 7638), (65, 4898), (66, 4441)])

if __name__ == '__main__':
	unittest.main()