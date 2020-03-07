from json import loads
from utilities import *


# This method starts the code running
def getApexCode(inputJson):
    apex = "public JSONGenerator getJsonGen(){\n"
    apex += "    JSONGenerator gen = JSON.createGenerator(true);\n"
    print( type(inputJson) )
    #try:
    y = loads(inputJson)
   # except ValueError as err:
    #    return 'Error in Json decoding, please check.'+ str(err.__str__)
    if type(y) is list:
        apex += startingArray
        if len(y) > 0 and (type(y[0]) is dict):
            for i in y:
                apex += startObject
                apex += funToCheck(i)
                apex += endObject

        else:
            listType = getListType(y)
            values = str(y).replace("[", "").replace("]", "")
            apex += writeObject("new List<" + listType + ">{" + values + "}")
        apex += endingArray
    elif type(y) is dict:
        apex += startObject
        apex += funToCheck(y)
        apex += endObject
    elif type(y) is str:
        apex += writeString(y)
    elif type(y) is int:
        apex += writeNumber(y)
    elif type(y) is bool:
        apex += writeBoolean(y)
    apex += '   return gen;\n'
    return apex + '}'


# This method recursively generates the code
def funToCheck(j):
    apex = ""
    for x in j.keys():

        if type(j.get(x)) is dict:
            apex += writeFieldName(x)
            apex += startObject
            apex += funToCheck(j.get(x))
            apex += endObject

        elif type(j.get(x)) is list:
            if len(j.get(x)) == 0:
                apex += writeFieldName(x)
                apex += startingArray
                apex += endingArray
            elif len(j.get(x)) > 0 and type(j.get(x)[0]) is dict:
                apex += writeFieldName(x)
                apex += startingArray
                for i in j.get(x):
                    apex += startObject
                    apex += funToCheck(i)
                    apex += endObject
                apex += endingArray
            else:
                listType = getListType(j.get(x))
                if listType is not None:
                    values = str(j.get(x)).replace("[", "").replace("]", "")
                    apex += writeObjectField(x, "new List<" + listType + ">{" + values + "}")

        elif type(j.get(x)) is str:
            apex += writeStringField(x, str(j.get(x)))
        elif type(j.get(x)) is int:
            apex += writeNumberField(x, str(j.get(x)))
        elif type(j.get(x)) is bool:
            apex += writeBooleanField(x, str(j.get(x)))
        elif j.get(x) is None:
            apex += writeNullField(x)

    return apex
