#!/usr/bin/env python3

import sys
import shutil
import os
import re

version = "1.0.1"

def createParameterMapping(parameters):
    parameters = parameters[1:]
    parameterMapping = []

    for parameter in parameters:
        parameterMapping.append(parameter)

    return parameterMapping

def analyzeIfIsFile(object):
    if not os.path.exists(object):
        return False
    try:
        file = open(object, "r")
        file.close()
        return True
    except:
        return False

def hasCleanupFlag(parameter):
    return "--cleanup" in parameter

def hasVersionFlag(parameter):
    return "--version" in parameter

def removeAllBackupFiles(file_path):
    if not os.access(file_path, os.W_OK):
        print(f"No write permissions for {file_path}")
        return

    file_dir = os.path.dirname(file_path)
    file_name = os.path.basename(file_path)

    test_file_path = os.path.join(file_dir, file_name + ".bak")
    if os.path.exists(test_file_path):
        try:
            os.remove(test_file_path)
            print(f"Deleted {test_file_path}")
        except:
            print(f"Unable to delete {test_file_path}")

    # remove all files with .bak or .bak-* suffix
    pattern = re.compile(f"^{file_name}\.bak-\d+$")
    for file in os.listdir(file_dir):
        if pattern.match(file):
            os.remove(os.path.join(file_dir, file))

def create_backup_copy(file_path):
    # Check if the file already has a ".bak" copy
    if os.path.exists(file_path + ".bak"):
        # Find the highest suffix number
        suffix_number = 1
        while True:
            suffix = f".bak-{suffix_number}"
            backup_path = file_path + suffix
            if not os.path.exists(backup_path):
                break
            suffix_number += 1
    else:
        suffix = ".bak"
        backup_path = file_path + suffix

    # Create the copy
    shutil.copy(file_path, backup_path)

parameterMap = createParameterMapping(sys.argv)

cleanup_flag_present = False
for parameter in parameterMap:
    # check if the parameter is the cleanup flag
    if hasCleanupFlag(parameter):
        cleanup_flag_present = True
    if hasVersionFlag(parameter):
        print(version)
        sys.exit(0)
    elif analyzeIfIsFile(parameter):
        if cleanup_flag_present:
            removeAllBackupFiles(parameter)
        else:
            create_backup_copy(parameter)