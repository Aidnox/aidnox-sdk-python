from setuptools import setup, find_packages

setup(
    name='aidnox-sdk',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='Muhammad Hamza',
    author_email='hamza.00dev1@gmail.com',
    description='Aidnox Python SDK for AI-based healthcare diagnostics.',
        long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Aidnox/aidnox-sdk-python",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    license='MIT',
) 