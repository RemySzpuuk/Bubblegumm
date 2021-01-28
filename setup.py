import setuptools
with open("README.md", 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Bubblegumm",
    version="0.1.0",
    author="Remy Szpuk",
    author_email="harryszpuk@outlook.com",
    description="Package for generating sitemaps",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/RemySzpuuk/bubblegumm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)