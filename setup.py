from setuptools import setup, find_packages

VERSION = "1.0.1"

setup(
    name="printwizard",
    version=VERSION,
    packages=find_packages(),
    install_requires=[],
    author="GoodBoyNeon (Sushant Ray)",
    author_email="<contact@neon.is-a.dev>",
    description="A minimal logger to make your print statements beautiful and functional",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
