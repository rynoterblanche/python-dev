from demo_app.workers import cloud, on_prem

platform_map = {
    'config.onprem': on_prem.worker,
    'config.cloud': cloud.worker
}


class App:
    def __init__(self, config_file_name: str):
        self.worker = platform_map.get(config_file_name)

    def start(self):
        self.worker.start()
