import setuptools

setuptools.setup(
    name="demo_app_onprem_plugin",
    description="Demo application - on-prem worker plugin",
    version="1.0.0",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'demo_app.worker_plugins': [
            'config.onprem = demo_app_onprem.onprem_worker'
        ]
    }
)
