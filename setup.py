import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="python_hello",
    version="0.0.1",
    author="Cedd Burge",
    author_email="ceddlyburge@gmail.com",
    description="A function that returns 'hello world'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ceddlyburge/python-hello",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
	install_requires=[
        'python_world>=0.0',
    ],
    dependency_links=[
        'git+https://github.com/ceddlyburge/python_world#egg=python_world-0.0.1',
    ]
)