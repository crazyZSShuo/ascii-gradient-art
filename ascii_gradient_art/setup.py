
from setuptools import setup, find_packages

setup(
    name="ascii-gradient-art",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pyfiglet",
    ],
    entry_points={
        "console_scripts": [
            "ascii-gradient-art=ascii_gradient_art.ascii_gradient_art:main",
        ],
    },
    author="Maxzs",
    author_email="zsshuo1024@gmail.com",
    description="A command-line tool to generate colorful ASCII art with gradients and animations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/crazyZSShuo/ascii-gradient-art.git", # Placeholder URL
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
)



