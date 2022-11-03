from demo_app.infrastructure.on_prem_worker import OnPremWorker

config = 'config.onprem'
worker = OnPremWorker()

if __name__ == '__main__':
    worker.start()
