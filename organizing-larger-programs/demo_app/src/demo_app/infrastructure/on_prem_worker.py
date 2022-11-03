from demo_app.core.interfaces.worker import Worker


class OnPremWorker(Worker):
    def start(self):
        print("Started on-prem worker")
