from setuptools import find_packages, setup


def _read_reqs(req_path):
    with open(req_path) as f:
        return [
            s.strip() for s in f.readlines()
            if s.strip() and not s.strip().startswith('#')
        ]


setup(
    name="pex-test",
    version='0.1',
    install_requires=_read_reqs("requirements.txt"),
)
