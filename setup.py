from setuptools import setup, find_packages
from setuptools.command.install import install


class PostInstallCommand(install):
    """Post-installation for boring package"""
    def run(self):
        install.run(self)
        print("\n")
        print("boring-package installed successfully.")
        print("Run 'boring-package <name>' to execute.")
        print("\n")


setup(
    name="boring-package",
    version="1.0.0",
    author="System Admin",
    author_email="admin@example.com",
    description="A utility package for system maintenance tasks",
    long_description="A simple utility package. Nothing interesting here.",
    long_description_content_type="text/plain",
    url="https://github.com/example/boring-package",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={
        'console_scripts': [
            'boring-package=valentines_surprise:main',
        ],
    },
)
