import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sinsta",
    version="0.0.1",
    author="Behrouz Safari",
    author_email="behrouz.safari@gmail.com",
    description="Simple Instagram API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/behrouzz/sinsta",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["sinsta"],
    include_package_data=True,
    install_requires=["requests", "pandas"],
    python_requires='>=3.4',
)
