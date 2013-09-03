mysql2folder
============

Python script: MySQL dump to local folder

Small Python script designed to dump MySQL databases in separate compressed files to a destination folder. Configuration is in the same file and includes MySQL username, password and server hostname plus destination folder of the processed files:

	# START: configuration
	username = 'root'
	password = '555-password-555'
	hostname = 'localhost'
	dest_folder = '/home/backup'
	# END: configuration

New files are created in dest_folder directory. Files are named in format: YYYYMMDD-<database name>.sql.gz.

To backup databases regularly you can add the next line to /etc/crontab file:

    0 0 * * * <username> python /<folder>/mysql2folder.py