# -*- coding: utf-8 -*-
# Author: Douglas Creager <dcreager@dcreager.net>
# This file is placed into the public domain.

# Calculates the current version number.  If possible, this is the
# output of “git describe”, modified to conform to the versioning
# scheme that setuptools uses.  If “git describe” returns an error
# (most likely because we're in an unpacked copy of a release tarball,
# rather than in a git working copy), then we fall back on reading the
# contents of the RELEASE-VERSION file.
#
# To use this script, simply import it your setup.py file, and use the
# results of get_git_version() as your package version:
#
# from version import *
#
# setup(
#     version=get_git_version(),
#     .
#     .
#     .
# )
#
# This will automatically update the RELEASE-VERSION file, if
# necessary.  Note that the RELEASE-VERSION file should *not* be
# checked into git; please add it to your top-level .gitignore file.
#
# You'll probably want to distribute the RELEASE-VERSION file in your
# sdist tarballs; to do this, just create a MANIFEST.in file that
# contains the following line:
#
#   include RELEASE-VERSION

from __future__ import print_function

__all__ = ("get_git_version")

from BB_jekyll_hook.jekyll_hook import Runner, CmdError
import os


def call_git_describe(abbrev=4):
    runner = Runner('git')
    output = runner.run(['rev-parse', '--abbrev-ref', 'HEAD'])
    branch = output[0].strip()

    output = runner.run(['describe', '--long', '--abbrev=%d' % abbrev])
    tag = output[0].strip()
    release, commits_ahead, _ = tag.split('-')
    commits_ahead = int(commits_ahead)
    if commits_ahead:
        if 'master' == branch:
            return "{t}.post{c}".format(t=release, c=commits_ahead)
        else:
            return "{t}.dev{c}".format(t=release, c=commits_ahead)
    else:
        return release

def read_release_version():
    try:
        with open(get_release_version_path(), "r") as f:
            version = f.readlines()[0]
            return version.strip()
    except IOError:
        return None
    except OSError:
        return None

def get_release_version_path():
    top_level_dir = os.path.dirname(os.path.abspath(__file__))
    assert os.path.isdir(top_level_dir)
    rv_path = os.path.join(top_level_dir, 'RELEASE-VERSION')
    return rv_path

def write_release_version(version):
    f = open(get_release_version_path(), "w")
    f.write("%s\n" % version)
    f.close()


def get_git_version(abbrev=4):
    # Read in the version that's currently in RELEASE-VERSION.
    release_version = read_release_version()

    # First try to get the current version using “git describe”.
    try:
        version = call_git_describe(abbrev)
    except CmdError:
        # We're probably operating from a source dist
        version = None

    # If that doesn't work, fall back on the value that's in
    # RELEASE-VERSION.
    if version is None:
        version = release_version

    # If we still don't have anything, that's an error.
    if version is None:
        raise ValueError("Cannot find the version number!")

    # If the current version is different from what's in the
    # RELEASE-VERSION file, update the file to be current.
    if version != release_version:
        write_release_version(version)

    # Finally, return the current version.
    return version


if __name__ == "__main__":
    print(get_git_version())
