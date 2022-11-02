from demo_app.workers import cloud, on_prem

platform_map = {
    'config.onprem': cloud.worker,
    'config.cloud': on_prem.worker
}


class App:
    def __init__(self, config_file_name: str):
        self.worker = platform_map.get(config_file_name)

    def start(self):
        self.worker.start()
