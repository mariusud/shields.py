import setuptools

setuptools.setup(
    name='shields',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
