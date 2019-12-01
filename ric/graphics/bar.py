from riem.graphics import Align, Graphics
from riem.library import ArrayList, Colour, Dimensions, Point

class OptionBar:

	def __init__(self, pos: Point, width: int, height: int = 32, colour_bkg: Colour = Colour(59, 59, 60)):
		self.pos = pos
		self.size = Dimensions(width, height)
		self.colour_bkg = colour_bkg.to_hex()
		self.elements = ArrayList()

	def add_element(self, label: str): # -> OptionBarElement

		# Create Element
		new_element = OptionBarElement(self, label)

		# Append Element
		self.elements = self.elements.add(new_element)

		# Return Element
		return new_element

	def get_pos(self) -> Point:
		return self.pos

	def render(self, gfx: Graphics) -> None:

		# Render Background
		gfx.draw_rect(self.pos, self.size, self.colour_bkg, True)

		# Render Elements
		self.elements.each(lambda it, pos: it.render(gfx, pos))

class OptionBarElement:

	def __init__(self, option_bar: OptionBar, label: str) -> None:
		self.option_bar = option_bar
		self.label = label
		self.text = {
			"font": "Inconsolata 10",
			"colour": "black"
		}

	def render(self, gfx: Graphics, pos: int) -> None:
		gfx.draw_text(self.label, Point(10, self.option_bar.get_pos().y + 8), Align.LEFT, self.text["font"], self.text["colour"])