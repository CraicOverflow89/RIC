from graphics.bar import OptionBar
from riem.core import Application, State
from riem.graphics import Align, Graphics, ImageLoader
from riem.library import Colour, Point

class StateMain(State):

	def __init__(self, app: Application) -> None:
		super().__init__(app)

		# Create Options
		self.bar_option = OptionBar(Point(0, 0), self.app.size.width)
		self.bar_option.add_element("Project")

		# Create Status
		self.bar_status = OptionBar(Point(0, self.app.size.height - 32), self.app.size.width)
		self.bar_status.add_element("Status Bar")

		# Define Colours
		self.colour_bkg = Colour(36, 36, 36).to_hex()

	def render(self, gfx: Graphics) -> None:

		# Render Background
		gfx.draw_rect(Point(0, 0), self.app.get_dimensions(), self.colour_bkg, True)

		# Render Options
		self.bar_option.render(gfx)

		# Render Content
		gfx.draw_text("Content Placeholder", Point(10, 40))

		# Render Status
		self.bar_status.render(gfx)

	def tick(self) -> None:
		pass