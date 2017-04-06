from setuptools import setup

setup(
    name = 'pvim2',
    license = 'GPL-3.0',
    install_requires = ['pyperclip'],
    version = '2.0.0',
    url = 'https://github.com/Sherlock-Holo/pvim',
    author = 'Sherlock Holo',
    author_email = 'sherlockya@gmail.com',
    description = 'pvim python version',
    scripts = ['pvim2.py'],
    classifiers = [
        'License :: OSI Approved :: GPL-3.0 License',
        'Programming Language :: Python :: 3.6'
        ]
)
