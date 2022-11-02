from demo_app.core.interfaces.worker import Worker


class CloudWorker(Worker):
    def start(self):
        print("Started cloud worker")
