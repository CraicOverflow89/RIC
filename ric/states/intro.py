from riem.core import Application, State
from riem.graphics import Align, Graphics, ImageLoader
from riem.library import Point

class StateIntroRIC(State):

	def __init__(self, app: Application) -> None:
		super().__init__(app)
		self.add_event(2000, lambda: self.app.state_update("StateMain"))

	def render(self, gfx: Graphics) -> None:

		# Render Logo
		gfx.draw_image(ImageLoader.load("logo"), Point(self.app.get_dimensions().width / 2, self.app.get_dimensions().height / 2), Align.CENTER)

	def tick(self) -> None:
		pass