#
# PROJECT   = setupdocx
# AUTHOR    = Arno-Can Uestuensoez
# COPYRIGHT = Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez
# LICENSE   = Artistic-License-2.0 + Forced-Fairplay-Constraints
#

DOCX_DEBUG=${DOCX_DEBUG:-0}
DOCX_VERBOSE=${DOCX_VERBOSE:-0}
DOCX_QUIET=${DOCX_QUIET:-0}


# writes exec traces into the root of the document-build directory
if((DOCX_DEBUG > 0));then
	DOCX_EXECTRACE="${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}/exec-calls-${DOCX_DOCTEMPLATE:-default}-${DOCX_DOCTYPE:-default}.txt"

	if((DOCX_DEBUG > 1));then
		echo "# DBG:" >&2
		echo "# DBG: WRAPPER      = ${0}">&2
		echo "# DBG: LIB          = ${BASH_SOURCE}">&2
		echo "# DBG:PWD          = ${PWD}">&2
		echo "# DBG:\$@           = '$@'">&2
		echo "# DBG:DATETIME     = $(date '+%Y%m%d%H%M%S')">&2
		echo "# DBG:">&2
	fi
	
	echo "#" > "${DOCX_EXECTRACE}"
	echo "#" >> "${DOCX_EXECTRACE}"
	echo "# $(date)" >> "${DOCX_EXECTRACE}"
	echo "#" >> "${DOCX_EXECTRACE}"
	echo "# EXEC-WRAPPER" >> "${DOCX_EXECTRACE}"
	echo "# ============" >> "${DOCX_EXECTRACE}"
	echo "#" >> "${DOCX_EXECTRACE}"
	echo "# build and assembly calls for document creation" >> "${DOCX_EXECTRACE}"
	echo "# created by 'exec_call' from 'libbash.sh'" >> "${DOCX_EXECTRACE}"
	echo "#" >> "${DOCX_EXECTRACE}"
	echo "# WRAPPER      = ${0}" >> "${DOCX_EXECTRACE}"
	echo "# LIB          = ${BASH_SOURCE}" >> "${DOCX_EXECTRACE}"
	echo "# PWD          = ${PWD}" >> "${DOCX_EXECTRACE}"
	echo "# \$@           = '$@'" >> "${DOCX_EXECTRACE}"
	echo "# DATETIME     = $(date '+%Y%m%d%H%M%S')" >> "${DOCX_EXECTRACE}"
	echo "#" >> "${DOCX_EXECTRACE}"
	echo "# PROJECT      = ${PROJECT}" >> "${DOCX_EXECTRACE}"
	echo "# DOCNAME      = ${DOCX_DOCNAME}" >> "${DOCX_EXECTRACE}"
	echo "# CONFIG       = ${DOCX_CONFIGPATH}" >> "${DOCX_EXECTRACE}"
	echo "# TEMPLATE     = ${DOCX_DOCTEMPLATE}" >> "${DOCX_EXECTRACE}"
	echo "# INDEXSRC     = ${DOCX_INDEXSRC}" >> "${DOCX_EXECTRACE}"
	echo "# DOCTYPE      = ${DOCX_DOCTYPE}" >> "${DOCX_EXECTRACE}"
	echo "# SOURCE       = ${DOCX_DOCSRC}" >> "${DOCX_EXECTRACE}"
	echo "# BUILDER      = ${DOCX_BUILDER}" >> "${DOCX_EXECTRACE}"
	echo "# BUILDDIR     = ${DOCX_BUILDDIR}" >> "${DOCX_EXECTRACE}"
	echo "# BUILDRELDIR  = ${DOCX_BUILDRELDIR}" >> "${DOCX_EXECTRACE}"
	echo "# ENVIRON      = ${DOCX_BUILDDIR}/${DOCX_BUILDRELDIR}/setenv.sh" >> "${DOCX_EXECTRACE}"
	echo "#" >> "${DOCX_EXECTRACE}"
	echo "# VERSION      = ${VERSION}" >> "${DOCX_EXECTRACE}"
	echo "# RELEASE      = ${RELEASE}" >> "${DOCX_EXECTRACE}"
	echo "#" >> "${DOCX_EXECTRACE}"
	echo "" >> "${DOCX_EXECTRACE}"
fi

function display() {
	# displays text
	# evaluates DOCX_QUIET
	#
	# Args:
	#   $1:  debug level
	#   $2:  verbose level
	#   $3+  output text
	# Returns:
	#   Displayed text
	#
	local _dlvl=$1;
	local _vlvl=$2;
	local _off=0
	local _err=0
	local _wng=0
	local _empty=0
	
    if [[ "$1" == "ERROR" ]];then
		_err=$2
		shift 2
		_off=1
    elif [[ "$1" == "WARNING" ]];then
    	_wng=1
		shift 1
		_off=1
    elif [[ "$3" == "EMPTYLINE" ]];then
		_empty=1
    elif [[ "X${_dlvl//[0-9]/}" != "X" || "X${_vlvl//[0-9]/}" != "X" ]];then
		_off=1
	fi
	
	local _callidx=${#BASH_LINENO[@]}
	_callidxline=$((_callidx-2))
	_callidxfile=$((_callidx-3))
	if [ "$BASH_SOURCE" == "${BASH_SOURCE[$_callidxfile]}" ];then
		_callidxfile=$((_callidx-4))
	fi

	if((_empty==1));then
		if((DOCX_DEBUG > _dlvl));then
			echo "#" >&2
		elif((DOCX_VERBOSE > _vlvl));then
			echo "#"
		elif((DOCX_DEBUG ==0 && DOCX_VERBOSE == 0 && DOCX_QUIET == 0));then
			echo "#"
		elif((DOCX_QUIET == 0));then
			echo 
		fi
	elif((_off==0 && DOCX_DEBUG > _dlvl));then
		shift 2
		printf "# DBG:%s:%04d: %s\n" "${BASH_SOURCE[$_callidxfile]##*/}" ${BASH_LINENO[$_callidxline]} "$*" >&2
	elif((_off==0 && DOCX_VERBOSE > _vlvl));then
		shift 2
		printf "# VERB:%s:%04d: %s\n" "${BASH_SOURCE[$_callidxfile]##*/}" ${BASH_LINENO[$_callidxline]} "$*"
	elif((_err>0));then
		printf "\n#***\n# ERROR:%s:%04d:%d: %s\n#***\n\n" "${BASH_SOURCE[$_callidxfile]##*/}" ${BASH_LINENO[$_callidxline]} $_err "$*" >&2
	elif((_wng>0));then
		printf "#\n# WARNING:%s:%04d:%d: %s\n#\n" "${BASH_SOURCE[$_callidxfile]##*/}" ${BASH_LINENO[$_callidxline]} $_wng "$*" >&2
	elif((DOCX_DEBUG ==0 && DOCX_VERBOSE == 0 && DOCX_QUIET == 0));then
		shift 2
		echo "# $@"
	elif((DOCX_QUIET == 0));then
		echo "$@"
	fi
}

function display_state() {
	# gets resulting display status as return code
	#
	# Args:
	#   $1:  debug level
	#   $2:  verbose level
	# Returns:
	#   0:   no output
	#   1:   standard
	#   2:   verbose
	#   4:   debug
	#
	local _dlvl=$1; 
	local _vlvl=$2;
	local ret=0
	
	if((DOCX_VERBOSE > _vlvl));then ret=$((ret+2)); fi
	if((DOCX_DEBUG > _dlvl));then ret=$((ret+4)); fi
	if((DOCX_DEBUG ==0 && DOCX_VERBOSE == 0 && DOCX_QUIET == 0));then ret=$((ret+1)); fi

	return $ret
}


function exec_call() {
	# executes the call, or prints it only
	# evaluates DOCX_NOEXEC

	if [ "X${DOCX_NOEXEC}" == "X1" ];then
		display $@
	else
		display $@
		if((DOCX_DEBUG > 0));then
			echo $@ >> "${DOCX_EXECTRACE}"
		fi
		eval $*
		_err=$?
		if((_err!=0));then
			display ERROR $_err "EXEC-FAILED: $*"
			if((DOCX_DEBUG > 0));then
			    display ERROR $_err "EXEC-FAILED: $*" 2>>"${DOCX_EXECTRACE}" 
			fi
		fi
	fi
	if((DOCX_BREAKONERR>0 && _err!=0));then
		display "BREAKONERR:exit wrapper after first error => exit=$_err"
		display " "
		exit $_err
	fi
	return $_err
}

display 1 1 "libbash.sh loaded..."
