try:
    import pysqlite3  # type: ignore
    import sys

    sys.modules["sqlite3"] = pysqlite3
    sys.modules["sqlite3.dbapi2"] = pysqlite3
except ImportError:
    pass
