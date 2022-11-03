from demo_app.infrastructure.cloud_worker import CloudWorker

config = 'config.cloud'
worker = CloudWorker()

if __name__ == '__main__':
    worker.start()
