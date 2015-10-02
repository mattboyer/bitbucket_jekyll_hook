from setuptools import setup
import version


setup(
    name='bitbucket-jekyll-hook',
    version=version.get_git_version(),
    url='https://github.com/mattboyer/bitbucket_jekyll_hook',
    description='fdfd',
    author='Matt Boyer',
    author_email='mboyer@sdf.org',
    license='BSD',
    classifiers=[
        #'Environment :: Console',
        #'Development Status :: 3 - Alpha',
        #'Intended Audience :: Developers',
        #'License :: OSI Approved :: BSD License',
        #'Operating System :: POSIX',
        #'Topic :: Software Development :: Version Control',
        #'Programming Language :: Python :: 2.6',
        #'Programming Language :: Python :: 2.7',
        #'Programming Language :: Python :: 3.3',
        #'Programming Language :: Python :: 3.4',
    ],
    keywords='git webhook bitbucket jekyll publish',
    packages=['BB_jekyll_hook'],
    include_package_data=True,
    data_files = [],
    install_requires=['flask'],
    entry_points={
        'console_scripts': [
            'git-guilt = git_guilt.guilt:main'
        ]
    },
)
