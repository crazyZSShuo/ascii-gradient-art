
from setuptools import setup, find_packages

setup(
    name="ascii-gradient-art",
    version="0.1.5",
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
    maintainer="Maxzs",
    description="A command-line tool to generate colorful ASCII art with gradients and animations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/crazyZSShuo/ascii-gradient-art",
    download_url="https://pypi.org/project/ascii-gradient-art/",
    project_urls={
        "Homepage": "https://github.com/crazyZSShuo/ascii-gradient-art",
        "Source Code": "https://github.com/crazyZSShuo/ascii-gradient-art",
        "Bug Tracker": "https://github.com/crazyZSShuo/ascii-gradient-art/issues",
        "Documentation": "https://github.com/crazyZSShuo/ascii-gradient-art#readme",
        "Download": "https://pypi.org/project/ascii-gradient-art/",
    },
    keywords=["ascii", "art", "gradient", "color", "animation", "terminal", "cli"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Artistic Software",
        "Topic :: Multimedia :: Graphics",
        "Topic :: Terminals",
        "Topic :: Utilities",
    ],
    python_requires=">=3.6",
    license="MIT",
)



