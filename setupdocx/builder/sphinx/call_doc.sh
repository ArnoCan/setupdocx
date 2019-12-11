PROJECT='setupdocx'
VERSION=${DOCX_VERSION:-`date +%Y.%m.%d`}
RELEASE=${DOCX_RELEASE:-$VERSION}
AUTHOR='Arno-Can Uestuensoez'
COPYRIGHT='Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez'
LICENSE='Artistic-License-2.0 + Forced-Fairplay-Constraints'
STATUS='beta'
MISSION='Support extensions for setuptools / distutils.'
BUILDDATE=`date`

DOCX_DEBUG=${DOCX_DEBUG:-0}
DOCX_VERBOSE=${DOCX_VERBOSE:-0}
DOCX_QUIET=${DOCX_QUIET:-0}


# the absolute pathname for this source
MYPATH="${BASH_SOURCE%/*}/"
if [ "X${MYPATH#.}" != "X$MYPATH" ];then
	MYPATH="${PWD}/${MYPATH#.}";MYPATH="${MYPATH//\/\//\/}"
fi

#
# library with generic functions
#
MYLIB=${MYPATH%/*/*/}/
source ${MYLIB}libbash.sh

display 1 0 "Wrapper started..."

if((DOCX_QUIET == 0));then
	cat <<EOF

################################################################
#                                                              #
# WRAPPER = call_doc.sh                                        #
$(printf "# PROJECT = %-51s#" $PROJECT)
#                                                              #
# Create documentation - default: sphinx                       #
#                                                              #
################################################################
#
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
EOF
fi

display_state 1 1
if [ $? -ne 0 ];then
	IFSO=$IFS
	IFS=':'
	_F=0
	for p in ${PATH};do
		if((_F==0));then
			_F=1
			echo "#   PATH                  = '$p'"
		else
			echo "#                         : '$p'"
		fi
	done

	echo "#"

	_F=0
	for p in ${PYTHONPATH};do
		if((_F==0));then
			_F=1
			echo "#   PYTHONPATH            = '$p'"
		else
			echo "#                         : '$p'"
		fi
	done

	echo "#"
	echo "#   MYPATH                = '$MYPATH'"
	echo "#   INDIR                 = '$INDIR'"
	echo "#"
	
	IFS=$IFSO
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
	exec_call mkdir -p "${DOCX_BUILDDIR}"
fi
export PYTHONPATH="$PWD:$PYTHONPATH"

# document source directory
DOCX_DOCSRC="${DOCX_DOCSRC:-docsrc}"
DOCX_DOCSRC="${DOCX_DOCSRC%%/}"
DOCX_INDEXSRC="${DOCX_INDEXSRC:-$DOCX_DOCSRC/index.rst}"

# document source directory
DOCX_DOCNAME="${DOCX_DOCNAME:-$PROJECT}"

DOCX_DOCTEMPLATE=${DOCX_DOCTEMPLATE:-default}
DOCX_DOCTYPE=${DOCX_DOCTYPE:-html}

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
#   DOCX_BUILDER          = '$DOCX_BUILDER'"
#   DOCX_BUILDRELDIR      = '$DOCX_BUILDRELDIR'"
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
			echo "#   PATH                  = '$p'"
		else
			echo "#                         : '$p'"
		fi
	done

	echo "#"

	_F=0
	for p in ${PYTHONPATH};do
		if((_F==0));then
			_F=1
			echo "#   PYTHONPATH            = '$p'"
		else
			echo "#                         : '$p'"
		fi
	done

	echo "#"
	echo "#   MYPATH                = '$MYPATH'"
	echo "#   INDIR                 = '$INDIR'"
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

#
# *** start exec ***
#

RES=0

# map virtual types to real builder
if [ "X${DOCX_DOCTYPE,,}" == "Xpdf" ];then
	_BUILDER=latexpdf
	_BUILDOUT=latex
else
	_BUILDER=$DOCX_DOCTYPE
	_BUILDOUT=$DOCX_DOCTYPE
fi

# the complete build path
BUILDPATH="${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}/"

# import directory for entries of static reference
STATIC="${BUILDPATH}/_static"

# import manually edited documents
#
display_state 1 3
_STATE=$?
{
	display 0 0 EMPTYLINE
	if [ ! -e "${BUILDPATH}" ];then
		exec_call mkdir -p "${BUILDPATH}";	
	fi 

	if [ "X${DOCX_RAWDOC}" == "X1" ]; then
		display 0 0 "Using generated raw documents only."
	else
		if [ -d "${DOCX_LIB}/config/sphinx/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/" ];then
			display " "
	        display 0 0 EMPTYLINE 
			display 0 0 "copy generic default configuration files:";
	        display 0 0 EMPTYLINE 
			IFSO=$IFS
			IFS='
'
			for d in ${DOCX_LIB}/config/sphinx/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/*;do
				IFS=$IFSO
				exec_call cp -a "${d}" "${BUILDPATH}"; 
			done
			IFS=$IFSO
		fi

		if [ -d "${DOCX_DOCSRC}/config/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/" ];then
			display " "
	        display 0 0 EMPTYLINE 
			display 0 0 "copy default document configuration files:"; 
	        display 0 0 EMPTYLINE 
			IFSO=$IFS
			IFS='
'
			for d in ${DOCX_DOCSRC}/config/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/*;do
				IFS=$IFSO
				exec_call cp -a "${d}" "${BUILDPATH}"; 
			done
			IFS=$IFSO
		fi	

		display " "
		display 0 0 EMPTYLINE 
        display 0 0 "copy document files from ${DOCX_DOCSRC}"; 
		display 0 0 EMPTYLINE 
		IFSO=$IFS
		IFS='
'
		for d in `find "${DOCX_DOCSRC}" -type f -name '*.rst' | sed 's|^'"${DOCX_DOCSRC}"'/*||'`;do
			IFS=$IFSO
			dx=${d%/*} 
			if [ "X$dx" == "X$d" ];then
				dx=''
			fi
			
			if [ ! -e "${BUILDPATH}${dx}" ];then
				exec_call mkdir -p "${BUILDPATH}${dx}";	
			fi 
			exec_call cp -a "${DOCX_DOCSRC}/$d" "${BUILDPATH}${dx}/"; 
		done
		IFS=$IFSO

		# put the docs together
		display " "
		display 0 0 EMPTYLINE
        display 0 0 "copy index"; 
		display 0 0 EMPTYLINE
		if [ "X${DOCX_INDEXSRC}" != "X" ];then
			if [ -e "${DOCX_INDEXSRC}" ]; then
				exec_call cp "${DOCX_INDEXSRC}" "${BUILDPATH}index.rst"
			else
				display WARNING 1 "Cannot find index file for patch: \"${DOCX_INDEXSRC}\"" >&2
			fi
		fi

		display " "
		display 0 0 EMPTYLINE
	    display 0 0 "copy static literal data"; 
		display 0 0 EMPTYLINE
		if [ ! -e "${STATIC}" ];then
			exec_call mkdir -p "${STATIC}";
		fi
	
		#
		# copy _static from source directory
		#
		display " "
		display 0 0 EMPTYLINE
	    display 0 0 "copy _static from source directory"; 
		display 0 0 EMPTYLINE
		IFSO=$IFS
		IFS='
'
		for d in ${DOCX_DOCSRC}/_static/*;do
			IFS=$IFSO
			exec_call cp -pPr "${d}" "${STATIC}";
		done
		IFS=$IFSO


		#
		# copy finally the adapted configuration files from configdir 
		#
		display " "
		display 0 0 EMPTYLINE
	    display 0 0 "copy finally the adapted configuration files from custom configdir:"; 
	    display 0 0 "    ${DOCX_CONFIGPATH}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/"; 
	    display 0 0 "    DOCX_CONFIGPATH  = ${DOCX_CONFIGPATH}"; 
	    display 0 0 "    DOCX_DOCTEMPLATE = ${DOCX_DOCTEMPLATE}"; 
	    display 0 0 "    DOCX_DOCTYPE     = ${DOCX_DOCTYPE}"; 
		display 0 0 EMPTYLINE
		IFSO=$IFS
		IFS='
'
		for d in ${DOCX_CONFIGPATH}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/*;do
			IFS=$IFSO
			exec_call cp -pPr "${d}" "${BUILDPATH}";
		done
		IFS=$IFSO
	fi 

	echo __REGULAREND__
} | \
awk -v state=_STATE '/__REGULAREND__/{regend=1;}and(state, 6){print;}END{if(regend!=1){exit 1;}}'
_EXIT=$?
if [ $_EXIT -ne 0 ];then
	display ERROR $_EXIT "prepare document build input"
	exit $_EXIT
fi


#{
#cat <<EOF
#**Product Data**
#
#* PROJECT=${DOCX_NAME}
#
#* MISSION=${MISSION}
#
#* AUTHOR=${AUTHOR}
#
#* COPYRIGHT=${COPYRIGHT}
#
#* LICENSE=${LICENSE}
#
#* VERSION=${DOCX_VERSION}
#
#* RELEASE=${DOCX_RELEASE}
#
#* STATUS=${STATUS}
#
#* BUILDDATE=${BUILDDATE}
#
#EOF
#} > "${BUILDPATH}project.rst"

CALL=" "
#FIXME: see BUILDEXEC  
CALL="export SPHINXBUILD=sphinx-build; "
# CALL="export SPHINXBUILD=sphinx-build-3; "

CALL="$CALL cd ${BUILDPATH};"
CALL="$CALL export PYTHONPATH=$PWD:$PYTHONPATH;"

#
# cp makefiles
#
display 0 0 EMPTYLINE
display 0 0 "copy makefiles into build directory"; 
exec_call cp -pPr "${MYPATH}/Makefile_docx" "${BUILDPATH}";
exec_call cp -pPr "${MYPATH}/make_docx.bat" "${BUILDPATH}";
display 0 0 EMPTYLINE 

DOMAKE=" make -f Makefile_docx "
# cleanup build history
if [ "X$DOCX_CLEAN" == "X1" ];then
	pushd ${BUILDPATH}
	display 1 4 "In directory: ${PWD}"
	display 1 1 "${DOMAKE} clean"				
	exec_call ${DOMAKE} clean;
	popd
fi
display 0 0 EMPTYLINE 

# use for direct sphinx-build
#for((i=0;i<DOCX_VERBOSEX;i++));do
#	CALL="$CALL -v "
#done

# set verbosity
for((i=0;i<DOCX_VERBOSEX;i++));do
	SPOPTS+=" -v "
done

if [ "X$DOCX_CLEAN" == "X1" ];then
	SPOPTS+=" -E "
	SPOPTS+=" -a "
fi

#if [ "X${SPOPTS// /}" != "X" ];then
#	CALL="$CALL make ${_BUILDER} SPHINXOPTS='${SPOPTS}';"
#else
#	CALL="$CALL make ${_BUILDER};"
#fi

#FIXME: BUILDEXEC="sphinx-build "
# 
BUILDEXEC="sphinx-build "
# 
# BUILDEXEC="sphinx-build-2 "
# BUILDEXEC="sphinx-build-3 "

# BUILDEXEC+=" -P "


if((DOCX_VERBOSE > 6));then
	# due to some odd behaviour of sphinx-build more '-v' has to be provided manually
	for((vx=DOCX_VERBOSE;vx > 0;vx-=1));do BUILDEXEC+=" -v "; done 
fi

#
#TODO:
# not documenteddoes not works s.time... - for now not highest priority to provide a public solution
# see make-call for developer: BUILDEXEC+=" -M '${_BUILDER}' "
case ${_BUILDER} in
	latexpdf)
		BUILDEXEC+=" -M '${_BUILDER}' ";
		_EXTRASUB=latexpdf/;;
	latexpdfja)
		BUILDEXEC+=" -M '${_BUILDER}' ";
		_EXTRASUB=latexpdfja/;;
	*)  BUILDEXEC+=" -b '${_BUILDER}' ";
		_EXTRASUB='';;
esac


#BUILDEXEC+=" -c '${DOCX_CONFIGPATH}/docsrc' "


BUILDEXEC+=" . _build/'${_BUILDOUT}'  ${SPOPTS}"
CALL="$CALL ${BUILDEXEC};"
# CALL="$CALL sphinx-build -M ${_BUILDER} . _build  ${SPOPTS};"
#	@$(BUILDDOC) -M $@ "." "_build" $(BUILDDOCOPTS)

# reminder for further study
# SPHINXOPTS+=" -E "
# CALL="$CALL make ${_BUILDER} SPHINXOPTS='${SPHINXOPTS}';"


CALL="$CALL cd - "

display_state 1 1
_STATE=$?
if((_STATE&6));then
	cat <<EOF
#
# call";
#   CWD=${PWD}";
#   ${BUILDEXEC}";
#   #>>>
EOF
fi

display_state 1 2
_STATE=$?
if((_STATE&7));then
	cat <<EOF
#
# call ${BUILDEXEC}";
#    $CALL
# proceed";
#
EOF
fi
exec_call $CALL
RESULT=$?
let RES+=1;
if((_STATE&7));then
	echo "   #<<<";
	echo
fi


#
# copy to transfer directory - within build/doc
#
display_state 1 1
_STATE=$?
if((_STATE&7));then
	display "#"
	display "# copy";
	display "#    from: ${BUILDPATH}_build/${_BUILDOUT}";
	display "#    to:   ${DOCX_BUILDDIR}doc/${DOCX_DOCNAME}";
	display "#"
fi

display_state 1 1
_STATE=$?
{
	if [ -e "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}" ];then
		exec_call rm -rf "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/*"
	else
		exec_call mkdir -p "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}"
	fi
} | \
if((_STATE & 6));then
	cat
else
	cat > /dev/null
fi


display "Results of BUILDER=${_BUILDER,,}"
_B=${_BUILDER,,}
display_state 1 1
_STATE=$?

#
#TODO: eventually fix the imported structure
#
#  1. using 'sphinx-build -M latexpdf(ja)' -> creates: $_BUILDOUT/$_BUILDOUT/
#  2. using 'sphinx-build -b <else>)'      -> creates: $_BUILDOUT/
#
#  the second 2. seems more accurate, but fails for latex...
#  while 1. fails for man...
#
#  :-) ...for now using both:
#  1. for PDF
#     for now use a double-subdir in order to safely avoid interference of metadata
#     for successive builds of different document types
#     this could becomee likely when different patch patterns of content are required
#     _BUILDOUT and DOCX_DOCTYPE are not in any case the same strings here
#     so not for latexpdf vs. pdf
#  2. for others
#
case ${_B} in
	html|singlehtml)
		{
			if [ -e "${BUILDPATH}_build/${_BUILDOUT}" ];then
				exec_call cp -pPr "${BUILDPATH}_build/${_BUILDOUT}/${_EXTRASUB}"* "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/"
			fi
		
			# quick-fix for missing custom.css, and ev. others
			if [ -e "${STATIC}" ];then
				exec_call cp -pPr "${STATIC}" "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/"
			fi
		}
		;;

	latexpdf|latexpdfja)
		{
			if [ -e "${BUILDPATH}_build/${_BUILDOUT}" ];then
				exec_call cp -pPr "${BUILDPATH}_build/${_BUILDOUT}/${_EXTRASUB}"*.pdf "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/"
			fi
		}
		;;

	epub)
		{
			if [ -e "${BUILDPATH}_build/${_BUILDOUT}" ];then
				exec_call cp -pPr "${BUILDPATH}_build/${_BUILDOUT}/${_EXTRASUB}"*.epub "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/"
			fi
		}
		;;

	man)
		{
			if [ -e "${BUILDPATH}_build/${_BUILDOUT}" ];then
				# do not want the intermediate data of applied tools 
				exec_call cp -pPr "${BUILDPATH}_build/${_BUILDOUT}/${_EXTRASUB}"*.* "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/"
			fi
		}
		;;

	*)
		{
			if [ -e "${BUILDPATH}_build/${_BUILDOUT}" ];then

				exec_call cp -pPr "${BUILDPATH}_build/${_BUILDOUT}/${_EXTRASUB}"* "${DOCX_BUILDDIR}/doc/${DOCX_DOCNAME}/"
			fi
		}
		;;
			
esac | \
if((_STATE & 6));then
	cat
else
	cat > /dev/null
fi

display 0 0 EMPTYLINE

exit $RESULT


#
# editedcheck: 20191128520340
#
