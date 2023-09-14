This project explores accessing oracle 19c via SQLAlchemy, using oracledb.

It is based on [this article](https://medium.com/oracledevs/using-the-development-branch-of-sqlalchemy-2-0-with-python-oracledb-d6e89090899c).

It uses  [docker image](https://registry.hub.docker.com/r/doctorkirk/oracle-19c): a *SingleInstance-NonCDB* server.

These instructions were run on an M-series Mac.

### Setup venv

Setup your venv...

```bash title="Install API Logic Server in a Virtual Environment"
python -m venv venv                        # may require python3 -m venv venv
venv\Scripts\activate                      # mac/linux: source venv/bin/activate
python -m pip install -r requirements.txt  # accept "new Virtual environment"
```

### Download and start Oracle

#### Set up Oracle Volume

```bash
cd ~/dev/ApiLogicServer/ApiLogicServer-dev/oracle
mkdir oracle-19c
chmod -R 755 oracle-19c
```

### Start Oracle

For an M-series mac:

-e MYSQL_ROOT_PASSWORD=p
```bash
docker run --name oracle-19c --platform linux/amd64 -p 1521:1521 -e ORACLE_SID=ORCL -e ORACLE_PWD=tiger -v ~/dev/ApiLogicServer/ApiLogicServer-dev/oracle/oracle-19c/oradata/:/opt/oracle/oradata doctorkirk/oracle-19c 
```

For amd architectures:
```bash
docker run --name oracle-19c -p 1521:1521 -e ORACLE_SID=ORCL -e ORACLE_PWD=tiger -v /Users/val/dev/ApiLogicServer/ApiLogicServer-dev/oracle/oracle-19c/oradata/:/opt/oracle/oradata doctorkirk/oracle-19c 
```

#### Fails - no services

The log indicates the database failed to start, *listener supports no services*:

```log
(venv) val@Vals-MPB-14 python-oracledb-SQLAlchemy % docker run --name oracle-19c --platform linux/amd64 -p 1521:1521 -e ORACLE_SID=ORCL -e ORACLE_PWD=tiger -v ~/dev/ApiLogicServer/ApiLogicServer-dev/oracle/oracle-19c/oradata/:/opt/oracle/oradata doctorkirk/oracle-19c
cat: /sys/fs/cgroup/memory/memory.limit_in_bytes: No such file or directory
cat: /sys/fs/cgroup/memory/memory.limit_in_bytes: No such file or directory
/opt/oracle/runOracle.sh: line 102: [: -lt: unary operator expected
ORACLE PASSWORD FOR SYS, SYSTEM AND PDBADMIN: tiger

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 14-SEP-2023 02:20:04

Copyright (c) 1991, 2020, Oracle.  All rights reserved.

Starting /opt/oracle/product/19c/dbhome_1/bin/tnslsnr: please wait...

TNSLSNR for Linux: Version 19.0.0.0.0 - Production
System parameter file is /opt/oracle/product/19c/dbhome_1/network/admin/listener.ora
Log messages written to /opt/oracle/diag/tnslsnr/211e1d9eee03/listener/alert/log.xml
Listening on: (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1)))
Listening on: (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=0.0.0.0)(PORT=1521)))

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=EXTPROC1)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 19.0.0.0.0 - Production
Start Date                14-SEP-2023 02:20:04
Uptime                    0 days 0 hr. 0 min. 0 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Listener Parameter File   /opt/oracle/product/19c/dbhome_1/network/admin/listener.ora
Listener Log File         /opt/oracle/diag/tnslsnr/211e1d9eee03/listener/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=0.0.0.0)(PORT=1521)))
The listener supports no services
The command completed successfully
```

maybe try `oracleinanutshell/oracle-xe-11g`, using
```bash
docker run -d --rm -p 1521:1521 --name=Oracle-11g --platform linux/amd64 -e ORACLE_ALLOW_REMOTE=true oracleinanutshell/oracle-xe-11g
```

and, for sql:

```bash
docker run --rm --name=sqlplus --platform linux/amd64 --interactive guywithnose/sqlplus sqlplus system/oracle@//10.0.0.77:1521
```

system/oracle

ORCL?



&nbsp;

## Use sqlplus

In Docker desktop, click the image and open terminal, and enter `sqlplus`.
Fails to login with user (scott, SYS, SYSTEM) and pwd `tiger`:

```log
ORA-12547: TNS:lost contact
```

Database log contains:
```log
The listener supports no services
```

Some suggestions in [this article](https://ittutorial.org/the-listener-supports-no-services-alter-system-set-local_listener/).


```bash
sh-4.2$ lsnrctl status listener

LSNRCTL for Linux: Version 19.0.0.0.0 - Production on 14-SEP-2023 01:52:04

Copyright (c) 1991, 2020, Oracle.  All rights reserved.

Connecting to (DESCRIPTION=(ADDRESS=(PROTOCOL=IPC)(KEY=EXTPROC1)))
STATUS of the LISTENER
------------------------
Alias                     LISTENER
Version                   TNSLSNR for Linux: Version 19.0.0.0.0 - Production
Start Date                14-SEP-2023 01:19:47
Uptime                    0 days 0 hr. 32 min. 17 sec
Trace Level               off
Security                  ON: Local OS Authentication
SNMP                      OFF
Listener Parameter File   /opt/oracle/product/19c/dbhome_1/network/admin/listener.ora
Listener Log File         /opt/oracle/diag/tnslsnr/1726a1dad864/listener/alert/log.xml
Listening Endpoints Summary...
  (DESCRIPTION=(ADDRESS=(PROTOCOL=ipc)(KEY=EXTPROC1)))
  (DESCRIPTION=(ADDRESS=(PROTOCOL=tcp)(HOST=0.0.0.0)(PORT=1521)))
The listener supports no services
The command completed successfully
```


&nbsp;

## Run `sa-db`

Use Run Config sa-db.

Fails "orclpdb1 is not registered..."


