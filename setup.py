import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wtfpy-memorymanagement-Zyycyx", 
    version="0.0.1",
    author="Zyycyx",
    author_email="pth@gmail.hu",
    description="A basic module to work with memory addresses and references.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Zyycyx/wtfpy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

