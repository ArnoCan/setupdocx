# 0. start polipo http/https

# 1. set proxy
export http_proxy=localhost:8125
export https_proxy=localhost:8125

# 2. set environ
. ./setenv-acue3.sh
. ./setenv.sh
. ~/venv/3.8.0/bin/activate


# 3. build

rm -f dist/*
python setup.py sdist

# python setup.py bdist

# 4. upload
twine upload  -u acue  dist/*
