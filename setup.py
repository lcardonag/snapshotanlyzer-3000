import setuptools

setuptools.setup(
    name = 'snapshotalyzer-2020',
    version = '0.1',
    author='Luis Cardona',
    author_email='lcardonag@gmail.com',
    description='Snapshotalyer is a tool to manage AWS EC2 instances and snapshots',
    license='GPLv3+',
    packages=['shotty'],
    url='https://github.com/lcardonag/snapshotanlyzer-3000',
    install_requires=['click','boto3'],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
        ''',
)
