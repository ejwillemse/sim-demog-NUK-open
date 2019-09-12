from setuptools import setup, find_packages

setup(
    name="sim-demog-NUK-open",

    version="0.1.1",
    
    author="Elias, Benny",
    author_email="elias_willemse@sutd.edu.sg, benny_chin@sutd.edu.sg",

    packages=['population',],

    include_package_data=True,

    url="https://github.com/ejwillemse/sim-demog-NUK-open",

    license="not specified",
    description="population simulation model for SG",

    long_description=open("README.md").read(),
    
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Education',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='Singapore, agent-based model, population structure, simulation',

    install_requires=[
		"configobj", 
        "pandas",
        "numpy",
        "matplotlib",
    ]
)
