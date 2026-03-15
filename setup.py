from setuptools import setup, find_packages

setup(
    name="mlops_enterprise_frameworks",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "mlflow",
        "dvc",
        "docker",
        "kubernetes",
    ],
    author="Krishna Pandey",
    description="Enterprise-grade MLOps Lifecycle Frameworks",
)