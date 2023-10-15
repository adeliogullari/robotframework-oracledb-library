from typing import Optional

from oracledb import Connection, Cursor, SessionPool, Var
from ..decorator import Singleton


@Singleton
class OracleBase:

    def __init__(self):
        self._connection: Optional[Connection] = None
        self._cursor: Optional[Cursor] = None
        self._session_pool: Optional[SessionPool] = None
        self._var: Optional[Var] = None

    @property
    def connection(self) -> Connection:
        return self._connection

    @connection.setter
    def connection(self, value: Connection):
        self._connection = value

    @property
    def cursor(self) -> Cursor:
        return self._cursor

    @cursor.setter
    def cursor(self, value: Cursor):
        self._cursor = value

    @property
    def session_pool(self) -> SessionPool:
        return self._session_pool

    @session_pool.setter
    def session_pool(self, value: SessionPool):
        self._session_pool = value

    @property
    def var(self) -> Var:
        return self._var

    @var.setter
    def var(self, value: Var):
        self._var = value
