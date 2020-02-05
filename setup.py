from setuptools import setup, find_packages

setup(
    name='epeuva_cli',
    version='0.1.2',
    description='Epeuva CLI tool',
    url='https://github.com/DT42/epeuva-cli',
    author='DT42',
    author_email='contact@dt42.io',
    license='DT42',
    packages=find_packages(exclude=['tests']),
    python_requires='>=3.4',
    install_requires=[
        'click',
        'Pygments',
        'requests-mock',
        'requests',
        'tqdm',
    ],
    entry_points={
        'console_scripts': [
            'epeuva=epeuva_cli.__main__:main',
        ],
    },
    test_suite='tests'
)
