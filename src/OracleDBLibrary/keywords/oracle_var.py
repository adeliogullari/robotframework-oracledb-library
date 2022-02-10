import cx_Oracle
from typing import Any
from robotlibcore import keyword
from ..base.oracle_base import OracleBase


class OracleVarKeywords:

    def __init__(self):
        self.oracle_base = OracleBase()

    @keyword
    def oracle_var(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.var = cx_Oracle.Var(*args, **kwargs)

    @keyword
    def oracle_var_copy(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.var.copy(*args, **kwargs)

    @keyword
    def oracle_var_getvalue(self, *args: Any, **kwargs: Any) -> None:
        return self.oracle_base.var.getvalue(*args, **kwargs)

    @keyword
    def oracle_var_setvalue(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.var.setvalue(*args, **kwargs)

    @keyword
    def oracle_var_actual_elements(self) -> None:
        return self.oracle_base.var.actual_elements

    @keyword
    def oracle_var_buffer_size(self) -> None:
        return self.oracle_base.var.buffer_size

    @keyword
    def oracle_var_inconverter(self, value=None) -> None:
        if value:
            self.oracle_base.var.inconverter = value
        return self.oracle_base.var.inconverter

    @keyword
    def oracle_var_num_elements(self) -> None:
        return self.oracle_base.var.num_elements

    @keyword
    def oracle_var_outconverter(self, value=None) -> None:
        if value:
            self.oracle_base.var.outconverter = value
        return self.oracle_base.var.outconverter

    @keyword
    def oracle_var_size(self) -> None:
        return self.oracle_base.var.size

    @keyword
    def oracle_var_type(self) -> None:
        return self.oracle_base.var.type

    @keyword
    def oracle_var_values(self) -> None:
        return self.oracle_base.var.values
