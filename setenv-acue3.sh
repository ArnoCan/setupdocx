#
# - do not deploy public
# - source this first
#

# Python releases
export SDK_PATH_NAMEDTUPLEDEFS=/local/hd1/home1/data/acue/rd/p-open-deploy/namedtupledefs/components/namedtupledefs/

# export SDK_PATH_SETUPLIB=/local/hd1/home1/data/acue/rd/p-open-deploy/setuplib/components/setuplib/
export SDK_PATH_SETUPBASHX=/local/hd1/home1/data/acue/rd/p-open-deploy/setupbashx/components/setupbashx/
export SDK_PATH_SETUPCX=/local/hd1/home1/data/acue/rd/p-open-deploy/setupcx/components/setupcx/
export SDK_PATH_SETUPCPPX=/local/hd1/home1/data/acue/rd/p-open-deploy/setupcppx/components/setupcppx/
export SDK_PATH_SETUPDOCX=/local/hd1/home1/data/acue/rd/p-open-deploy/setupdocx/components/setupdocx/
export SDK_PATH_SETUPJAVASCRIPTX=/local/hd1/home1/data/acue/rd/p-open-deploy/setupjavascriptx/components/setupjavascriptx/
export SDK_PATH_SETUPJAVAX=/local/hd1/home1/data/acue/rd/p-open-deploy/setupjavax/components/setupjavax/
export SDK_PATH_SETUPLUAX=/local/hd1/home1/data/acue/rd/p-open-deploy/setupluax/components/setupluax/
export SDK_PATH_SETUPRUBYX=/local/hd1/home1/data/acue/rd/p-open-deploy/setuprubyx/components/setuprubyx/
export SDK_PATH_SETUPTESTX=/local/hd1/home1/data/acue/rd/p-open-deploy/setuptestx/components/setuptestx/
export SDK_PATH_SETUPLIB=/local/hd1/home1/data/acue/rd/p-open-deploy/setuplib/components/setuplib/

# generic
export SDK_PATH_NAMEDTUPLEX=/local/hd1/home1/data/acue/rd/p-open-deploy/namedtuplex/components/namedtuplex/
export SDK_PATH_FILESYSOBJECTS=/local/hd1/home1/data/acue/rd/p-open-deploy/filesysobjects/components/pyfilesysobjects/
export SDK_PATH_JSONDATA=/local/hd1/home1/data/acue/rd/p-open-deploy/jsondata/components/pyjsondata/
export SDK_PATH_MULTICONF=/local/hd1/home1/data/acue/rd/p-open-deploy/multiconf/components/pymulticonf/
export SDK_PATH_PLATFORMIDS=/local/hd1/home1/data/acue/rd/p-open-deploy/platformids/components/pyplatformids/
export SDK_PATH_PYTHONDISTIDS=/local/hd1/home1/data/acue/rd/p-open-deploy/pythonids/components/pythonids/
export SDK_PATH_RDBG=/local/hd1/home1/data/acue/rd/p-open-deploy/rdbg/components/pyrdbg/
export SDK_PATH_SOURCEINFO=/local/hd1/home1/data/acue/rd/p-open-deploy/sourceinfo/components/pysourceinfo/
export SDK_PATH_YAPYUTILS=/local/hd1/home1/data/acue/rd/p-open-deploy/yapyutils/components/yapyutils/
export SDK_PATH_YAPYDATA=/local/hd1/home1/data/acue/rd/p-open-deploy/yapydata/components/yapydata/

export SDK_PATH_SYSCALLS=/local/hd1/home1/data/acue/rd/p-open-deploy-next/syscalls/components/pysyscalls/
export SDK_PATH_EPYUNIT=/local/hd1/home1/data/acue/rd/p-open-deploy-next/epyunit/components/epyunit/


export SDK_PATH_EPYDOC4=/local/hd1/home1/data/acue/rd/p-open-set-documentation/apydoc/components/epydoc-4
export SDK_PATH_EPYDOC3=/local/hd1/home1/data/acue/rd/p-open-set-documentation/apydoc/components/epydoc


#
##############
#

# centos6: . /opt/rh/python27/enable
# centos6: . /opt/rh/python33/enable
# centos6: ssh -R 5678:localhost:5678 root@centos6 . ./setenv.sh \&\& . /opt/rh/python27/enable \&\& python -m unittest discover -s tests.30_libs.platforms.scan.dist.centos -p CallCase.py --rdbg
# opensuse:  scp -r /local/hd1/home1/data/acue/rd/p-open-staging.lap001/jsondata/components/jsondata/jsondata /local/hd1/home1/data/acue/rd/p-open-staging.lap001/namedtuplex/components/namedtuplex/namedtuplex /local/hd1/home1/data/acue/rd/p-open-staging.lap001/sourceinfo/components/pysourceinfo/pysourceinfo root@opensuse15:.
# ssh -R 5678:localhost:5678 test@solaris11liveinst . ./setenv.sh \&\& python -m unittest  -- --rdbg --rdbg-map "/local/hd1/home1/data/acue/rd/p-open-staging.lap001/platformids/components/pyplatformids/tests/[latformids/00_manual_validation/Case000/CallCase.py"  "/root"
# ssh -R 5678:localhost:5678 test@solaris11liveinst . ./setenv.sh \&\& python -m unittest  /local/hd1/home1/data/acue/rd/p-open-staging.lap001/platformids/components/pyplatformids/tests/[latformids/00_manual_validation/Case000/CallCase.py -- --rdbg --rdbg-map "/local/hd1/home1/data/acue/rd/p-open-staging.lap001/platformids/components/pyplatformids/tests/[latformids/00_manual_validation/Case000/CallCase.py"  "/root"
# ssh -R 5678:localhost:5678 test@solaris11liveinst . ./setenv.sh \&\& python tests/platformids/00_manual_validation/Case000/CallCase.py  --rdbg --rdbg-map "/local/hd1/home1/data/acue/rd/p-open-staging.lap001/platformids/components/pyplatformids"  "/root"
# soaris10
# export PATH=/opt/python/python-2.7.14/bin:$PATH
# export PYTHONPATH=/opt/python/python-2.7.14/lib/python2.7:$PYTHONPATH
# export LD_LIBRARY_PATH=/opt/python/python-2.7.14/lib:$LD_LIBRARY_PATH
# soaris10
# export PATH=/opt/python/python-3.6.5/bin:$PATH
# export PYTHONPATH=/opt/python/python-3.6.5/lib/python3.6:$PYTHONPATH
# export LD_LIBRARY_PATH=/opt/python/python-3.6.5/lib:$LD_LIBRARY_PATH
#
