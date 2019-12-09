
if [ ! -e "RELEASE-INFO.sh"  ];then
	cat <<EOF

Missing file: RELEASE-INFO.sh

Contains:

   # current release of the project
   RELEASE=<e.g. 00.01.006>

   # name of the project
   PROJECTNAME=<e.g. setuplib>

   # name of the package
    PACKAGENAME=<e.g. setuplib>

EOF
	
	exit 1
fi

source RELEASE-INFO.sh



# 1. set proxy
export http_proxy=localhost:8125
export https_proxy=localhost:8125


#
# ***  new repo  ***
#
# requires currently SSH keys
#
#  create repo
# cd myproject
# git init
# # add all your files.  Users can specify file names or directories instead of '.'
# git add .
# # git commit -a -m initial
# git commit -m update-${RELEASE}
# git config user.name "ArnoCan"
# git remote add origin git@github.com:ArnoCan/${PACKAGENAME}.git
# git push -u origin master
#

#
# 2. build - packages
#
. ./setenv-acue3.sh
. ./setenv.sh
. ~/venv/3.8.0/bin/activate
#workon 3.8.0
#

# #
# # 2. build - documents
# #
# . ./setenv-acue2.sh
# . ./setenv.sh
# #workon 2.7.16
# . ~/venv/2.7.16/bin/activate
#
python setup.py build_docx --doctemplate=rtd_apiref --apiref --clean-all --docname=${PACKAGENAME} --config-path=../../../components/${PROJECTNAME}/config/sphinx/

if [ -e doc/en ];then
	rm -rf doc/en
fi
mkdir -p doc/en/
cp -pPR build/doc/${PACKAGENAME} doc/en/${PACKAGENAME}
# cp -pPR build/doc/${PACKAGENAME} doc/en/${PROJECTNAME}


#
# 3. sync repos - git
#

git add .
git commit -m update-${RELEASE}


# git pull --rebase
git pull origin master
git push origin master





