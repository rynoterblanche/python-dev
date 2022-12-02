class Workflow:
    priority: int
    tasks: list

    def __init__(self, priority: int, tasks: list):
        self.priority = priority
        self.tasks = tasks

    def start_async(self):
        raise NotImplementedError

    def wait_on_completion(self):
        raise NotImplementedError
