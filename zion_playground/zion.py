import contextlib
import os
import shutil
import tempfile

import delegator


def run(program_text):
    with program_context(program_text) as name:
        result = delegator.run('zion run {}'.format(name))
        return result.out


def fmt(program_text):
    with program_context(program_text) as name:
        result = delegator.run('zion fmt {}'.format(name))
        return result.out


@contextlib.contextmanager
def change_directory_context(path):
    original_path = os.getcwd()
    try:
        os.chdir(path)
        yield
    finally:
        os.chdir(original_path)

cd = change_directory_context


@contextlib.contextmanager
def program_context(program_text, program_name='program'):
    try:
        # Write program to temp file
        tempdir = tempfile.mkdtemp()
        program_path = os.path.join(tempdir, '{}.zion'.format(program_name))
        with open(program_path, 'w') as f:
            f.write(program_text)

        # Yield to caller
        with cd(tempdir):
            yield program_name

    finally:
        shutil.rmtree(tempdir)


