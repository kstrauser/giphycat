from setuptools import setup

setup(
    name='giphycat',
    version='0.1',
    author='Kirk Strauser',
    author_email='kirk@strauser.com',
    description='Fetch and display a Giphy image in an iTerm 2 window',
    license='MIT',
    keywords='giphy iterm iterm2',
    url='https://github.com/kstrauser/giphycat',
    packages=['giphycat'],
    install_requires=[
        'giphypop',
        'iterm2-tools',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'giphycat = giphycat.giphycat:handle_command_line',
        ]
    }
)
