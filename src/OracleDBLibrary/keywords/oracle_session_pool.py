import oracledb
from typing import Any
from robotlibcore import keyword
from ..base import OracleBase


class OracleSessionPoolKeywords:

    def __init__(self):
        self.oracle_base = OracleBase()

    @keyword
    def oracle_session_pool(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.session_pool = oracledb.SessionPool(*args, **kwargs)

    @keyword
    def oracle_session_pool_acquire(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.connection = self.oracle_base.session_pool.acquire(*args, **kwargs)

    @keyword
    def oracle_session_pool_close(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.session_pool.close(*args, **kwargs)

    @keyword
    def oracle_session_pool_drop(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.session_pool.drop(*args, **kwargs)

    @keyword
    def oracle_session_pool_reconfigure(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.session_pool.reconfigure(*args, **kwargs)

    @keyword
    def oracle_session_pool_release(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.session_pool.release(*args, **kwargs)

    @keyword
    def oracle_session_pool_busy(self) -> None:
        return self.oracle_base.session_pool.busy

    @keyword
    def oracle_session_pool_dsn(self) -> None:
        return self.oracle_base.session_pool.dsn

    @keyword
    def oracle_session_pool_getmode(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.getmode = value
        return self.oracle_base.session_pool.getmode

    @keyword
    def oracle_session_pool_homogeneous(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.homogeneous = value
        return self.oracle_base.session_pool.homogeneous

    @keyword
    def oracle_session_pool_increment(self) -> None:
        return self.oracle_base.session_pool.increment

    @keyword
    def oracle_session_pool_max(self) -> None:
        return self.oracle_base.session_pool.max

    @keyword
    def oracle_session_pool_max_lifetime_session(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.max_lifetime_session = value
        return self.oracle_base.session_pool.max_lifetime_session

    @keyword
    def oracle_session_pool_max_sessions_per_shard(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.max_sessions_per_shard = value
        return self.oracle_base.session_pool.max_sessions_per_shard

    @keyword
    def oracle_session_pool_min(self) -> None:
        return self.oracle_base.session_pool.min

    @keyword
    def oracle_session_pool_name(self) -> None:
        return self.oracle_base.session_pool.name

    @keyword
    def oracle_session_pool_opened(self) -> None:
        return self.oracle_base.session_pool.opened

    @keyword
    def oracle_session_pool_ping_interval(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.ping_interval = value
        return self.oracle_base.session_pool.ping_interval

    @keyword
    def oracle_session_pool_stmtcachesize(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.stmtcachesize = value
        return self.oracle_base.session_pool.stmtcachesize

    @keyword
    def oracle_session_pool_timeout(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.timeout = value
        return self.oracle_base.session_pool.timeout

    @keyword
    def oracle_session_pool_tnsentry(self) -> None:
        return self.oracle_base.session_pool.tnsentry

    @keyword
    def oracle_session_pool_username(self) -> None:
        return self.oracle_base.session_pool.username

    @keyword
    def oracle_session_pool_wait_timeout(self, value=None) -> None:
        if value:
            self.oracle_base.session_pool.wait_timeout = value
        return self.oracle_base.session_pool.wait_timeout
