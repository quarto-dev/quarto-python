import setuptools

with open("DESCRIPTION.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="quarto", 
    version="0.1.0",
    author="JJ Allaire",
    author_email="jj@rstudio.com",
    description="Python Interface to 'Quarto' Markdown Publishing System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quarto-dev/quarto-python",
    packages=setuptools.find_packages(),
    install_requires=["jupyter_core", "nbformat", "nbclient", "ipykernel", "pyyaml"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)