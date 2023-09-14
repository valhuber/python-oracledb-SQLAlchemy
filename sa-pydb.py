# sa-pydb.py
#
# Using SQLAlchemy 2.0 with python-oracledb
#
# https://oracle.github.io/python-oracledb/

import os

import oracledb
from sqlalchemy import create_engine
from sqlalchemy import text

# Database Credentials
username = os.environ.get("scott")
password = os.environ.get("tiger")

# For PYTHON_CONNECTSTRING, I use Easy Connect strings like "localhost/orclpdb1".  These two lines
# let me access the components individually
cp = oracledb.ConnectParams()
cp.parse_connect_string("localhost/orclpdb1")
# cp.parse_connect_string(os.environ.get("localhost/orclpdb1"))

# For the default, python-oracledb Thin mode that doesn't use Oracle Instant Client
thick_mode = None

# To use python-oracledb Thick mode on macOS (Intel x86).
#thick_mode = {"lib_dir": os.environ.get("HOME")+"/Downloads/instantclient_19_8"}

# To use python-oracledb Thick mode on Windows
#thick_mode = {"lib_dir": r"C:\oracle\instantclient_19_15"}

# For thick mode on Linux use {} ie. no lib_dir parameter.  On Linux you
# must configure the Instant Client directory by setting LD_LIBRARY_PATH or
# running ldconfig before starting Python.
#thick_mode = {}

engine = create_engine(
    f'oracle+oracledb://{username}:{password}@{cp.host}:{cp.port}/?service_name={cp.service_name}',
    thick_mode=thick_mode)

with engine.connect() as connection:
    print(connection.scalar(text("""SELECT UNIQUE CLIENT_DRIVER
                                    FROM V$SESSION_CONNECT_INFO
                                    WHERE SID = SYS_CONTEXT('USERENV', 'SID')""")))