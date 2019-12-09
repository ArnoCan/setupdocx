
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


# Last login: Thu Jun 14 12:28:50 2018 from 172.30.20.205

# You don't have an active shell at this time.  For basic file transfers and
# management, use web.sourceforge.net -- it allows rsync, sftp, and scp access.

# If you would like to create a shell, pass the "create" command to ssh. If you
# tell ssh to allocate a tty (e.g. using -t), an interactive shell will be opened
# when the create is done. Otherwise, the create command will exit when the shell
# becomes ready for use. An example create that enters the shell when ready:

#     ssh -t myname@shell.sourceforge.net create

# Connection to shell.sourceforge.net closed.
# (2.7.16) [acue@lap001 pysourceinfo]$ ssh -t acue_sf1@shell.sourceforge.net create

# Requesting a new shell for "acue_sf1" and waiting for it to start.
