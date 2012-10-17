from sqlalchemy.sql import ColumnElement, func
from sqlalchemy.ext.compiler import compiles
from sqlalchemy.orm.properties import ColumnProperty


class extract_field(ColumnElement):
    def __init__(self, base, field):
        self.base = base
        self.field = field
        # throws an error unless declared...
        self.type = None


@compiles(extract_field)
def compile(expr, compiler, **kw):
    return '(' + compiler.process(expr.base) + ').' + expr.field


class extract_array_item(ColumnElement):
    def __init__(self, array, index):
        self.array = array
        self.index = index
        # throws an error unless declared...
        self.type = None


@compiles(extract_array_item)
def compile(expr, compiler, **kw):
    return compiler.process(expr.array) + '[' + str(expr.index) + ']'


class cast(ColumnElement):
    def __init__(self, base, field):
        self.base = base
        self.field = field
        # throws an error unless declared...
        self.type = None


@compiles(cast)
def compile(expr, compiler, **kw):
    return '(' + compiler.process(expr.base) + ')::' + expr.field


class LowerCaseComparator(ColumnProperty.Comparator):
    def __eq__(self, other):
        return func.lower(self.__clause_element__()) == func.lower(other)
