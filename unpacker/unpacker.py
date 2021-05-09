import os, glob, io, pkgutil
import importlib, collections
import csv, json, struct

def unpack(path=None, projectName=None):
    moduleList = ['magic']
    for name in moduleList:
        file = path + '/data/text/dat_en/t_' + name + '.tbl'
        outputPath = 'projects/' + projectName + '/' + name + '/'

        os.makedirs('projects/' + projectName + '/' + name + '/', exist_ok=True)

        schemaFile = importlib.import_module('schema.' + name)
        headers = schemaFile.headers
        schemas = []
        
        for header in headers:
            schemas.append(eval('schemaFile.' + header))
        
        with open(file, 'rb') as dataFile:
            totalEntries = int.from_bytes(dataFile.read(2), 'little')
            entryTypeNum = int.from_bytes(dataFile.read(2), 'little')
            dataFile.read(2)

            data = dataFile.read()

            with open(outputPath + 'summary.json', 'w') as summaryFile:
                entryNum = 0
                summary = collections.OrderedDict()
                summary['total'] = totalEntries
                for i in range(entryTypeNum):
                    chunks = data.split(b'\x00', maxsplit=1)
                    data = io.BytesIO(chunks[1])
                    entryType = chunks[0].decode('utf-8')
                    typeLength = int.from_bytes(data.read(2), 'little')
                    entryNum += typeLength

                    summary[entryType] = typeLength

                    data.read(2)
                    data = data.read()
                
                if entryNum == totalEntries:
                    summary['result'] = 'No Error'
                else:
                    summary['result'] = 'Header Mismatch'

                json.dump(summary, summaryFile, indent='\t')

            for i in range(len(headers)):
                header = headers[i]
                schema = schemas[i]
                with open(outputPath + header + '.csv', 'w', newline='', encoding='utf-8') as headerFile:
                    fieldNames = list(schema.keys())
                    data = io.BytesIO(data)
                    writer = csv.DictWriter(headerFile, fieldnames=fieldNames)
                    writer.writeheader()

                    for j in range(summary[header]):
                        data.read(len(header) + 1)
                        length = int.from_bytes(data.read(2), 'little')
                        headerData = io.BytesIO(data.read(length))

                        rowData = list()
                        row = {}

                        for key in fieldNames:
                            if schema[key] == 'd':
                                hexText = headerData.read().hex()
                                hexText = ' '.join(hexText[j:j+2] for j in range(0, len(hexText), 2)).upper()
                                rowData.append(hexText)
                                break
                            elif schema[key] == 'b':
                                rowData.append(int.from_bytes(headerData.read(1), 'little'))
                            elif schema[key] == 's':
                                rowData.append(int.from_bytes(headerData.read(2), 'little'))
                            elif schema[key] == 'i':
                                rowData.append(int.from_bytes(headerData.read(4), 'little'))
                            elif schema[key] == 'f':
                                rowData.append(struct.unpack('<f', headerData.read(4))[0])
                            elif schema[key] == 't':
                                headerData = headerData.read()
                                chunks = headerData.split(b'\x00', maxsplit=1)
                                rowData.append(chunks[0].decode('utf-8'))
                                headerData = io.BytesIO(chunks[1])
                            else:
                                moduleName = schema[key]
                                moduleSchema = eval('schemaFile.' + moduleName)

                                loopAmount = None
                                if isinstance(moduleSchema['size'], str):
                                    if moduleSchema['size'][0] == '#':
                                        loopAmount = rowData[int(moduleSchema['size'][1:])]
                                    elif moduleSchema['size'][0] == '?':
                                        parts = moduleSchema['size'].split('?')
                                        if rowData[int(parts[1])] in schemaFile.ref:
                                            loopAmount = int(parts[2])
                                        else:
                                            loopAmount = int(parts[3])
                                else:
                                    loopAmount = moduleSchema['size']

                                subPath = outputPath + moduleName + '/'
                                if not os.path.exists(subPath):
                                    os.mkdir(subPath)

                                subFileName = None
                                if isinstance(moduleSchema['uid'], str):
                                    if moduleSchema['uid'][0] == '#':
                                        subFileName = rowData[int(moduleSchema['uid'][1:])]
                                else:
                                    subFileName = moduleSchema['uid']
                                subFieldNames = list(moduleSchema.keys())[2:]

                                with open(subPath + str(subFileName) + '.csv', 'w', newline='', encoding='utf-8') as subFile:
                                    subWriter = csv.DictWriter(subFile, fieldnames=subFieldNames)
                                    subWriter.writeheader()

                                    for k in range(loopAmount):
                                        data.read(len(moduleName) + 1)
                                        length = int.from_bytes(data.read(2), 'little')
                                        subData = io.BytesIO(data.read(length))

                                        subRowData = list()
                                        subRow = {}

                                        for subKey in subFieldNames:
                                            if moduleSchema[subKey] == 'd':
                                                hexText = subData.read().hex()
                                                hexText = ' '.join(hexText[j:j+2] for j in range(0, len(hexText), 2)).upper()
                                                subRowData.append(hexText)
                                                break
                                            elif moduleSchema[subKey] == 'b':
                                                subRowData.append(int.from_bytes(subData.read(1), 'little'))
                                            elif moduleSchema[subKey] == 's':
                                                subRowData.append(int.from_bytes(subData.read(2), 'little'))
                                            elif moduleSchema[subKey] == 'i':
                                                subRowData.append(int.from_bytes(subData.read(4), 'little'))
                                            elif moduleSchema[subKey] == 'f':
                                                subRowData.append(struct.unpack('<f', subData.read(4))[0])
                                            elif moduleSchema[subKey] == 't':
                                                subData = subData.read()
                                                chunks = subData.split(b'\x00', maxsplit=1)
                                                subRowData.append(chunks[0].decode('utf-8'))
                                                subData = io.BytesIO(chunks[1])

                                        for l in range(len(subRowData)):
                                            subRow[subFieldNames[l]] = subRowData[l]
                                        subWriter.writerow(subRow)


                        for j in range(len(rowData)):
                            row[fieldNames[j]] = rowData[j]
                        writer.writerow(row)

                data = data.read()
    print('Unpack Done')