from setuptools import setup, find_packages

setup(
    name="files-docker-compose",
    version="0.1",
    description="Meltano project files for docker-compose",
    packages=find_packages(),
    package_data={"bundle": ["docker-compose.yml"]},
)
