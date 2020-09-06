#!/bin/bash
if [ $# -lt 1 ]
then
  echo "Usage: ./install.sh <install_dir>"
  echo "e.g ./install.sh /opt/ohpc/pub/software/hdevarajan/spack/0.15.4"
  exit
fi

if [ $# -lt 1 ]
then
  SPACK_INSTALL_DIR_ORIG=$HOME/software/spack
else
  SPACK_INSTALL_DIR_ORIG=$1
fi

SCRIPT_DIR=`pwd`
REPO_DIR="$(dirname "$SCRIPT_DIR")"
VERSION=`git branch | awk '{print$2}'  | sed ':a;N;$!ba;s/\n//g'`
SPACK_INSTALL_DIR=$SPACK_INSTALL_DIR_ORIG/$VERSION

echo "[INFO] Updating bashrc with spack env."
echo "export PATH=$SPACK_INSTALL_DIR/bin:$PATH" >> ~/.bashrc
echo "export spack=$SPACK_INSTALL_DIR" >> ~/.bashrc
echo ". $SPACK_INSTALL_DIR/share/spack/setup-env.sh" >> ~/.bashrc

echo "[INFO] Setting up spack env."
source ~/.bashrc
