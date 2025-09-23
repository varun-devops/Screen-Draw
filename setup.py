from setuptools import setup, find_packages

setup(
    name="WebTroopScreenDraw",
    version="1.0.0",
    description="A professional screen drawing tool",
    author="WebTroop",
    author_email="contact@webtroop.com",
    url="https://github.com/varun-devops/WebTroopScreenDraw",
    packages=find_packages(),
    package_data={
        'assets': ['*.ico'],
    },
    install_requires=[
        'pynput>=1.7.6',
        'pillow>=9.0.0',
    ],
    entry_points={
        'console_scripts': [
            'webtroop-screen-draw=WebTroopScreenDraw:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6",
)
