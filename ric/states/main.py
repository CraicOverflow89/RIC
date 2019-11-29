from riem.core import Application, State
from riem.graphics import Align, Graphics, ImageLoader
from riem.library import Point

class StateMain(State):

	def __init__(self, app: Application) -> None:
		super().__init__(app)

	def render(self, gfx: Graphics) -> None:

		# Render Test
		gfx.draw_text("Hello Word", Point(0, 0))

	def tick(self) -> None:
		pass