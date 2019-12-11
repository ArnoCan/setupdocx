#!/usr/bin/bash

MYPATH=${BASH_SOURCE%/*}/
if [[ "X${MYPATH:0:1}" == "X." ]];then
	MYPATH=${PWD}/${MYPATH:1}
fi

MY_SDK_PATH=${BASH_SOURCE%/*}
if [ "X${MY_SDK_PATH#.}" != "X${MY_SDK_PATH}" ];then
	MY_SDK_PATH=${PWD}/${MY_SDK_PATH#.}
fi
PYTHONPATH=${MY_SDK_PATH}:$PYTHONPATH
export PYTHONPATH

if [[ ! -e "${PWD}/epyunit" ]];then
	if [[ ! -e "$SDK_PATH_EPYUNIT" ]];then echo "ERROR:SDK requires: SDK_PATH_EPYUNIT" >&2 ; fi
	PYTHONPATH=$SDK_PATH_EPYUNIT:$PYTHONPATH
else
	SDK_PATH_EPYUNIT="${PWD}/epyunit"
fi

if [[ ! -e "${PWD}/filesysobjects" ]];then
	if [[ ! -e "$SDK_PATH_FILESYSOBJECTS" ]];then echo "ERROR:SDK requires: SDK_PATH_FILESYSOBJECTS" >&2 ; fi
	PYTHONPATH=$SDK_PATH_FILESYSOBJECTS:$PYTHONPATH
else
	SDK_PATH_FILESYSOBJECTS="${PWD}/filesysobjects"
fi

if [[ ! -e "${PWD}/jsondata" ]];then
	if [[ ! -e "$SDK_PATH_JSONDATA" ]];then echo "ERROR:SDK requires: SDK_PATH_JSONDATA" >&2 ; fi
	PYTHONPATH=$SDK_PATH_JSONDATA:$PYTHONPATH
else
	SDK_PATH_JSONDATA="${PWD}/jsondata"
fi

if [[ ! -e "${PWD}/multiconf" ]];then
	if [[ ! -e "$SDK_PATH_MULTICONF" ]];then echo "ERROR:SDK requires: SDK_PATH_MULTICONF" >&2 ; fi
	PYTHONPATH=$SDK_PATH_MULTICONF:$PYTHONPATH
else
	SDK_PATH_EPYUNIT="${PWD}/multiconf"
fi

if [[ ! -e "${PWD}/platformids" ]];then
	if [[ ! -e "$SDK_PATH_PLATFORMIDS" ]];then echo "ERROR:SDK requires: SDK_PATH_PLATFORMIDS" >&2 ; fi
	PYTHONPATH=$SDK_PATH_PLATFORMIDS:$PYTHONPATH
else
	SDK_PATH_PLATFORMIDS="${PWD}/platformids"
fi

if [[ ! -e "${PWD}/pythonids" ]];then
	if [[ ! -e "$SDK_PATH_PYTHONDISTIDS" ]];then echo "ERROR:SDK requires: SDK_PATH_PYTHONDISTIDS" >&2 ; fi
	PYTHONPATH=$SDK_PATH_PYTHONDISTIDS:$PYTHONPATH
else
	SDK_PATH_PYTHONDISTIDS="${PWD}/pythonids"
fi

if [[ ! -e "${PWD}/rdbg" ]];then
	if [[ ! -e "$SDK_PATH_RDBG" ]];then echo "ERROR:SDK requires: SDK_PATH_RDBG" >&2 ; fi
	PYTHONPATH=$SDK_PATH_RDBG:$PYTHONPATH
else
	SDK_PATH_EPYUNIT="${PWD}/rdbg"
fi

if [[ ! -e "${PWD}/sourceinfo" ]];then
	if [[ ! -e "$SDK_PATH_SOURCEINFO" ]];then echo "ERROR:SDK requires: SDK_PATH_SOURCEINFO" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SOURCEINFO:$PYTHONPATH
else
	SDK_PATH_SOURCEINFO="${PWD}/sourceinfo"
fi

if [[ ! -e "${PWD}/syscalls" ]];then
	if [[ ! -e "$SDK_PATH_SYSCALLS" ]];then echo "ERROR:SDK requires: SDK_PATH_SYSCALLS" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SYSCALLS:$PYTHONPATH
else
	SDK_PATH_SYSCALLS="${PWD}/syscalls"
fi

if [[ ! -e "${PWD}/namedtuplex" ]];then
	if [[ ! -e "$SDK_PATH_NAMEDTUPLEX" ]];then echo "ERROR:SDK requires: SDK_PATH_NAMEDTUPLEX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_NAMEDTUPLEX:$PYTHONPATH
else
	SDK_PATH_NAMEDTUPLEX="${PWD}/namedtuplex"
fi

if [[ ! -e "${PWD}/namedtupledefs" ]];then
	if [[ ! -e "$SDK_PATH_NAMEDTUPLEDEFS" ]];then echo "ERROR:SDK requires: SDK_PATH_NAMEDTUPLEDEFS" >&2 ; fi
	PYTHONPATH=$SDK_PATH_NAMEDTUPLEDEFS:$PYTHONPATH
else
	SDK_PATH_NAMEDTUPLEDEFS="${PWD}/namedtupledefs"
fi

if [[ ! -e "${PWD}/yapyutils" ]];then
	if [[ ! -e "$SDK_PATH_YAPYUTILS" ]];then echo "ERROR:SDK requires: SDK_PATH_YAPYUTILS" >&2 ; fi
	PYTHONPATH=$SDK_PATH_YAPYUTILS:$PYTHONPATH
else
	SDK_PATH_YAPYUTILS="${PWD}/yapyutils"
fi

if [[ ! -e "${PWD}/yapydata" ]];then
	if [[ ! -e "$SDK_PATH_YAPYDATA" ]];then echo "ERROR:SDK requires: SDK_PATH_YAPYDATA" >&2 ; fi
	PYTHONPATH=$SDK_PATH_YAPYDATA:$PYTHONPATH
else
	SDK_PATH_YAPYDATA="${PWD}/yapydata"
fi


if [[ ! -e "${PWD}/setupdocx" ]];then
	if [[ ! -e "$SDK_PATH_SETUPDOCX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPDOCX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPDOCX:$PYTHONPATH
else
	SDK_PATH_SETUPDOCX="${PWD}/setupdocx"
fi

if [[ ! -e "${PWD}/setuptestx" ]];then
	if [[ ! -e "$SDK_PATH_SETUPTESTX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPTESTX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPTESTX:$PYTHONPATH
else
	SDK_PATH_SETUPTESTX="${PWD}/setuptestx"
fi

if [[ ! -e "${PWD}/setupjavax" ]];then
	if [[ ! -e "$SDK_PATH_SETUPJAVAX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPJAVAX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPJAVAX:$PYTHONPATH
else
	SDK_PATH_SETUPJAVAX="${PWD}/setupjavax"
fi

if [[ ! -e "${PWD}/setupjavascriptx" ]];then
	if [[ ! -e "$SDK_PATH_SETUPJAVASCRIPTX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPJAVASCRIPTX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPJAVASCRIPTX:$PYTHONPATH
else
	SDK_PATH_SETUPJAVASCRIPTX="${PWD}/setupjavascriptx"
fi

if [[ ! -e "${PWD}/setupcx" ]];then
	if [[ ! -e "$SDK_PATH_SETUPCX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPCX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPCX:$PYTHONPATH
else
	SDK_PATH_SETUPCX="${PWD}/setupcx"
fi

if [[ ! -e "${PWD}/setupcppx" ]];then
	if [[ ! -e "$SDK_PATH_SETUPCPPX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPCPPX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPCPPX:$PYTHONPATH
else
	SDK_PATH_SETUPCPPX="${PWD}/setupcppx"
fi

if [[ ! -e "${PWD}/setupbashx" ]];then
	if [[ ! -e "$SDK_PATH_SETUPBASHX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPBASHX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPBASHX:$PYTHONPATH
else
	SDK_PATH_SETUPBASHX="${PWD}/setupbashx"
fi

if [[ ! -e "${PWD}/setuprubyx" ]];then
	if [[ ! -e "$SDK_PATH_SETUPRUBYX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPRUBYX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPRUBYX:$PYTHONPATH
else
	SDK_PATH_SETUPRUBYX="${PWD}/setuprubyx"
fi

if [[ ! -e "${PWD}/setupluax" ]];then
	if [[ ! -e "$SDK_PATH_SETUPLUAX" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPLUAX" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPLUAX:$PYTHONPATH
else
	SDK_PATH_SETUPLUAX="${PWD}/setupluax"
fi

if [[ ! -e "${PWD}/setuplib" ]];then
	if [[ ! -e "$SDK_PATH_SETUPLIB" ]];then echo "ERROR:SDK requires: SDK_PATH_SETUPLIB" >&2 ; fi
	PYTHONPATH=$SDK_PATH_SETUPLIB:$PYTHONPATH
else
	SDK_PATH_SETUPLIB="${PWD}/setuplib"
fi

#if [[ ! -e "${PWD}/epydoc" ]];then
#	if [[ ! -e "$SDK_PATH_EPYDOC3" ]];then echo "ERROR:SDK requires: SDK_PATH_EPYDOC3" >&2 ; fi
#	PYTHONPATH=$SDK_PATH_EPYDOC3:$PYTHONPATH
#else
#	SDK_PATH_EPYDOC3="${PWD}/epydoc"
#	PATH=${SDK_PATH_EPYDOC3}/bin:${SDK_PATH_EPYDOC3}/scripts:$PATH
#fi

if [[ ! -e "${PWD}/epydoc" ]];then
	if [[ ! -e "$SDK_PATH_EPYDOC4" ]];then echo "ERROR:SDK requires: SDK_PATH_EPYDOC4" >&2 ; fi
	PYTHONPATH=$SDK_PATH_EPYDOC4:$PYTHONPATH
	PATH=${SDK_PATH_EPYDOC4}/bin:${SDK_PATH_EPYDOC4}/scripts:$PATH
else
	SDK_PATH_EPYDOC4="${PWD}/epydoc"
fi

PYTHONPATH=$PWD:$PYTHONPATH
JYTHONPATH=$PYTHONPATH
PYTHONPATH=$PYTHONPATH:$PYTHONPATH_SYS

PATH=${MY_SDK_PATH}/bin:$PATH

export PATH
export PYTHONPATH
export JYTHONPATH
