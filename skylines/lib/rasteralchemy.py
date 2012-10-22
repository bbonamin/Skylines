from sqlalchemy import event
from sqlalchemy.types import UserDefinedType
from sqlalchemy.schema import DDL


class Raster(UserDefinedType):
    def get_col_spec(self):
        return "raster"


def RasterDDL(table):
    for column in table.columns:
        if type(column.type) == Raster:
            ddl = DDL("CREATE INDEX {0}_{1}_gist ON {0} USING gist(ST_CONVEXHULL({1}))" \
                      .format(table.name, column.name))
            event.listen(table, "after_create", ddl)
