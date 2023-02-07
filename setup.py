from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="ssmpy",
    version="0.2.6",
    description="Basic functions to start using semantic similarity measures directly from a rdf or owl file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andre Lamurias",
    author_email="alamurias@lasige.di.fc.ul.pt",
    maintainer="Francisco M Couto",
    maintainer_email="fjcouto@edu.ulisboa.pt",
    packages=["ssmpy"],
    keywords=["graphs", "semantic similarity", "ontologies"],
    url="https://github.com/lasigeBioTM/DiShIn",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_data={"ssmpy": ["data/*"]},
    install_requires=["rdflib", "pandas; python_version>='3.8'"", "numpy>=1.18.5, <=1.19.5; python_version<='3.8'"], #'pandas; python_version >= 3.8'], #"numpy <= 1.19.5"], # "sqlite3","math", "multiprocessing","numpy<=1.19.5"
)
