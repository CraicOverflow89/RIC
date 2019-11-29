from riem.core import Application

class EditorApp(Application):

	def __init__(self):
		super().__init__("RIC Editor", "Main", "ric/states")

EditorApp()