from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='biblioteka_mh',
    version='0.0.1',
    description='biblioteka zaliczeniowa',
    long_description=open('README.txt').read(),
    url='',
    author='Miłosz Holeksa',
    author_email='m.holeksa@student.uw.edu.pl',
    license='MIT',
    classifiers=classifiers,
    keywords='',
    packages=find_packages(),
    install_requires=['pandas', 'numpy', ]
)