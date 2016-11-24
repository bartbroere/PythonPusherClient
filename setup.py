from setuptools import setup

VERSION = "0.3.1"

requirements = ["websocket-client"]

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name="pusherclientb",
    version=VERSION,
    description="Pusher websocket client for python",
    long_description=readme(),
    keywords="pusher websocket client",
    author="Bart Broere",
    author_email="mail@bartbroere.eu",
    license="MIT",
    url="https://github.com/bartbroere/PythonPusherClient",
    install_requires=requirements,
    packages=["pusherclientb"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries ',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
