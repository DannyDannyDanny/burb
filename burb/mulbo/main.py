"""Define mpath, read files in mpath, write file index to database."""
import sqlite3
import os
try:
    import config
except ImportError:
    from foldersage import config
import pandas as pd
from pathlib import Path
import sys
try:
    from foldersage.foldersage import get_db_con
except ImportError:
    from foldersage import get_db_con

path_to_db = config.dirs['db_foldersage']
if not Path(path_to_db).exists():
    path_to_db = path_to_db.replace('../', '')

print('connecting')
con = get_db_con()

there = """
SELECT
    *
FROM
    sqlite_master
"""
tables = pd.read_sql(there, con)
print('sqlite master')
print(tables.to_markdown())

print('files head')
df1 = pd.read_sql("select * from files;", con)
print(df1.head().to_markdown())

# %%
sys.exit(0)
sql_exec(sql_audio_create)
# tasks
file_id = 1
audio = ('Analyze the requirements of the app', 1)
# create tasks
create_task(con, audio)
table = "audio"
pd.read_sql(f"SELECT * FROM {table}", con)
# %%
print(dir(con))

sql_exec(there)

# %%

# %%


# %%0

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    c = conn.cursor()
    c.execute(create_table_sql)


# create a database connection

# create projects table
create_table(conn, sql_index_files_table)

# create tasks table
create_table(conn, sql_create_tasks_table)

sql_table_paths = """
DROP TABLE IF EXISTS files;"""
con = get_db_con()
pd.read_sql(sql_table_paths, con)

# Create table paths with all paths in library
print("Create paths table")
sql_table_paths = """
DROP TABLE IF EXISTS files;"""
sql_exec(sql_table_paths)
sql_table_paths = """
CREATE TABLE files(
    file_id INTEGER PRIMARY KEY AUTOINCREMENT,
    path text,
    filename text,
    filsize integer);"""
sql_exec(sql_table_paths)
print("get collections glob")
