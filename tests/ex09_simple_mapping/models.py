import related


@related.immutable
class Settings(object):
    devices = related.MappingField(str, "name")
