import setuptools

setuptools.setup(
    name="demo_app_cloud_plugin",
    description="Demo application - cloud worker plugin",
    version="1.0.0",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    entry_points={
        'demo_app.worker_plugins': [
            'config.cloud = demo_app_cloud.cloud_worker'
        ]
    }
)
