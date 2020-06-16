import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="plot_utils",
    version="0.0.1",
    author="Geza Kovacs",
    author_email="noreply@gkovacs.com",
    description="High level API for plotting via Plotly",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gkovacs/python-plot-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)