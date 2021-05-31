from setuptools import setup, find_packages

setup(
        name="weekendinator",
        desc="Assign groups to weekends, easily",
        author="Cara Salter, Raleigh Wise",
        author_email="cara@devcara.com",
        packages=find_packages(),
        include_package_data=True,
        zip_safe=False,
)
