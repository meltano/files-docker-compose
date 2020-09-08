from setuptools import setup, find_packages

setup(
    name="files-docker-compose",
    version="0.2",
    description="Meltano project files for Docker Compose",
    packages=find_packages(),
    package_data={
        "bundle": ["docker-compose.yml", "docker-compose.prod.yml", "README.md"]
    },
)
