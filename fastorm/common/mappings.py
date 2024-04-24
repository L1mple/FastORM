from fastorm.common.enums import ColumnTypeEnum, PythonTypeEnum

TO_PYTHON = {
    ColumnTypeEnum.BIGINT: PythonTypeEnum.INT,
    ColumnTypeEnum.BIGSERIAL: PythonTypeEnum.INT,
    ColumnTypeEnum.BIT: PythonTypeEnum.STR,
    ColumnTypeEnum.BITVAR: PythonTypeEnum.STR,
    ColumnTypeEnum.BOOLEAN: PythonTypeEnum.BOOL,
    ColumnTypeEnum.BOX: PythonTypeEnum.TUPLE,
    ColumnTypeEnum.BYTEA: PythonTypeEnum.BYTES,
    ColumnTypeEnum.CHAR: PythonTypeEnum.STR,
    ColumnTypeEnum.VARCHAR: PythonTypeEnum.STR,
    ColumnTypeEnum.CIDR: PythonTypeEnum.STR,
    ColumnTypeEnum.CIRCLE: PythonTypeEnum.TUPLE,
    ColumnTypeEnum.DATE: PythonTypeEnum.DATE,
    ColumnTypeEnum.DOUBLE_PRECISION: PythonTypeEnum.FLOAT,
    ColumnTypeEnum.INET: PythonTypeEnum.STR,
    ColumnTypeEnum.INTEGER: PythonTypeEnum.INT,
    ColumnTypeEnum.INTERVAL: PythonTypeEnum.ANY,  # TODO
    ColumnTypeEnum.JSON: PythonTypeEnum.DICT,
    ColumnTypeEnum.JSONB: PythonTypeEnum.DICT,
    ColumnTypeEnum.LINE: PythonTypeEnum.TUPLE,
    ColumnTypeEnum.LSEG: PythonTypeEnum.TUPLE,
    ColumnTypeEnum.MACADDR: PythonTypeEnum.STR,
    ColumnTypeEnum.MONEY: PythonTypeEnum.STR,
    ColumnTypeEnum.NUMERIC: PythonTypeEnum.FLOAT,
    ColumnTypeEnum.PATH: PythonTypeEnum.TUPLE,
    ColumnTypeEnum.PG_LSN: PythonTypeEnum.STR,
    ColumnTypeEnum.PG_SNAPSHOT: PythonTypeEnum.STR,
    ColumnTypeEnum.POINT: PythonTypeEnum.TUPLE,
    ColumnTypeEnum.POLYGON: PythonTypeEnum.TUPLE,
    ColumnTypeEnum.REAL: PythonTypeEnum.FLOAT,
    ColumnTypeEnum.SMALLINT: PythonTypeEnum.INT,
    ColumnTypeEnum.SMALLSERIAL: PythonTypeEnum.INT,
    ColumnTypeEnum.SERIAL: PythonTypeEnum.INT,
    ColumnTypeEnum.TEXT: PythonTypeEnum.STR,
    ColumnTypeEnum.TIME: PythonTypeEnum.DATETIME,
    ColumnTypeEnum.TIMESTAMP: PythonTypeEnum.DATETIME,
    ColumnTypeEnum.TSQUERY: PythonTypeEnum.STR,
    ColumnTypeEnum.TSVECTOR: PythonTypeEnum.ANY,  # TODO
    ColumnTypeEnum.TXID_SNAPSHOT: PythonTypeEnum.STR,
    ColumnTypeEnum.UUID: PythonTypeEnum.UUID,
    ColumnTypeEnum.XML: PythonTypeEnum.ANY,  # TODO
}