
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
# create repo
# cd myproject
# git init
# # add all your files.  Users can specify file names or directories instead of '.'
# git add .
# git commit -m update-${RELEASE}
# git remote add origin ssh://acue_sf1@git.code.sf.net/p/${PROJECTNAME}/code
# git push -u origin master
#

#
# 2. build - packages
#
. ./setenv-acue3.sh
. ./setenv.sh
. ~/venv/3.8.0/bin/activate
# workon 3.8.0
#
# . ./setenv-acue2.sh
# . ./setenv.sh
# #workon 2.7.16
# . ~/venv/2.7.16/bin/activate

rm -f dist/*
python setup.py sdist
python setup.py bdist
# python setup.py bdist_rpm



#
# 2. build - documents
#
# . ./setenv-acue2.sh
# . ./setenv.sh
# #workon 2.7.16
# . ~/venv/2.7.16/bin/activate
#
python setup.py build_docx --doctemplate=rtd_apiref --apiref  --clean-all --config-path=../../../components/${PACKAGENAME}/config/sphinx/
# python setup.py build_docx --doctemplate=rtd_apiref --apiref
# python setup.py install_docx --clean



#
# 3. sync repos - git
#
#git pull --rebase
git pull origin master
git add .
git commit -m update-${RELEASE}
git push origin master


#
# 4. upload file packages
#
FILELIST=""
FILELIST="${FILELIST} "
FILELIST="${FILELIST} "
FILELIST="${FILELIST} README.md"
FILELIST="${FILELIST} ArtisticLicense20.html"
FILELIST="${FILELIST} licenses-amendments.txt"
FILELIST="${FILELIST} dist/*"
rsync --delete -avP -e 'ssh' ${FILELIST}  acue_sf1@frs.sourceforge.net:/home/frs/project/${PACKAGENAME}/${PACKAGENAME}-${RELEASE}/
 

#
# 5. upload top-layer text
#
COMMONDOC=""
COMMONDOC="${COMMONDOC} README.md"
COMMONDOC="${COMMONDOC} ArtisticLicense20.html"
COMMONDOC="${COMMONDOC} licenses-amendments.txt"
rsync --delete -avP -e 'ssh' ${COMMONDOC}  acue_sf1@frs.sourceforge.net:/home/frs/project/${PACKAGENAME}/


# 6. upload documentation
rsync --delete -avHP -e 'ssh' build/doc/${PACKAGENAME}/  acue_sf1@frs.sourceforge.net:/home/project-web/${PACKAGENAME}/htdocs

rm -rf doc/en/
mkdir -p doc/en/
cp -pPR build/doc/${PACKAGENAME} doc/en/
git add .
git commit -m update-${RELEASE}
git push origin master
git push all

