from riem.core import Application

class EditorApp(Application):

	def __init__(self):
		super().__init__("RIC Editor", "StateIntroRIC", "ric/states", debug = "+")

EditorApp()