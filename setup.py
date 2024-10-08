import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dvis",
    version="0.8.8.1",
    author="Norman Müller",
    author_email="norman.mueller@tum.de",
    url="https://github.com/SirWyver/dvis",
    description="The best web-based visualizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": ["dvis=dvis.dvis_cli:dvis_cli",
        "dvis-server=dvis.dvis_cli:dvis_server_cli"],
    },
    install_requires=[
        "flask>=3.0.3",
        "flask_socketio>=5.3.4",
        "numpy>=1.19.5",
        "pillow==9.4.0",
        "trimesh>=3.15.5",
        "simple-websocket>=0.2.0",
        "python-socketio>=4.6.1",
        "eventlet>=0.36.1",
        "jinja2>=3.0.2",
        "werkzeug>=2.0.3",
        "opencv-python"
    ],
)
