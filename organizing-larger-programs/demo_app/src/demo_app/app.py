import pkg_resources

worker_plugins = {
    entry_point.load()
    for entry_point
    in pkg_resources.iter_entry_points('demo_app.worker_plugins')
}

platform_map = {
    module.config: module.worker
    for module in worker_plugins
}


class App:
    def __init__(self, config_file_name: str):
        self.worker = platform_map.get(config_file_name)

    def start(self):
        self.worker.start()
