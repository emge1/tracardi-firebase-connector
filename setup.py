from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='tracardi-firebase-connector',
    version='0.1.0',
    description='This plugin connects to firebase.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Marcin Gaca',
    author_email='emygeq@gmail.com',
    packages=['tracardi_firebase_connector'],
    install_requires=[
        'tracardi_plugin_sdk',
        'pydantic',
        'tracardi',
        'firebase'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords=['tracardi', 'plugin'],
    include_package_data=True,
    python_requires=">=3.8",
)
