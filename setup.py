import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nishant_miss_data_76", # Replace with your own username
    version="1.2.1",
    author="Nishant Goel",
    author_email="ngoel_be17@thapar.edu",
    description="Handle Missing Data",
    url="https://github.com/nishu195/nishant_miss_data_76",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["nishant_miss_data_76","missing_data_cli_76"],
    package_dir={'':'src'},
    entry_points = {
        'console_scripts': ['missing_data_cli_76=missing_data_cli_76:main'],
    },
    keywords = ['command-line', 'Missing-Data'],  
    install_requires=[            
          'numpy',
          'pandas',
      ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)