from riem.core import Application
from riem.library import Dimensions
from screeninfo import get_monitors

class EditorApp(Application):

	def __init__(self):
		monitor = get_monitors()[0]
		super().__init__("RIC Editor", "StateIntroRIC", "ric/states", {}, None, Dimensions(monitor.width, monitor.height), 250, debug = "+")

EditorApp()