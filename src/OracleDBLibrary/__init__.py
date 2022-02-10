import cx_Oracle
from robot.api import logger
from robotlibcore import DynamicCore
from .keywords import OracleConnectionKeywords, OracleCursorKeywords, OracleSessionPoolKeywords, OracleVarKeywords
from .mapper import ArgumentMapper
from .base import OracleBase


__version__ = "1.0.0"


class OracleDBLibrary(DynamicCore):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):

        DynamicCore.__init__(self, [OracleConnectionKeywords(),
                                    OracleCursorKeywords(),
                                    OracleSessionPoolKeywords(),
                                    OracleVarKeywords()])

    def run_keyword(self, name, args, kwargs=None):

        ArgumentMapper.map_argument(kwargs, cx_Oracle)
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except cx_Oracle.DatabaseError as e:
            logger.error(f"Oracle Error Code: {e.args[0].code}")
            logger.error(f"Oracle Error Message: {e.args[0].message}")
            raise
