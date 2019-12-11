PROJECT='setupdocx'
VERSION=${DOCX_VERSION:-`date +%Y.%m.%d`}
RELEASE=${DOCX_RELEASE:-$VERSION}
AUTHOR='Arno-Can Uestuensoez'
COPYRIGHT='Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
LICENSE='Artistic-License-2.0 + Forced-Fairplay-Constraints'
STATUS='beta'
MISSION='Support API documentation extensions for setuptools / distutils.'
BUILDDATE=`date`


# the absolute pathname for this source
MYPATH="${BASH_SOURCE%/*}/"
if [ "X${MYPATH#.}" != "X$MYPATH" ];then
	MYPATH="${PWD}/${MYPATH#.}";MYPATH="${MYPATH//\/\//\/}"
fi

MYLIB=${MYPATH%/*/*/}/
source ${MYLIB}libbash.sh


if((DOCX_QUIET == 0));then
	cat <<EOF

################################################################
#                                                              #
# WRAPPER = call_apidoc.sh                                     #
$(printf "# PROJECT = %-51s#" $PROJECT)
#                                                              #
# Generate API documentation - default: sphinx-apidoc          #
#                                                              #
################################################################

EOF
fi

display_state 1 1
if [ $? -ne 0 ];then
cat <<EOF
#
# ${0##*/}:Called:
#   $0 $@
#
# ${0##*/}:Input Environ Options:
#   DOCX_APIDOC           = '$DOCX_APIDOC'
#   DOCX_APIREF           = '$DOCX_APIREF'
#   DOCX_AUTHOR           = '$DOCX_AUTHOR'
#   DOCX_BUILDDIR         = '$DOCX_BUILDDIR'
#   DOCX_BUILDER          = '$DOCX_BUILDER'
#   DOCX_BUILDRELDIR      = '$DOCX_BUILDRELDIR'
#   DOCX_CLEAN            = '$DOCX_CLEAN'
#   DOCX_CONFIGPATH       = '$DOCX_CONFIGPATH'
#   DOCX_COPYRIGHT        = '$DOCX_COPYRIGHT'
#   DOCX_DEBUG            = '$DOCX_DEBUG'
#   DOCX_DOCNAME          = '$DOCX_DOCNAME'
#   DOCX_DOCSRC           = '$DOCX_DOCSRC'
#   DOCX_DOCTEMPLATE      = '$DOCX_DOCTEMPLATE'
#   DOCX_DOCTYPE          = '$DOCX_DOCTYPE'
#   DOCX_EMBED            = '$DOCX_EMBED'
#   DOCX_INDEXSRC         = '$DOCX_INDEXSRC'
#   DOCX_LIB              = '$DOCX_LIB'
#   DOCX_LICENSE          = '$DOCX_LICENSE'
#   DOCX_MISSION          = '$DOCX_MISSION'
#   DOCX_NAME             = '$DOCX_NAME'
#   DOCX_NOEXEC           = '$DOCX_NOEXEC'
#   DOCX_QUIET            = '$DOCX_QUIET'
#   DOCX_RAWDOC           = '$DOCX_RAWDOC'
#   DOCX_RELEASE          = '$DOCX_RELEASE'
#   DOCX_SRCDIR           = '$DOCX_SRCDIR'
#   DOCX_STATUS           = '$DOCX_STATUS'
#   DOCX_VERBOSE          = '$DOCX_VERBOSE'
#   DOCX_VERBOSEX         = '$DOCX_VERBOSEX'
#   DOCX_VERSION          = '$DOCX_VERSION'
#
#   PATH                  = '$PATH'
#
#   PYTHONPATH            = '$PYTHONPATH'
#
#   MYPATH                = '$MYPATH'
#   INDIR                 = '$INDIR'
#
EOF
fi


#----------------------------
#*** command line options *** 
#----------------------------
#
# Extract and optionally filter out known command line options of the wrapper.
# Non-filtered options are transparently passed as appendix to the executable
# anyhow, the executable should be instrumented only via DOCX_EXECOPTS
# see also DOCX_EXECOPTS_RESET.
for x in $@;do
	case $x in
		-v|--verbose)let DOCX_VERBOSE+=1;shift;;
		-d|--debug)let DOCX_DEBUG+=1;shift;;
	esac
	if((DOCX_VERBOSE > 0 || DOCX_DEBUG > 0));then
		# trace it as interface
		echo "got commandline option: $x"
	fi
done

# input base directory
INDIR="${INDIR:-$PWD}"
if [ "X${INDIR#.}" != "X$INDIR" ];then
	INDIR="${PWD}/${INDIR#.}";INDIR="${INDIR//\/\//\/}"
fi
INDIR="${INDIR}/"

# builder - for casual readout, even though defined by directory
DOCX_BUILDER="${DOCX_BUILDER:-sphinx}"

# output base directory
DOCX_BUILDDIR="${DOCX_BUILDDIR:-build}/"
if [ ! -e "${DOCX_BUILDDIR}" ];then
	exec_call mkdir -p "${DOCX_BUILDDIR}"
fi
if [ "X${DOCX_BUILDDIR#/}" != "X${DOCX_BUILDDIR}" ];then
	DOCX_BUILDDIR_ABS="${DOCX_BUILDDIR}"
else
	DOCX_BUILDDIR_ABS="${PWD}/${DOCX_BUILDDIR_ABS#.}";DOCX_BUILDDIR_ABS="${DOCX_BUILDDIR_ABS//\/\//\/}"
fi
export PYTHONPATH="$PWD:$PYTHONPATH"

# document source directory
DOCX_DOCSRC="${DOCX_DOCSRC:-docsrc}"
DOCX_DOCSRC="${DOCX_DOCSRC%%/}"


# document source directory
DOCX_DOCNAME="${DOCX_DOCNAME:-$PROJECT}"

# executable
DOCX_EXEC=${DOCX_EXEC:-sphinx-apidoc}

# alternate appearance
DOCX_DOCTEMPLATE=${DOCX_DOCTEMPLATE:-default}
DOCX_DOCTYPE="${DOCX_DOCTYPE:-html}"


DOCX_VERBOSE=${DOCX_VERBOSE:-0}


display_state 2 2
if [ $? -ne 0 ];then
	cat <<EOF
#
# ${0##*/}:Called:"
#   $0 $@"
#
# ${0##*/}:Input Environ Options:"
#   DOCX_APIDOC           = '$DOCX_APIDOC'"
#   DOCX_APIREF           = '$DOCX_APIREF'"
#   DOCX_AUTHOR           = '$DOCX_AUTHOR'"
#   DOCX_BUILDDIR         = '$DOCX_BUILDDIR'"
#   DOCX_BUILDER          = '$DOCX_BUILDER'
#   DOCX_BUILDRELDIR      = '$DOCX_BUILDDIR'"
#   DOCX_CLEAN            = '$DOCX_CLEAN'"
#   DOCX_CONFIGPATH       = '$DOCX_CONFIGPATH'"
#   DOCX_COPYRIGHT        = '$DOCX_COPYRIGHT'"
#   DOCX_DEBUG            = '$DOCX_DEBUG'"
#   DOCX_DOCNAME          = '$DOCX_DOCNAME'"
#   DOCX_DOCSRC           = '$DOCX_DOCSRC'"
#   DOCX_DOCTYPE          = '$DOCX_DOCTYPE'"
#   DOCX_DOCTEMPLATE      = '$DOCX_DOCTEMPLATE'"
#   DOCX_EMBED            = '$DOCX_EMBED'"
#   DOCX_INDEXSRC         = '$DOCX_INDEXSRC'"
#   DOCX_LIB              = '$DOCX_LIB'"
#   DOCX_LICENSE          = '$DOCX_LICENSE'"
#   DOCX_MISSION          = '$DOCX_MISSION'"
#   DOCX_NAME             = '$DOCX_NAME'"
#   DOCX_NOEXEC           = '$DOCX_NOEXEC'"
#   DOCX_QUIET            = '$DOCX_QUIET'"
#   DOCX_RAWDOC           = '$DOCX_RAWDOC'"
#   DOCX_RELEASE          = '$DOCX_RELEASE'"
#   DOCX_SRCDIR           = '$DOCX_SRCDIR'"
#   DOCX_STATUS           = '$DOCX_STATUS'"
#   DOCX_VERBOSE          = '$DOCX_VERBOSE'"
#   DOCX_VERBOSEX         = '$DOCX_VERBOSEX'"
#   DOCX_VERSION          = '$DOCX_VERSION'"	
#
EOF
fi

display_state 2 2
if [ $? -ne 0 ];then
	IFSO=$IFS
	IFS=':'
	_F=0
	for p in ${PATH};do
		if((_F==0));then
			_F=1
			echo "#  PATH                    = '$p'"
		else
			echo "#                          : '$p'"
		fi
	done

	echo "#"

	_F=0
	for p in ${PYTHONPATH};do
		if((_F==0));then
			_F=1
			echo "#  PYTHONPATH              = '$p'"
		else
			echo "#                          : '$p'"
		fi
	done

	echo "#"
	echo "#  MYPATH                  = '$MYPATH'"
	echo "#  INDIR                   = '$INDIR'"
	echo "#"
	
	IFS=$IFSO
fi

display_state 4 4
if [ $? -ne 0 ];then
	cat <<EOF
#   PATH                   = '$PATH'"
#
#   PYTHONPATH             = '$PYTHONPATH'"
#
#   MYPATH                 = '$MYPATH'"
#   INDIR                  = '$INDIR'"
#
EOF
fi


## input base directory
#INDIR="${INDIR:-$PWD}"
#if [ "X${INDIR#.}" != "X$INDIR" ];then
#	INDIR="${PWD}/${INDIR#.}";INDIR="${INDIR//\/\//\/}"
#fi
#INDIR="${INDIR}/"
#
## output base directory
#DOCX_BUILDDIR="${DOCX_BUILDDIR:-build}/"
#if [ ! -e "${DOCX_BUILDDIR}" ];then
#	exec_call mkdir -p "${DOCX_BUILDDIR}"
#fi
#export PYTHONPATH="$PWD:$PYTHONPATH"
#
## document source directory
#DOCX_DOCSRC="${DOCX_DOCSRC:-docsrc}"
#DOCX_DOCSRC="${DOCX_DOCSRC%%/}"
#
#
## document source directory
#DOCX_DOCNAME="${DOCX_DOCNAME:-$PROJECT}"
#
## decide to create an embedded subdocument or a standalone document 
#DOCX_EMBED="${DOCX_EMBED:-}"
#
#DOCX_DEBUG=${DOCX_DEBUG:-0}
#DOCX_VERBOSE=${DOCX_VERBOSE:-1}  # 0 is QUIET



#
# *** start exec ***
#

# import directory for entries of static reference
STATIC="${DOCX_BUILDDIR}/sphinx/apidoc/_static"

# the complete build path
BUILDPATH="${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}/"

# source entities
FILEDIRS=""
if [ "X${DOCX_SRCDIR}" != "X" ];then
	OIFS=$IFS
	IFS='
'
	for f in ${DOCX_SRCDIR//\;/$IFS};do
		FILEDIRS+=" ${INDIR}${f}"
	done
	IFS=$OIFS
else
	FILEDIRS+=" ${INDIR}setupdocx"
fi

# map virtual types to real builder
DOCX_DOCTYPE=${DOCX_DOCTYPE:-html}
case ${DOCX_DOCTYPE,,} in
	auto) _BUILDER=pdf; _BUILDOUT=auto;;
	pdflatex) _BUILDER=pdf; _BUILDOUT=pdflatex;;
	latexpdf) _BUILDER=pdf; _BUILDOUT=latex;;
	*) _BUILDER=$DOCX_DOCTYPE; _BUILDOUT=$DOCX_DOCTYPE;;
esac


#
# used common directories
#
if [ "X$DOCX_EMBED" == "X1" ]; then
	_CONFDIR="${DOCX_CONFIGPATH}"
	_LIBDIR="${DOCX_LIB}/config/epydoc/"
	_BUILDDIR="${DOCX_BUILDDIR}/epydoc/apiref/"
	_OUTDIR="${DOCX_BUILDDIR}/epydoc/apiref/_build/${_BUILDER}/"
	_DOCDIR="${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/apiref/"
else
	_CONFDIR="${DOCX_CONFIGPATH}"
	_LIBDIR="${DOCX_LIB}/config/epydoc/"
	_BUILDDIR="${DOCX_BUILDDIR}/epydoc/apiref/"
	_OUTDIR="${DOCX_BUILDDIR}/epydoc/apiref/_build/${_BUILDER}/"
	_DOCDIR="${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/"
fi

#
# main configuration
#
REFCONF="${_BUILDDIR}epydoc.conf"
REFCSS="${_BUILDDIR}epydoc.css"
display 2 2 "REFCONF=${REFCONF}"
display 2 2 "REFCSS=${REFCSS}"


# import manually edited documents
#
display_state 1 3
_STATE=$?
{
	if [ ! -e "${_OUTDIR}" ];then
		exec_call mkdir -p "${_OUTDIR}"
	fi
	
	display "#"
	if [ "X${DOCX_RAWDOC}" == "X1" ]; then
		display 0 0 "${0##*/}:Using generated raw documents only."
	else
		display " "
        display 0 0 EMPTYLINE 
		display 0 0 "copy common files from ${_LIBDIR}";
        display 0 0 EMPTYLINE 
		IFSO=$IFS
		IFS='
'
		for d in ${_LIBDIR}*;do
			exec_call cp -pPr "${d}" "${_BUILDDIR}"; 
		done
		IFS=$IFSO


		#
		# copy finally the adapted configuration files from configdir 
		#
		display "#"
	    display 0 0 "copy finally the adapted configuration files from configdir"; 
		IFSO=$IFS
		IFS='
'
		for d in ${_CONFDIR}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/*;do
			exec_call cp -pPr "${d}" "${_BUILDDIR}"; 
		done
		IFS=$IFSO

	fi 
	echo __REGULAREND__
} | \
awk -v state=_STATE '/__REGULAREND__/{regend=1;}and(state, 6){print;}END{if(regend!=1){exit 1;}}'
_EXIT=$?
if [ $_EXIT -ne 0 ];then
	display ERROR $_EXIT "prepare document build input failed:$_EXIT"
	exit $_EXIT
fi


#
# assembly of the actual call
#
display 1 1 "assemble call"; 

#CALL=""
#CALL="$CALL export PYTHONPATH=$PWD:$PYTHONPATH;"
#CALL="$CALL $DOCX_EXEC "
#if((DOCX_EXECOPTS_RESET == 0));then
#	CALL="$CALL -A '$AUTHOR'"
#	CALL="$CALL -H '$PROJECT'"
#	CALL="$CALL -V '$VERSION'"
#	CALL="$CALL -R '$RELEASE'"
#	CALL="$CALL -o ${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}"
#
#	CALL="$CALL -f "
#	CALL="$CALL -M "
#	CALL="$CALL -d 5 "
#	CALL="$CALL -e "
#
#	if((DOCX_GENDOC > 0));then
#		CALL="$CALL -F "
#	fi
#
#fi


CALL=""
CALL="$CALL export PYTHONPATH=$PWD:$PYTHONPATH;"
CALL="$CALL epydoc "
CALL="$CALL --${_BUILDER} "
case ${_BUILDOUT} in
	auto) CALL="$CALL --pdfdriver=auto ";;
	pdflatex) CALL="$CALL --pdfdriver=pdflatex ";;
	latexpdf) CALL="$CALL --pdfdriver=latex ";;
esac

CALL="$CALL --name '${DOCX_NAME}'"
# CALL="$CALL --url 'https://my/url'"  # to be set in epydoc.conf
CALL="$CALL --config '${REFCONF}'"     
CALL="$CALL --css '${REFCSS}'"         # must not set in epydoc.conf

if((DOCX_RAWDOC == 1));then
	CALL="$CALL --output '${_OUTDIR}' "  # must not set in epydoc.conf
else
	CALL="$CALL --output '${_OUTDIR}' "  # must not set in epydoc.conf
fi

for((i=0;i<DOCX_VERBOSEX;i++));do
	CALL="$CALL -v "
done
for((i=0;i<DOCX_DEBUG;i++));do
	CALL="$CALL --debug "
done
CALL="$CALL $@"

if [ ! -e "${_BUILDDIR}" ];then
	exec_call mkdir -p "${_BUILDDIR}";	
fi

display_state 3 3
_STATE=$?
if((_STATE&7));then
	display 0 0 EMPTYLINE
	display 0 0 "Call:"
	display 0 0 "  $CALL"
	display 0 0 EMPTYLINE
else
	display_state 1 1
	_STATE=$?
	if((_STATE&7));then
		display 0 0 EMPTYLINE
		display 0 0 "Call: external tools"
		display 0 0 "  epydoc"
		display 0 0 EMPTYLINE
	fi
fi


exec_call $CALL
RESULT=$?

display 0 0 EMPTYLINE
if [ ! -e "${_DOCDIR}" ];then
	exec_call mkdir -p "${_DOCDIR}"
fi

display 0 0 "Results of BUILDER=${_BUILDER,,}"
display_state 3 3
_STATE=$?
case ${_BUILDER,,} in
	html)
		{
			if [ -e "${_OUTDIR}" ];then
				exec_call cp -pPr "${_OUTDIR}*" "${_DOCDIR}"
			fi
		}
		;;

	pdf)
		{
			if [ -e "${_OUTDIR}" ];then
				exec_call cp -pPr "${_OUTDIR}*.pdf" "${_DOCDIR}${DOCX_DOCNAME}.pdf"
			fi
		}
		;;

	*)
		display 0 0"Document type not supported: $_BUILDER" >&2
		;;
		
esac | \
if((_STATE&7));then
	cat
else
	cat > /dev/null
fi

display " "
if((RESULT==0));then
	# post patches

	#
    # copy post-creation patches 
	#
	_FROM_PATCH=${_CONFDIR}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc_post/apiref/
	if [ -e "${_FROM_PATCH}" ]; then
		display " "
		display 0 0 EMPTYLINE 
	    display 0 0 "copy post-creation document patches from ${_FROM_PATCH}"; 
		display 0 0 EMPTYLINE 
		IFSO=$IFS
		IFS='
	'
		for d in `find "${_FROM_PATCH}" -type f | sed 's|^'"${_FROM_PATCH}"'/*||'`;do
			IFS=$IFSO
			dx=${d%/*} 
			if [ "X$dx" == "X$d" ];then
				dx=''
			fi
			
			if [ ! -e "${_DOCDIR}${dx}" ];then
				exec_call mkdir -p "${_DOCDIR}${dx}";	
			fi 
			exec_call cp -pPR "${_FROM_PATCH}/$d" "${_DOCDIR}${dx}/"; 
		done
		IFS=$IFSO
	fi	
fi
display " "

exit $RESULT

#
# editedcheck: 20191128530323
#
