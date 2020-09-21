#!/bin/bash
spack install boost@1.74.0%gcc@9.3.0
spack install cmake@3.17.3%gcc@9.3.0
spack install openmpi@4.0.5%gcc@9.3.0
spack install rapidjson@1.1.0%gcc@9.3.0
spack install hcl@master%gcc@9.3.0

spack env create rhea
spack env activate rhea

spack install boost@1.74.0%gcc@9.3.0
spack install cmake@3.17.3%gcc@9.3.0
spack install openmpi@4.0.5%gcc@9.3.0
spack install rapidjson@1.1.0%gcc@9.3.0
spack install hcl@master%gcc@9.3.0

spack load boost@1.74.0%gcc@9.3.0
spack load cmake@3.17.3%gcc@9.3.0
spack load hcl@master%gcc@9.3.0
spack load openmpi@4.0.5%gcc@9.3.0
spack load rapidjson@1.1.0%gcc@9.3.0
spack load rpclib@2.2.1%gcc@9.3.0

export CXXFLAGS="-I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/rhea/.spack-env/view/include -I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/rhea/.spack-env/view/include/bsoncxx/v_noabi -I/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/rhea/.spack-env/view/include/mongocxx/v_noabi"
export LDFLAGS="-L/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/rhea/.spack-env/view/lib -L/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/rhea/.spack-env/view/lib64"
export LD_LIBRARY_PATH=/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/rhea/.spack-env/view/lib:/opt/ohpc/pub/software/hdevarajan/spack/v0.15.4.scs/var/spack/environments/rhea/.spack-env/view/lib64
