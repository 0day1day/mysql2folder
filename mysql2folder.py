#!/usr/bin/env python
import os
import time

# START: configuration
username = ''
password = ''
hostname = ''
dest_folder = ''
# END: configuration

# timestamp
filestamp = time.strftime('%Y%m%d')
# database list
database_list_command="mysql -u%s -p%s -h %s --silent -N -e 'show databases'" % (username, password, hostname)
# iterate database list
for database in os.popen(database_list_command).readlines():
        database = database.strip()
        # databases not to backup
        if database == 'information_schema' or database == 'test' or database == 'mysql' or database == 'performance_schema':
                continue
        # destination and filename
        filename = "%s/%s-%s.sql" % (dest_folder, filestamp, database)
        # dump + gzip command
        os.popen("mysqldump -u%s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (username, password, hostname, database, filename))
