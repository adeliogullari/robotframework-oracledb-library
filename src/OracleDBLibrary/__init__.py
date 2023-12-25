import oracledb
from robot.api import logger
from robotlibcore import DynamicCore
from .keywords import OracleConnectionKeywords, OracleCursorKeywords, OracleSessionPoolKeywords, OracleVarKeywords
from .mapper import ArgumentMapper
from .base import OracleBase


__version__ = "0.1.4"


class OracleDBLibrary(DynamicCore):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):

        DynamicCore.__init__(self, library_components=[OracleConnectionKeywords(),
                                                       OracleCursorKeywords(),
                                                       OracleSessionPoolKeywords(),
                                                       OracleVarKeywords()])

    def run_keyword(self, name, args, kwargs=None):

        ArgumentMapper.map_argument(kwargs, oracledb)
        try:
            return DynamicCore.run_keyword(self, name, args, kwargs)
        except oracledb.DatabaseError as e:
            logger.error(f"Oracle Error Code: {e.args[0].code}")
            logger.error(f"Oracle Error Message: {e.args[0].message}")
            raise
