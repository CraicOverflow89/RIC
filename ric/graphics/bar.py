from riem.graphics import Graphics
from riem.library import Colour, Dimensions, Point

class OptionBar:

	def __init__(self, pos: Point, width: int):
		self.pos = pos
		self.size = Dimensions(width, 32)

	def render(self, gfx: Graphics):

		# TEMP RECT
		gfx.draw_rect(self.pos, self.size, Colour(59, 59, 60).to_hex(), True)