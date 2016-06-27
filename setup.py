from distutils.core import setup

setup(
    name='xonsh-autoxsh',
    version='0.1',
    url='-',
    license='GPLv3',
    author='Bernardas Ališauskas',
    author_email='bernardas.alisauskas@gmail.com',
    description="Auto launcher of `.autoxsh` scripts for Xonsh shell's `cd` function",
    packages=['xontrib'],
    package_dir={'xontrib': 'xontrib'},
    package_data={'xontrib': ['*.xsh']},
)
