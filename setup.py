import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="affordable",
    version="0.0.0",
    author="Mingli Yuan",
    author_email="mingli.yuan@gmail.com",
    description="Affordable is an abstraction layer to facilitate RL environment developing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=" https://pypi.org/project/affordable",
    project_urls={
        'Documentation': 'https://packaging.python.org/tutorials/distributing-packages/',
        'Source': 'https://github.com/mountain/affordable',
        'Tracker': 'https://github.com/mountain/affordable/issues',
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'torch',
        'gym',
    ],
    test_suite='nose.collector',
    tests_require=['nose'],
)

