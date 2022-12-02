from core.workflow import Workflow


def main():
    workflow = Workflow(priority=1, tasks=[])
    workflow.start_async()
    workflow.wait_on_completion()


if __name__ == "__main__":
    main()
