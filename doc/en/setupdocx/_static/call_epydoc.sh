PROJECT='setupdocx'
VERSION=${DOCX_VERSION:-`date +%Y.%m.%d`}
RELEASE=${DOCX_RELEASE:-$VERSION}
AUTHOR='Arno-Can Uestuensoez'
COPYRIGHT='Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
LICENSE='Artistic-License-2.0 + Forced-Fairplay-Constraints'
STATUS='beta'
MISSION='Support extensions for setuptools / distutils.'
BUILDDATE=`date`

cat <<EOF
################################################################
#                                                              #
$(printf "# PROJECT = %-51s#" $PROJECT)
#                                                              #
# Generate API reference - default: epydoc                     #
#                                                              #
################################################################
EOF

# the absolute pathname for this source
MYPATH="${BASH_SOURCE%/*}/"
if [ "X${MYPATH#.}" != "X$MYPATH" ];then
	MYPATH="${PWD}/${MYPATH#.}";MYPATH="${MYPATH//\/\//\/}"
fi

# input base directory
INDIR="${INDIR:-$PWD}"
if [ "X${INDIR#.}" != "X$INDIR" ];then
	INDIR="${PWD}/${INDIR#.}";INDIR="${INDIR//\/\//\/}"
fi
INDIR="${INDIR}/"

# output base directory
DOCX_BUILDDIR="${DOCX_BUILDDIR:-build}/"
if [ ! -e "${DOCX_BUILDDIR}" ];then
	mkdir -p "${DOCX_BUILDDIR}"
fi
export PYTHONPATH="$PWD:$PYTHONPATH"

# document source directory
DOCX_DOCSRC="${DOCX_DOCSRC:-docsrc}"
DOCX_DOCSRC="${DOCX_DOCSRC%%/}"


# document source directory
DOCX_DOCNAME="${DOCX_DOCNAME:-$PROJECT}"


DOCX_VERBOSE=${DOCX_VERBOSE:-0}
if((DOCX_VERBOSE > 1));then
	echo "${0##*/}:Called:"
	echo "  $0 $@"
	echo "${0##*/}:Environ Options:"
	echo "  DOCX_APIREF      = '$DOCX_APIREF'"
	echo "  DOCX_BUILDDIR    = '$DOCX_BUILDDIR'"
	echo "  DOCX_CONFDIR     = '$DOCX_CONFDIR'"
	echo "  DOCX_DOCNAME     = '$DOCX_DOCNAME'"
	echo "  DOCX_DOCSRC      = '$DOCX_DOCSRC'"
	echo "  DOCX_DOCTYPE     = '$DOCX_DOCTYPE'"
	echo "  DOCX_NAME        = '$DOCX_NAME'"
	echo "  DOCX_INDEXSRC    = '$DOCX_INDEXSRC'"
	echo "  DOCX_RAWDOC      = '$DOCX_RAWDOC'"
	echo "  DOCX_RELEASE     = '$DOCX_RELEASE'"
	echo "  DOCX_SRCDIR      = '$DOCX_SRCDIR'"
	echo "  DOCX_VERBOSE     = '$DOCX_VERBOSE'"
	echo "  DOCX_VERSION     = '$DOCX_VERSION'"

	echo "  PATH             = '$PATH'"
	echo "  PYTHONPATH       = '$PYTHONPATH'"
	echo "  MYPATH           = '$MYPATH'"
	echo "  INDIR            = '$INDIR'"
	echo
fi

#
# *** start exec ***
#

if [ -e "${DOCX_CONFDIR}/epydoc.conf" ];then
	REFCONF="${DOCX_CONFDIR}/epydoc.conf"
else
	REFCONF="${DOCX_DOCSRC}/conf/epydoc.conf"	
fi
if [ -e "${DOCX_CONFDIR}/epydoc.css" ];then
	REFCSS="${DOCX_CONFDIR}/epydoc.css"
else
	REFCSS="${DOCX_DOCSRC}/conf/epydoc.css"	
fi


CALL=""
CALL="$CALL export PYTHONPATH=$PWD:$PYTHONPATH;"
CALL="$CALL epydoc "
CALL="$CALL --html "
CALL="$CALL --name '${DOCX_NAME}'"
# CALL="$CALL --url 'https://my/url'"
CALL="$CALL --config '${REFCONF}'"
CALL="$CALL --css '${REFCSS}'"
CALL="$CALL --output '${DOCX_BUILDDIR}/apidoc/${DOCX_DOCNAME}/apiref' "

if((DOCX_VERBOSE > 1));then
	for((i=0;i<DOCX_VERBOSE;i++));do
		CALL="$CALL -v "
	done
fi

CALL="$CALL $@"

if [ ! -e "${DOCX_BUILDDIR}/sphinx/apidoc/apiref" ];then
	mkdir -p "${DOCX_BUILDDIR}/sphinx/apidoc/apiref"
fi

if((DOCX_VERBOSE > 1));then
	echo
	echo "${0##*/}:Call: $CALL"
	echo
fi


eval $CALL

echo

