from sqlalchemy import Column
from sqlalchemy.types import Integer
from skylines.model.base import DeclarativeBase
from skylines.lib.rasteralchemy import Raster, RasterDDL


class Elevation(DeclarativeBase):
    __tablename__ = 'elevations'

    rid = Column(Integer, autoincrement=True, primary_key=True)
    rast = Column(Raster)


RasterDDL(Elevation.__table__)
