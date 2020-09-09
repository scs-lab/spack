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
VERSION=`git branch | awk '{print$2}' | sed ':a;N;$!ba;s/\n//g'`
SPACK_INSTALL_DIR=${SPACK_INSTALL_DIR_ORIG}/$VERSION

BINARY_DIR=${SPACK_INSTALL_DIR}/binary

echo "[INFO] The following directories will be overwritten."
echo "[INFO]      $SPACK_INSTALL_DIR"
read -p "Are you sure? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Nn]$ ]]
then
    exit
fi
echo "[INFO] Cleaning existing installations"
rm -rf $SPACK_INSTALL_DIR
mkdir -p $SPACK_INSTALL_DIR


echo "[INFO] Installing spack"
#tar cvf - ${REPO_DIR}/. | (cd $SPACK_INSTALL_DIR/; tar xvf -)

cp -r ${REPO_DIR}/.* $SPACK_INSTALL_DIR/

./install_client.sh $SPACK_INSTALL_DIR_ORIG
echo "[WARNING] if you ran spack multiple times please clean your bashrc."
