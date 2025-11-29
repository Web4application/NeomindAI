#!/usr/bin/env bash
# race.bash: Auto-run Go standard library tests with race detector
# Works on supported OS/architectures
# Can be run from any directory

set -e

# Supported OS/ARCH combinations
SUPPORTED=("Darwin x86_64" "Darwin arm64" "Linux x86_64" "Linux ppc64le" "Linux aarch64" "Linux s390x" "FreeBSD amd64" "NetBSD amd64" "OpenBSD amd64")

# Detect OS/ARCH
OS_ARCH="$(uname -s) $(uname -m)"
if [[ ! " ${SUPPORTED[*]} " =~ " ${OS_ARCH} " ]]; then
    echo "Race detector is not supported on $OS_ARCH"
    echo "Supported: ${SUPPORTED[*]}"
    exit 1
fi

# Detect GOROOT
if [[ -z "$GOROOT" ]]; then
    GOROOT=$(go env GOROOT)
    if [[ -z "$GOROOT" ]]; then
        echo "Cannot detect GOROOT. Please set it or install Go."
        exit 1
    fi
fi

SRC_DIR="$GOROOT/src"

if [[ ! -f "$SRC_DIR/make.bash" ]]; then
    echo "Cannot find make.bash in $SRC_DIR. Please ensure you have the Go source installed."
    exit 1
fi

echo "Running race detector for Go standard library..."
echo "GOROOT: $GOROOT"
echo "OS/ARCH: $OS_ARCH"

# Run make.bash without banner
pushd "$SRC_DIR" > /dev/null
. ./make.bash --no-banner

# Install std library with race detector
go install -race std

# Run tests
go tool dist test -race
popd > /dev/null

echo "✅ Race detection complete."
