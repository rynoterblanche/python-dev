import unittest

from demo_app.app import App


class TestApp(unittest.TestCase):

    def test_start_with_cloud_config(self):
        App('config.cloud').start()

    def test_start_with_onprem_config(self):
        App('config.onprem').start()
