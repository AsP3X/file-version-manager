#!/bin/bash

# download the python script from the URL
curl -o /usr/bin/fvm.py https://raw.githubusercontent.com/AsP3X/file-version-manager/master/fvm.py?v=$(date +%s)

# make the script executable
chmod +x /usr/bin/fvm.py

# create a symlink to the script in /usr/bin
ln -s /usr/bin/fvm.py /usr/bin/fvm