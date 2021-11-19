import setuptools

setuptools.setup(
    name='ljwedb',
    version='1.1.0',
    description='Database setup and management scripts for LJWE trading system',
    author='Leo J. Wotzak',
    author_email='leojwotzak@gmail.com',
    urls='https://github.com/leowotzak/ljwe-db',
    package_dir={'': 'ljwedb'},
    packages=setuptools.find_packages(where="ljwedb"),
    install_requires=[
        'SQLAlchemy',
        'requests',
        'python-dotenv',
        'postgres',
        'pandas',
        'alembic',
    ]
)