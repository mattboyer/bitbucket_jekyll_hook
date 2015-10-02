from setuptools import setup
import version


setup(
    name='bitbucket-jekyll-hook',
    version=version.get_git_version(),
    url='https://github.com/mattboyer/bitbucket_jekyll_hook',
    description=('BitBucket webhook to trigger a static site build through '
        'Jekyll'),
    author='Matt Boyer',
    author_email='mboyer@sdf.org',
    license='BSD',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: No Input/Output (Daemon)',
        'Framework :: Flask',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
    keywords='git webhook bitbucket jekyll publish',
    packages=['BB_jekyll_hook'],
    install_requires=['flask'],
)
