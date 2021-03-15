import logging
import psycopg2

from .postgres_conn import PostgresConn
from src.utils.aws_data_handler import get_rds_connection_details


class Secret(PostgresConn):

    def __init__(self, db_conf, table):
        db_conf = get_rds_connection_details(db_conf['secret_name'])

        # create db connection
        self._connection = psycopg2.connect(
            host=db_conf['host'],
            database=db_conf['db_name'],
            user=db_conf['user'],
            password=db_conf['password'])

        # saved db name
        self._db_name = db_conf['db_name']
        self._table = table

        # Check if the connection was established
        if self.is_closed():
            logging.error(f'Unable to connect to database: {self._db_name}')
            raise Exception(f'Unable to connect to database: {self._db_name}')
