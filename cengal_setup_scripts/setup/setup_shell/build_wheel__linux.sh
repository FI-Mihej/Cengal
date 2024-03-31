#!/bin/bash

PACKAGE_NAME="cengal"

IMAGES=("manylinux2014_x86_64" "musllinux_1_1_x86_64" "musllinux_1_2_x86_64")

declare -A DOCKER_IMAGES
DOCKER_IMAGES["manylinux2014_x86_64"]="cp310-cp310 cp311-cp311 cp312-cp312 cp313-cp313 cp38-cp38 cp39-cp39 pp310-pypy310_pp73 pp38-pypy38_pp73 pp39-pypy39_pp73"
DOCKER_IMAGES["musllinux_1_1_x86_64"]="cp310-cp310 cp38-cp38 cp39-cp39"
DOCKER_IMAGES["musllinux_1_2_x86_64"]="cp311-cp311 cp312-cp312 cp313-cp313"

declare -A PLATFORM_TAGS
PLATFORM_TAGS["manylinux2014_x86_64"]="manylinux_2_17_x86_64.manylinux2014_x86_64"
PLATFORM_TAGS["musllinux_1_1_x86_64"]="musllinux_1_1_x86_64"
PLATFORM_TAGS["musllinux_1_2_x86_64"]="musllinux_1_2_x86_64"

declare -A PYTHON_SHORT_VERSIONS
PYTHON_SHORT_VERSIONS["cp310-cp310"]="cp310"
PYTHON_SHORT_VERSIONS["cp311-cp311"]="cp311"
PYTHON_SHORT_VERSIONS["cp312-cp312"]="cp312"
PYTHON_SHORT_VERSIONS["cp313-cp313"]="cp313"
PYTHON_SHORT_VERSIONS["cp38-cp38"]="cp38"
PYTHON_SHORT_VERSIONS["cp39-cp39"]="cp39"
PYTHON_SHORT_VERSIONS["pp310-pypy310_pp73"]="pp310"
PYTHON_SHORT_VERSIONS["pp38-pypy38_pp73"]="pp38"
PYTHON_SHORT_VERSIONS["pp39-pypy39_pp73"]="pp39"

read -p "Enter PyPI username: " PYPI_USERNAME
read -s -p "Enter PyPI password: " PYPI_PASSWORD
echo

echo "Removing old builds"
sudo chown -R $(id -u):$(id -g) .
rm -rf ./build
rm -rf ./dist
rm -rf ./sdist
rm -rf ./wheel
rm -rf ./wheelhouse

mkdir -p wheelhouse

for IMAGE_NAME in "${IMAGES[@]}"; do
    PLATFORM_TAG=${PLATFORM_TAGS[$IMAGE_NAME]}
    echo "Pulling image: quay.io/pypa/$IMAGE_NAME"
    docker pull quay.io/pypa/$IMAGE_NAME

    echo "Processing image: quay.io/pypa/$IMAGE_NAME"
    PYTHON_VERSIONS=${DOCKER_IMAGES[$IMAGE_NAME]}

    for PYTHON_VER in $PYTHON_VERSIONS; do
        PYTHON_SHORT_VER=${PYTHON_SHORT_VERSIONS[$PYTHON_VER]}
        echo ""
        echo " << Building $PYTHON_SHORT_VER wheel for Python $PYTHON_VER inside $IMAGE_NAME >>"

        docker run -i -v `pwd`:/io quay.io/pypa/$IMAGE_NAME /bin/bash -c "
            /opt/python/$PYTHON_VER/bin/pip install --upgrade pip;
            /opt/python/$PYTHON_VER/bin/pip install --upgrade setuptools;
            /opt/python/$PYTHON_VER/bin/pip install --upgrade wheel;
            /opt/python/$PYTHON_VER/bin/pip install --upgrade auditwheel;
            /opt/python/$PYTHON_VER/bin/pip install -r /io/requirements.txt;
            /opt/python/$PYTHON_VER/bin/pip wheel /io/ -w wheelhouse/;
            /io/rename_wheel.sh $PYTHON_SHORT_VER $PLATFORM_TAG
            cp -R wheelhouse/${PACKAGE_NAME}-*-$PYTHON_SHORT_VER-none-$PLATFORM_TAG.whl /io/wheelhouse/;
        "
    done
done


for IMAGE_NAME in "${IMAGES[@]}"; do
    PLATFORM_TAG=${PLATFORM_TAGS[$IMAGE_NAME]}
    echo "Uploading wheels for $IMAGE_NAME to PyPI..."
    twine upload --username "$PYPI_USERNAME" --password "$PYPI_PASSWORD" wheelhouse/${PACKAGE_NAME}-*-none-$PLATFORM_TAG.whl
done

sudo chown -R $(id -u):$(id -g) .

echo "Upload complete."
