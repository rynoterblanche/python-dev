import setuptools


setuptools.setup(
    name="demo_app",
    description="Demo application - how to organise packages",
    version="1.0.0",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'}
)