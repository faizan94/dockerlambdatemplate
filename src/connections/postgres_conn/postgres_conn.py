import logging
from abc import ABC, abstractmethod


class PostgresConn(ABC):

    _connection: object
    _db_name: str
    _table: str

    def execute(self, result):
        # Check if the connection is there
        if self.is_closed():
            logging.error(f'Connection closed for: {self._db_name}')
            raise Exception(f'Connection closed for: {self._db_name}')

        # Execute query
        cur = self._connection.cursor()
        query = f'INSERT INTO {self._table} VALUES({result}) ON CONFLICT DO NOTHING'
        cur.execute(query)
        self._connection.commit()

    def is_closed(self):
        return self._connection.closed

    def close(self):
        self._connection.close()
