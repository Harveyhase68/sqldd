from setuptools import find_packages, setup

setup(
    name="sqldd",
    description="A special internal sql parser for use of an data dictionaray",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/harveyhase68/sqlgdd",
    author="Alexander Predl",
    author_email="alexander.predl@gmail.com",
    license="MIT",
    packages=find_packages(include=["sqldd", "sqldd.*"]),
    package_data={"sqldd": ["py.typed"]},
    use_scm_version={
        "write_to": "sqldd/_version.py",
        "fallback_version": "0.0.0",
        "local_scheme": "no-local-version",
    },
    setup_requires=["setuptools_scm"],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 1 - bloody/alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: SQL",
        "Programming Language :: Python :: 3 :: Only",
    ],
)
