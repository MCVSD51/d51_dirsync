d51_dirsync
=======

Based on dirsync by Thomas Khyn and robocopier by Anand B Pillai

|copyright| 2014-2020 Thomas Khyn
|copyright| 2003-2015 Anand B Pillai

Advanced directory tree synchronisation tool

based on `Python robocopier`_ by Anand B Pillai

If you like d51_dirsync and find it useful, you may want to thank me and
encourage future development by sending a few mBTC / mBCH / mBSV at this address:
``1EwENyR8RV6tMc1hsLTkPURtn5wJgaBfG9``.

Usage
-----

From the command line::

   d51_dirsync <sourcedir> <targetdir> [options]

From python::

   from d51_dirsync import sync
   sync(sourcedir, targetdir, action, **options)


Main Options
------------

Chosing one option among the following ones is mandatory

--diff, -d              Only report difference between sourcedir and targetdir
--sync, -s              Synchronize content between sourcedir and targetdir
--update, -u            Update existing content between sourcedir and targetdir

If you use one of the above options (e.g. ``sync``) most of the time, you
may consider defining the ``action`` option in a `Configuration file`_ parsed
by d51_dirsync.


Additional Options
------------------

--verbose, -v           Provide verbose output
--purge, -p             Purge files when synchronizing (does not purge by
                        default)
--force, -f             Force copying of files, by trying to change file
                        permissions
--twoway, -2            Update files in source directory from target
                        directory (only updates target from source by default)
--create, -c            Create target directory if it does not exist (By
                        default, target directory should exist.)
--ctime                 Also takes into account the source file\'s creation
                        time (Windows) or the source file\'s last metadata
                        change (Unix)
--content               Takes into account ONLY content of files. 
                        Synchronize ONLY different files.
                        At two-way synchronization source files content 
                        have priority if destination and source are existed
--recursive, -r         If this is false, only files at the root of the path will synced.
--ignore, -x patterns   Regex patterns to ignore
--only, -o patterns     Regex patterns to include (exclude every other)
--exclude, -e patterns  Regex patterns to exclude
--include, -i patterns  Regex patterns to include (with precedence over
                        excludes)


Configuration file
------------------

.. note::
   Configuration files are only used when using the command line, and ignored
   when d51_dirsync is called from within Python.

If you want to use predefined options all the time, or if you need specific
options when 'd51_dirsyncing' a specific source directory, d51_dirsync looks for
two configuration files, by order or priority (the last takes precedence)::

    ~/.d51_dirsync
    source/directory/.d51_dirsync

.. note::
   A ~/.d51_dirsync configuration file is automatically created the first time
   d51_dirsync is ran from the command line. It enables ``sync`` mode by default.

.. warning::
   Any ``source/directory/.d51_dirsync`` file is automatically excluded from the
   files to compare. You have to explicitly include using the ``--include``
   option it if you want it to be covered by the comparison.

The command line options always override the values defined in the
configuration files.

The configuration files must have a ``defaults`` section, and the options are
as defined above. The only exception is for the option ``action``, which can
take 3 values ``diff``, ``sync`` or ``update``.

Example config file::

   [defaults]
   action = sync
   create = True


Custom logger
-------------

From python, you may not want to have the output sent to ``stdout``. To do so,
you can simply pass your custom logger via the ``logger`` keyword argument of
the ``sync`` function::

   sync(sourcedir, targetdir, action, logger=my_logger, **options)


.. |copyright| unicode:: 0xA9

.. _`Python robocopier`: http://code.activestate.com/recipes/231501-python-robocopier-advanced-directory-synchronizati/
