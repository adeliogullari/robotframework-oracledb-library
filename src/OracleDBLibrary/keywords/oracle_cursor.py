from typing import Any
from robotlibcore import keyword
from ..base.oracle_base import OracleBase


class OracleCursorKeywords:

    def __init__(self):
        self.oracle_base = OracleBase()

    @keyword
    def oracle_cursor_arrayvar(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.arrayvar(*args, **kwargs)

    @keyword
    def oracle_cursor_bindnames(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.bindnames(*args, **kwargs)

    @keyword
    def oracle_cursor_callfunc(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.callfunc(*args, **kwargs)

    @keyword
    def oracle_cursor_callproc(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.callproc(*args, **kwargs)

    @keyword
    def oracle_cursor_close(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.cursor.close(*args, **kwargs)

    @keyword
    def oracle_cursor_execute(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.execute(*args, **kwargs)

    @keyword
    def oracle_cursor_executemany(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.executemany(*args, **kwargs)

    @keyword
    def oracle_cursor_executemanyprepared(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.executemanyprepared(*args, **kwargs)

    @keyword
    def oracle_cursor_fetchall(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.fetchall(*args, **kwargs)

    @keyword
    def oracle_cursor_fetchmany(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.fetchmany(*args, **kwargs)

    @keyword
    def oracle_cursor_fetchone(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.fetchone(*args, **kwargs)

    @keyword
    def oracle_cursor_fetchraw(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.fetchraw(*args, **kwargs)

    @keyword
    def oracle_cursor_getarraydmlrowcounts(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.getarraydmlrowcounts(*args, **kwargs)

    @keyword
    def oracle_cursor_getbatcherrors(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.getbatcherrors(*args, **kwargs)

    @keyword
    def oracle_cursor_getimplicitresults(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.getimplicitresults(*args, **kwargs)

    @keyword
    def oracle_cursor_parse(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.cursor.parse(*args, **kwargs)

    @keyword
    def oracle_cursor_prepare(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.cursor.prepare(*args, **kwargs)

    @keyword
    def oracle_cursor_scroll(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.cursor.scroll(*args, **kwargs)

    @keyword
    def oracle_cursor_setinputsizes(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.cursor.setinputsizes(*args, **kwargs)

    @keyword
    def oracle_cursor_setoutputsize(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.cursor.setoutputsize(*args, **kwargs)

    @keyword
    def oracle_cursor_var(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.var = self.oracle_base.cursor.var(*args, **kwargs)

    @keyword
    def oracle_cursor_arraysize(self, value=None) -> None:
        if value:
            self.oracle_base.cursor.arraysize = value
        return self.oracle_base.cursor.arraysize

    @keyword
    def oracle_cursor_bindarraysize(self, value=None) -> None:
        if value:
            self.oracle_base.cursor.bindarraysize = value
        return self.oracle_base.cursor.bindarraysize

    @keyword
    def oracle_cursor_bindvars(self) -> None:
        return self.oracle_base.cursor.bindvars

    @keyword
    def oracle_cursor_description(self) -> None:
        return self.oracle_base.cursor.description

    @keyword
    def oracle_cursor_fetchvars(self) -> None:
        return self.oracle_base.cursor.fetchvars

    @keyword
    def oracle_cursor_lastrowid(self) -> None:
        return self.oracle_base.cursor.lastrowid

    @keyword
    def oracle_cursor_prefetchrows(self, value=None) -> None:
        if value:
            self.oracle_base.cursor.prefetchrows = value
        return self.oracle_base.cursor.prefetchrows

    @keyword
    def oracle_cursor_rowcount(self) -> None:
        return self.oracle_base.cursor.rowcount

    @keyword
    def oracle_cursor_rowfactory(self, value=None) -> None:
        if value:
            self.oracle_base.cursor.rowfactory = value
        return self.oracle_base.cursor.rowfactory

    @keyword
    def oracle_cursor_scrollable(self, value=None) -> None:
        if value:
            self.oracle_base.cursor.scrollable = value
        return self.oracle_base.cursor.scrollable

    @keyword
    def oracle_cursor_statement(self) -> None:
        return self.oracle_base.cursor.statement
