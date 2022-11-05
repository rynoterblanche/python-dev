import unittest

from demo_app.infrastructure.on_prem_worker import OnPremWorker

from demo_app.infrastructure.cloud_worker import CloudWorker

from demo_app.app import App


class TestApp(unittest.TestCase):

    def test_start_with_cloud_config(self):
        app = App('config.cloud')
        app.start()

        self.assertTrue(isinstance(app.worker, CloudWorker))

    def test_start_with_onprem_config(self):
        app = App('config.onprem')
        app.start()

        self.assertTrue(isinstance(app.worker, OnPremWorker))