from setuptools import setup, find_packages

__version__ = '0.2.0'


setup(
    name='kinpy',
    version=__version__,
    author='neka-nat',
    author_email='nekanat.stock@gmail.com',
    description='Robotics kinematic calculation toolkit',
    license='MIT',
    keywords='robot kinematics',
    url='http://github.com/neka-nat/kinpy',
    packages=find_packages(exclude=["tests"]), #['kinpy'],
    include_package_data = True,
    package_data = {'': ['kinpy/mjcf_parser/schema.xml']},
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    install_requires=['numpy', 'scipy', 'absl-py', 'pyyaml',
                      'lxml', 'transformations>=2022.10.18', 'vtk'],
    dependency_links = [
        'git+https://github.com/RebootMotion/transformations@reboot_init#egg=transformations-2022.10.18'
    ]
)
