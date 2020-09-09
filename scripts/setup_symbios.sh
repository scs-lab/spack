#!/bin/bash
spack install boost@1.74.0%gcc@9.3.0
spack install cmake@3.17.3%gcc@9.3.0
spack install dlib@19.17%gcc@9.3.0
spack install mongo-cxx-driver@3.5.1%gcc@9.3.0
spack install mpich@3.3.2%gcc@9.3.0
spack install redis-plus-plus@1.1.2%gcc@9.3.0
spack install rapidjson@1.1.0%gcc@9.3.0
spack install hiredis@1.0.0%gcc@9.3.0
spack install openblas@0.3.10%gcc@9.3.0
spack install hcl@master%gcc@9.3.0

spack env create symbios
spack env activate symbios

spack install boost@1.74.0%gcc@9.3.0
spack install cmake@3.17.3%gcc@9.3.0
spack install dlib@19.17%gcc@9.3.0
spack install mongo-cxx-driver@3.5.1%gcc@9.3.0
spack install mpich@3.3.2%gcc@9.3.0
spack install redis-plus-plus@1.1.2%gcc@9.3.0
spack install rapidjson@1.1.0%gcc@9.3.0
spack install hiredis@1.0.0%gcc@9.3.0
spack install openblas@0.3.10%gcc@9.3.0
spack install hcl@master%gcc@9.3.0

spack load boost@1.74.0%gcc@9.3.0
spack load cmake@3.17.3%gcc@9.3.0
spack load dlib@19.17%gcc@9.3.0
spack load hcl@master%gcc@9.3.0
spack load mongo-cxx-driver@3.5.1%gcc@9.3.0
spack load mpich@3.3.2%gcc@9.3.0
spack load redis-plus-plus@1.1.2%gcc@9.3.0
spack load rapidjson@1.1.0%gcc@9.3.0
spack load hiredis@1.0.0%gcc@9.3.0
spack load openblas@0.3.10%gcc@9.3.0
spack load rpclib@2.2.1%gcc@9.3.0

export CXXFLAGS="-I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/symbios/.spack-env/view/include -I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/symbios/.spack-env/view/include/bsoncxx/v_noabi -I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/symbios/.spack-env/view/include/mongocxx/v_noabi"
export LDFLAGS="-L/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/symbios/.spack-env/view/lib -L/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/symbios/.spack-env/view/lib64"
export LD_LIBRARY_PATH=/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/symbios/.spack-env/view/lib:/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/symbios/.spack-env/view/lib64
