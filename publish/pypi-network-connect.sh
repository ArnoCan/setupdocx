
if [ ! -e "RELEASE-INFO.sh"  ];then
	cat <<EOF

Missing file: RELEASE-INFO.sh

Contains:

   # current release of the project
   RELEASE=00.01.006

   # name of the project
   PROJECTNAME=setuplib

   # name of the package
    PACKAGENAME=setuplib

EOF
	
	exit 1
fi

source RELEASE-INFO.sh



# 0. start network

#  - start polipo http/https

#
#  - setup iptables: sshxd
#
# set: 01.10.012-min-ssh
#
# as root
#
if [ "A" == "B" ]; then
	REL=01.10.012-min-ssh;WLANIF=wlp3s0 /local/home1/data/acue/rd/p-own_lap001/firewall-linux-laptop-bash/src/firewall-linux-laptop-bash/rt/firewall/PMs/lap001/${REL}/src/bash/ch.bern.wedorooms.lap001.sh
	iptables -v -I INPUT 1  -m state --state ESTABLISHED,RELATED -j ACCEPT -i wlp3s0
	iptables -v -I OUTPUT 1  -p tcp --dport 22  -o wlp3s0 -j ACCEPT
fi

# 1. set proxy
export http_proxy=localhost:8125
export https_proxy=localhost:8125


#
# 2. connect ssh-agent
#
. ~acue/bin/ssh-agent-manage.sh -A sf
. ~acue/bin/ssh-agent-manage.sh -S sf
#. ssh-agent-manage.sh -a sf
SSH_ADDONS_DIRS=/mnt1/repokeys/keys/pypi.org/ssh-key-20180611/ . ~acue/bin/ssh-agent-manage.sh -a 0
# . ssh-agent-manage.sh -s 0:sf
. ~acue/bin/ssh-agent-manage.sh -s sf
. ~acue/bin/ssh-agent-manage.sh -p




#
#----------------------------------------------------
#
# open maintenance shell
#
# ssh -t  acue_sf1@shell.sourceforge.net create
# ssh  acue_sf1@shell.sourceforge.net
#
#----------------------------------------------------
#


##############################################################################################################

#
# misc.
#


# git commit -a -m 'Initial commit'
# git config --global user.email "acue_sf1@users.sourceforge.net"
# git config --global user.name "Arno-Can Uestuensoez"
# git config branch.master.merge refs/heads/master
# git config branch.master.remote origin
# git config user.email "acue_sf1@users.sourceforge.net"
# git config user.name "Arno-Can Uestuensoez"
# git pull --rebase 
# git pull origin master --allow-unrelated-histories
# git push -u origin master
# git push origin master
# git remote add origin ssh://acue_sf1@git.code.sf.net/p/${PROJECTNAME}/${PROJECTNAME}
# git remote add origin ssh://acue_sf1@git.code.sf.net/p/${PROJECTNAME}/code
# git remote add origin ssh://acue_sf1@git.code.sf.net/p/setuplib/code
# rsync -avP --delete -e 'ssh' platformids  acue_sf1@frs.sourceforge.net:/home/project-web/
# rsync -avP -e 'ssh -o PasswordAuthentication=yes -o PubkeyAuthentication=no' platformids  acue_sf1@frs.sourceforge.net:userweb/htdocs/
# rsync -avP -e 'ssh' platformids  acue_sf1@frs.sourceforge.net:userweb/htdocs/
# ssh  -o PasswordAuthentication=yes -o StrictHostKeyChecking=no -o PubkeyAuthentication=no acue_sf1@shell.sourceforge.net 
# rsync -avP -e 'ssh' ${COMMONDOC}  acue_sf1@frs.sourceforge.net:/home/frs/project/${PROJECTNAME}/
# rsync -avHP -e 'ssh' ${FILELIST}  acue_sf1@frs.sourceforge.net:/home/frs/project/${PROJECTNAME}/${PROJECTNAME}-${RELEASE}/
# rsync --delete  -avHP -e 'ssh' ${FILELIST}  acue_sf1@frs.sourceforge.net:/home/frs/project/${PROJECTNAME}-${RELEASE}/
