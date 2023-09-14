This project explores accessing oracle 19c via SQLAlchemy, using oracledb.

It is based on [this article](https://medium.com/oracledevs/using-the-development-branch-of-sqlalchemy-2-0-with-python-oracledb-d6e89090899c), using this [docker image](https://registry.hub.docker.com/r/doctorkirk/oracle-19c).

These instructions apply to an M-series Mac.

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
```bash
docker run --name oracle-19c --platform linux/amd64 -p 1521:1521 -e ORACLE_SID=ORCL -e ORACLE_PWD=tiger -v ~/dev/ApiLogicServer/ApiLogicServer-dev/oracle/oracle-19c/oradata/:/opt/oracle/oradata doctorkirk/oracle-19c 
```

For amd architectures:
```bash
docker run --name oracle-19c -p 1521:1521 -e ORACLE_SID=ORCL -e ORACLE_PWD=tiger -v /Users/val/dev/ApiLogicServer/ApiLogicServer-dev/oracle/oracle-19c/oradata/:/opt/oracle/oradata doctorkirk/oracle-19c 
```


