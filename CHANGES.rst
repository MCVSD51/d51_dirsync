d51_dirsync - Changes
=================


2.2 (28-01-2015)
----------------

Fixed:
- [cmdline] Package name is now consistently displayed in console messages
- [cmdline] Traceback is no longer shown when an exception is raised
- Nicer error messages
- Created directories counter now works

Changed:
- [backwards incompatible]: --nodirection option replaced by --twoway (-2)
- [backwards incompatible]: --modtimeonly option replaced by --ctime
  (defaults to False)
- A default ~/.d51_dirsync config file is created on first run

2.2.1 (19-07-2015)
..................

Fixed:
- duplicate log entries when calling d51_dirsync subsequently (#2)

2.2.2 (29-02-2016)
..................

Fixed:
- six was not present in install_requires (#3)

2.2.3 (06-02-2017)
..................

Fixed:
- options file initialisation
- newline chars at end of logs (#15)

2.2.4 (06-07-2019)
..................

Added:
- ``--content`` option to compare files by content

2.2.5 (01-08-2020)
..................

2.2.6 (02-08-2022)

Added functionality to not recurse through a directory.

Fixed:
- Comparisons on windows
- Read-only files handling (#25)


2.1 (08-09-2014)
----------------

- Added config files support when called from command line
- Added custom logger when called from python


2.0 (30-07-2014)
----------------

- The script is now wrapped into a python package
- ``ignore``, ``exclude``, ``only`` and ``include`` options for advanced file
  filtering via regular expressions
- Python 3 compatibility


1.0 (30-10-2003)
----------------

- Anand's Python robocopier is published on activestate:
  http://code.activestate.com/recipes/231501-python-robocopier-advanced-directory-synchronizati/
