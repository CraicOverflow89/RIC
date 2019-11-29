from graphics.bar import OptionBar
from riem.core import Application, State
from riem.graphics import Align, Graphics, ImageLoader
from riem.library import Colour, Point

class StateMain(State):

	def __init__(self, app: Application) -> None:
		super().__init__(app)
		self.bar = OptionBar(Point(0, 0), self.app.size.width)

	def render(self, gfx: Graphics) -> None:

		# Render Background
		gfx.draw_rect(Point(0, 0), self.app.get_dimensions(), Colour(36, 36, 36).to_hex(), True)

		# Render Bar
		self.bar.render(gfx)

		# Render Content
		#

		# Render Hint
		# ?

	def tick(self) -> None:
		pass