import oracledb
from typing import Any
from robotlibcore import keyword
from ..base import OracleBase


class OracleConnectionKeywords:

    def __init__(self):
        self.oracle_base = OracleBase()

    @keyword
    def init_oracle_client(self, *args: Any, **kwargs: Any) -> None:
        oracledb.init_oracle_client(*args, **kwargs)

    @keyword
    def oracle_makedsn(self, *args: Any, **kwargs: Any) -> str:
        return oracledb.makedsn(*args, **kwargs)

    @keyword
    def oracle_connect(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection = oracledb.connect(*args, **kwargs)

    @keyword
    def oracle_connection(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection = oracledb.Connection(*args, **kwargs)

    @keyword
    def oracle_connection_begin(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.begin(*args, **kwargs)

    @keyword
    def oracle_connection_cancel(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.cancel(*args, **kwargs)

    @keyword
    def oracle_connection_changepassword(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.changepassword(*args, **kwargs)

    @keyword
    def oracle_connection_close(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.close(*args, **kwargs)

    @keyword
    def oracle_connection_commit(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.commit(*args, **kwargs)

    @keyword
    def oracle_connection_createlob(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.createlob(*args, **kwargs)

    @keyword
    def oracle_connection_cursor(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.cursor = self.oracle_base.connection.cursor(*args, **kwargs)

    @keyword
    def oracle_connection_deq(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.deq(*args, **kwargs)

    @keyword
    def oracle_connection_deqoptions(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.deqoptions(*args, **kwargs)

    @keyword
    def oracle_connection_enq(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.enq(*args, **kwargs)

    @keyword
    def oracle_connection_enqoptions(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.enqoptions(*args, **kwargs)

    @keyword
    def oracle_connection_gettype(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.connection.gettype(*args, **kwargs)

    @keyword
    def oracle_connection_msgproperties(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.connection.msgproperties(*args, **kwargs)

    @keyword
    def oracle_connection_ping(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.connection.ping(*args, **kwargs)

    @keyword
    def oracle_connection_prepare(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.prepare(*args, **kwargs)

    @keyword
    def oracle_connection_rollback(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.rollback(*args, **kwargs)

    @keyword
    def oracle_connection_shutdown(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.shutdown(*args, **kwargs)

    @keyword
    def oracle_connection_startup(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection.startup(*args, **kwargs)

    @keyword
    def oracle_connection_action(self, value=None) -> None:
        self.oracle_base.connection.action = value

    @keyword
    def oracle_connection_autocommit(self, value=None) -> None:
        if value:
            self.oracle_base.connection.autocommit = value
        return self.oracle_base.connection.autocommit

    @keyword
    def oracle_connection_clientinfo(self, value=None) -> None:
        self.oracle_base.connection.clientinfo = value

    @keyword
    def oracle_connection_client_identifier(self, value=None) -> None:
        self.oracle_base.connection.client_identifier = value

    @keyword
    def oracle_connection_current_schema(self, value=None) -> None:
        if value:
            self.oracle_base.connection.current_schema = value
        return self.oracle_base.connection.current_schema

    @keyword
    def oracle_connection_dsn(self) -> None:
        return self.oracle_base.connection.dsn

    @keyword
    def oracle_connection_edition(self) -> None:
        return self.oracle_base.connection.edition

    @keyword
    def oracle_connection_encoding(self) -> None:
        return self.oracle_base.connection.encoding

    @keyword
    def oracle_connection_external_name(self, value=None) -> None:
        if value:
            self.oracle_base.connection.external_name = value
        return self.oracle_base.connection.external_name

    @keyword
    def oracle_connection_internal_name(self, value=None) -> None:
        if value:
            self.oracle_base.connection.internal_name = value
        return self.oracle_base.connection.internal_name

    @keyword
    def oracle_connection_ltxid(self, value=None) -> None:
        self.oracle_base.connection.ltxid = value

    @keyword
    def oracle_connection_maxBytesPerCharacter(self, value=None) -> None:
        self.oracle_base.connection.maxBytesPerCharacter = value

    @keyword
    def oracle_connection_module(self, value=None) -> None:
        self.oracle_base.connection.module = value

    @keyword
    def oracle_connection_nencoding(self) -> None:
        return self.oracle_base.connection.nencoding

    @keyword
    def oracle_connection_stmcachesize(self, value=None) -> None:
        if value:
            self.oracle_base.connection.stmtcachesize = value
        return self.oracle_base.connection.stmtcachesize

    @keyword
    def oracle_connection_tag(self, value=None) -> None:
        if value:
            self.oracle_base.connection.tag = value
        return self.oracle_base.connection.tag

    @keyword
    def oracle_connection_tnsentry(self) -> None:
        return self.oracle_base.connection.tnsentry

    @keyword
    def oracle_connection_username(self) -> None:
        return self.oracle_base.connection.username

    @keyword
    def oracle_connection_version(self) -> None:
        return self.oracle_base.connection.version
