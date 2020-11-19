import pathlib
import setuptools

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()


setuptools.setup(
    	name="wtfpy-memoman",
    	version="1.0.0",
    	author="Zyycyx",
    	author_email="pth@gmail.hu",
    	description="A basic module to work with memory addresses and references.",
    	long_description=README,
    	long_description_content_type="text/markdown",
    	url="https://github.com/Zyycyx/wtfpy",
    	packages=setuptools.find_packages(),
    	classifiers=[
        	"Programming Language :: Python :: 3.8",
        	"License :: OSI Approved :: MIT License",
        	"Operating System :: OS Independent",
    	],
	include_package_data=True,
	install_requires=["sys", "array"],
    	python_requires='>=3.7',
)

