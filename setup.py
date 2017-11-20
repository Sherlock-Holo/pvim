from setuptools import setup, find_packages

setup(
    name='pvim2',
    license='MPL',
    install_requires=['requests'],
    extras_require={'pyperclip': []},
    version='2.4',
    url='https://github.com/Sherlock-Holo/pvim',
    author='Sherlock Holo',
    author_email='sherlockya@gmail.com',
    description='pvim python version',
    packages=find_packages(),
    data_files=[('/etc/pvim2', ['pvim2.conf'])],
    entry_points={
        'console_scripts': [
            'pvim2 = pvim2.pvim2:main'
        ]
    },
    classifiers=[
        'Environment :: Console',
        'License :: OSI Approved :: MPL License',
        'Programming Language :: Python :: 3'
    ]
)
