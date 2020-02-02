startingArray = '    gen.writeStartArray();\n'
endingArray = '    gen.writeEndArray();\n'
startObject = '    gen.writeStartObject();\n'
endObject = '    gen.writeEndObject();\n'


def writeObject(value):
    return "    gen.writeObject(" + value + ");\n"


def writeString(value):
    return "    gen.writeString('" + value + "');\n"


def writeNumber(value):
    return "    gen.writeNumber(" + value + ");\n"


def writeFieldName(value):
    return "    gen.writeFieldName('" + value + "');\n"


def writeStringField(key, value):
    return "    gen.writeStringField('" + key + "', '" + value + "');\n"


def writeNumberField(key, value):
    return "    gen.writeNumberField('" + key + "', " + value + ");\n"


def writeObjectField(key, value):
    return "    gen.writeObjectField('" + key + "', " + value + ");\n"


def writeNullField(key):
    return "    gen.writeNullField('" + key + "');\n"


def writeBoolean(value):
    return "    gen.writeBoolean(" + value + ");\n"


def writeBooleanField(key, value):
    return "    gen.writeBooleanField('" + key + "', " + value + ");\n"


def getListType(givenList):
    for k in givenList:
        if k is not None:
            if type(k) is str:
                return "String"
            elif type(k) is int:
                return "Integer"
            elif type(k) is bool:
                return "Boolean"
            elif type(k) is float:
                return "Decimal"
    return None
