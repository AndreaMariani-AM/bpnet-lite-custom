from setuptools import setup

setup(
    name='bpnet-lite-custom',
    version='0.0.1',
    author='Andrea Mariani',
    author_email='andrea.mariani1@icloud.com',
    packages=['bpnetlite_custom'],
    scripts=['bpnet', 'chrombpnet'],
    url='https://github.com/AndreaMariani-AM/bpnet-lite-custom',
    license='LICENSE.txt',
    description='bpnet-lite-custom is a modification of the original bpnet-lite.',
    python_requires='>=3.9',
    install_requires=[
        "bpnet-lite >= 0.8.1"
    ],
)
