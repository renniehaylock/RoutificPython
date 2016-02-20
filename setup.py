"""
A wrapper package module for Routific API

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/renniehaylock/RoutificPython
"""

setup(
     name='routific',
     version='0.0.1',
     description='A wrapper package module for Routific API',
     url='https://github.com/renniehaylock/RoutificPython',
     author='Rennie Haylock',
     license='MIT',
     classifiers= [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
     ],
     keywords='routific',
     packages=find_packages(),
     install_requires=[]
)
