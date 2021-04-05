QUOTED_HELP_MSG = '''


            \'{"menu": {'+
                '"id": "file",'+
                '"value": "File",'+
                '"popup": {'+
                  '"menuitem": ['+
                    '{"value": "New", "onclick": "CreateNewDoc()"},'+
                    '{"value": "Open", "onclick": "OpenDoc()"},'+
                    '{"value": "Close", "onclick": "CloseDoc()"}'+
                  ']'+
                '}'+
            '}}\'
            '''

GEN_API_ENDPOINT = '/api/generateApexAPI'
GEN_STARTERS = "public JSONGenerator getJsonGen(){\n    JSONGenerator gen = JSON.createGenerator(true);\n"
JSON_ERROR = "Error in Json decoding, please check."