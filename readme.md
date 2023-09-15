This project explores accessing oracle 19c via SQLAlchemy, using oracledb.

It is based on [this article](https://medium.com/oracledevs/using-the-development-branch-of-sqlalchemy-2-0-with-python-oracledb-d6e89090899c).

The article provides the [following sample code](https://github.com/cjbj/python-oracledb-demos-2022/blob/main/6_sqlalchemy_example.py).

These instructions were run on an AMD-series Mac, **ONLY**.

&nbsp;

## Setup venv

Setup your venv...

```bash title="Install API Logic Server in a Virtual Environment"
python -m venv venv                        # may require python3 -m venv venv
venv\Scripts\activate                      # mac/linux: source venv/bin/activate
python -m pip install -r requirements.txt  # accept "new Virtual environment"
```

&nbsp;

## Obtain the Docker Image

**Set up Oracle Volume**

```bash
cd ~/dev/ApiLogicServer/oracle
mkdir oracle-19c
chmod -R 755 oracle-19c
```

**Start Oracle**

For amd architectures, this will install Oracle 19 and SqlPlus (command line SQL):

```bash
docker run --name oracle-19c -p 1521:1521 -e ORACLE_SID=ORCL -e ORACLE_PWD=tiger -v /Users/val/dev/ApiLogicServer/ApiLogicServer-dev/oracle/oracle-19c/oradata/:/opt/oracle/oradata doctorkirk/oracle-19c 
```

> Note: Start takes several minutes (initially) once docker is downloaded/started.

> Note: This fails under M-series Macs.  There are several web articles that discuss how to make this work, but we have not tried them.

**Verify SqlPlus**

Use Docker desktop > terminal to login to `sqlplus` with system/tiger.  Some commands you might want:

```sql
-- list schemas

select * from all_users;

select USERNAME from all_users;

alter session set current_schema = HR;

SELECT table_name FROM all_tables WHERE owner = 'HR';

-- determine service name

select value from v$parameter where name like '%service_name%';
```

&nbsp;

## Verify Connectivity

&nbsp;

### Run `sa-db`

Use Run Config sa-db.

&nbsp;

### Run `6_sqlalchemy_example`

&nbsp;


## API Logic Server usage

### Deploy the HR Example

Use [this documentation](https://docs.oracle.com/en/database/oracle/oracle-database/19/comsc/installing-sample-schemas.html#GUID-CB945E4C-D08A-4B26-A12D-3D6D688467EA).

The installer will ask several questions; we used the following responses:

> args: 1 = tiger, 2 = users, 3 = temp, 4 = tiger, 5 = $ORACLE_HOME/demo/schema/log/

Here, for example, is the [create sql](https://github.com/oracle-samples/db-sample-schemas/blob/main/human_resources/hr_create.sql).

&nbsp;

### Create API Logic Project

```bash
ApiLogicServer create --project_name=oracle_hr --db_url='oracle+oracledb://hr:tiger@localhost:1521/?service_name=ORCL'
```

Notes:

1. `oracle+oracledb` designates the database type.  ApiLogicServer includes this driver, so you don't need to pip-install it.

2. Observe the login is `hr` (not `system`).  The previous step defines the `hr` user as having the default schema as `hr`.  This is one approach for filtering the tables for a specific schema.  

3. Note the `service_name=ORCL` corresponds to `ORACLE_SID=ORCL` on the docker start command above.