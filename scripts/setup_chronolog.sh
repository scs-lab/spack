#!/bin/bash
spack install boost@1.74.0%gcc@9.3.0
spack install cmake@3.17.3%gcc@9.3.0
spack install mpich@3.3.2%gcc@9.3.0
spack install rapidjson@1.1.0%gcc@9.3.0
spack install hcl@master%gcc@9.3.0
spack install java@8
spack isntall maven@3.6.3
spack install flink@1.9.1

spack env create chronolog
spack env activate chronolog

spack install boost@1.74.0%gcc@9.3.0
spack install cmake@3.17.3%gcc@9.3.0
spack install mpich@3.3.2%gcc@9.3.0
spack install rapidjson@1.1.0%gcc@9.3.0
spack install hcl@master%gcc@9.3.0
spack install java@8
spack isntall maven@3.6.3
spack install flink@1.9.1

spack load boost@1.74.0%gcc@9.3.0
spack load cmake@3.17.3%gcc@9.3.0
spack load hcl@master%gcc@9.3.0
spack load mpich@3.3.2%gcc@9.3.0
spack load rapidjson@1.1.0%gcc@9.3.0
spack load rpclib@2.2.1%gcc@9.3.0
spack load java@8
spack load maven@3.6.3
spack load flink@1.9.1

export CXXFLAGS="-I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/chronolog/.spack-env/view/include -I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/chronolog/.spack-env/view/include/bsoncxx/v_noabi -I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/chronolog/.spack-env/view/include/mongocxx/v_noabi"
export LDFLAGS="-L/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/chronolog/.spack-env/view/lib -L/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/chronolog/.spack-env/view/lib64"
export LD_LIBRARY_PATH=/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/chronolog/.spack-env/view/lib:/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/chronolog/.spack-env/view/lib64
