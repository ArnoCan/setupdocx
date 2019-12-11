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

CALL=""
CALL="$CALL export PYTHONPATH=$PWD:$PYTHONPATH;"
CALL="$CALL $DOCX_EXEC "
if((DOCX_EXECOPTS_RESET == 0));then
	CALL="$CALL -A '$AUTHOR'"
	CALL="$CALL -H '$PROJECT'"
	CALL="$CALL -V '$VERSION'"
	CALL="$CALL -R '$RELEASE'"
	CALL="$CALL -o ${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}"

	CALL="$CALL -f "
	CALL="$CALL -M "
	CALL="$CALL -d 5 "
	CALL="$CALL -e "

	if((DOCX_GENDOC > 0));then
		CALL="$CALL -F "
	fi

fi


#
# clear options
#
if((DOCX_EXECOPTS_RESET != 0));then
	# remaining options are by default passed to the exec-call, 
	# thus suppressed here for reset
	CALL="$CALL $@"
fi


#
# append extra options
#
CALL="$CALL ${DOCX_EXECOPTS} "

EXCLUDE="  "

RES=0


#
# generate final API documentation 
#
if((RES==0 && DOCX_GENDOC>0));then
	if [ "X${DOCX_TEMPLATE}" != "X" ];then
	SPHINXOPTS+=" -c ${DOCX_CONFIGPATH}/${DOCX_BUILDER}/${DOCX_TEMPLATE}/${DOCX_DOCTYPE}/docsrc"
	fi
fi


#
#build=patches
DOCHTMLDIR="${DOCX_BUILDDIR}sphinx/apidoc/_build/"
DOCHTML="${DOCHTMLDIR}html/index.html"

IFSO=$IFS
IFS=';'
FX=( ${FILEDIRS} )
IFS=$IFSO
for fx in ${FX[@]};do
	if((DOCX_DEBUG > 0));then
		echo "${0##*/}:EXECUTABLE = '$(which ${DOCX_EXEC})'"
		echo "${0##*/}:SOURCE-DIR = '$fx'"
		echo
		echo "${0##*/}:CALL       = <$CALL '$fx' '${EXCLUDE}'>"
	elif((DOCX_VERBOSE > 2));then
		echo "${0##*/}:EXECUTABLE = '$(which ${DOCX_EXEC})'"
		echo "${0##*/}:SOURCE-DIR = '$fx'"
		echo

		IFSO=$IFS
		IFS=';'
		_F=0
		for p in ${CALL};do
			if((_F==0));then
				_F=1
				echo "  CALL                    = '$p'"
			else
				echo "                          ; '$p'"
			fi
		done
		echo "                            '$fx'"
		echo "                            '${EXCLUDE}'"
		echo

		IFS=$IFSO

	elif((DOCX_VERBOSE > 1));then
		echo "${0##*/}:EXECUTABLE = '${DOCX_EXEC}'"
		_f=${fx::-1}
		echo "${0##*/}:SOURCE-DIR = '${_f##*/}'"
	fi

	if((DOCX_NOEXEC == 1));then
		echo "$CALL $fx ${EXCLUDE}"
		RES=0;

	else
		echo
		echo "${0##*/}:Calling executable sphinx-apidoc"
		eval $CALL "$fx" "${EXCLUDE}"
		RES=$?;
		if((RES==0 && DOCX_GENDOC>0));then
			
			if [ "X${DOCX_RAWDOC}" == "X1" ]; then
				display 0 0 "Using generated raw documents only."
			else
				# import manually edited documents
				#
				display_state 1 3
				_STATE=$?
				{
echo "4TEST:$LINENO:${DOCX_LIB}/config/sphinx/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/" >&2
					display 0 0 EMPTYLINE
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
				
echo "4TEST:$LINENO:${DOCX_DOCSRC}/config/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/" >&2
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
				
				
					# put the docs together
echo "4TEST:$LINENO:${DOCX_INDEXSRC}" >&2
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
					# copy finally the adapted configuration files from configdir 
					#

echo "4TEST:$LINENO:${DOCX_CONFIGPATH}/${DOCX_BUILDER}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc" >&2

					for cp in ${DOCX_CONFIGPATH//:/ };do

echo "4TEST:$LINENO:${cp}" >&2
						
						if [ -e "${cp}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc" ];then
							display " "
							display 0 0 EMPTYLINE
						    display 0 0 "copy finally the adapted configuration files from custom configdir:"; 
						    display 0 0 "    ${cp}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/"; 
						    display 0 0 "    DOCX_CONFIGPATH  = ${DOCX_CONFIGPATH}"; 
						    display 0 0 "    DOCX_DOCTEMPLATE = ${DOCX_DOCTEMPLATE}"; 
						    display 0 0 "    DOCX_DOCTYPE     = ${DOCX_DOCTYPE}"; 
							display 0 0 EMPTYLINE
							IFSO=$IFS
							IFS='
					'
							for d in ${cp}/${DOCX_DOCTEMPLATE}/${DOCX_DOCTYPE}/docsrc/*;do
								IFS=$IFSO
								exec_call cp -pPr "${d}" "${BUILDPATH}";
							done
							IFS=$IFSO
						fi
					done

					echo __REGULAREND__
				} | \
				awk -v state=_STATE '/__REGULAREND__/{regend=1;}and(state, 6){print;}END{if(regend!=1){exit 1;}}'
				_EXIT=$?
				if [ $_EXIT -ne 0 ];then
					display ERROR $_EXIT "prepare document build input"
					exit $_EXIT
				fi
				
			fi
			echo "${0##*/}:Calling build of document 'make ${DOCX_DOCTYPE}'"
			if((DOCX_DEBUG > 0));then
				display 0 0 ":CD:            <${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}>"
				display 0 0 ":SPHINXOPTS:    <${SPHINXOPTS}>"
				display 0 0 ":CALL:          <make ${DOCX_DOCTYPE}>"
			fi
			cd  ${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}
			SPHINXOPTS="${SPHINXOPTS}" make ${DOCX_DOCTYPE}
			RES=$?;
			cd -
		else
			echo "${0##*/}:Result: $RES"
		fi
	fi
	if((DOCX_VERBOSE > 1));then
		echo
	fi
done

echo

exit $RES


#
# editedcheck: 20191128510334
#
