import sys

from demo_app.app import App

config = sys.argv[1]
app = App(config)
app.start()
