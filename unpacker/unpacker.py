import os, io
import importlib, collections
import csv, json, struct

def unpack(path=None, projectName=None):
    moduleList = ['attach', 'item_en', 'magic', 'mons', 'mstqrt', 'name', 'orb', 'slot', 'status']
    for name in moduleList:
        file = f'{path}/data/text/dat_en/t_{name}.tbl'
        outputPath = f'projects/{projectName}/text/{name}/'

        os.makedirs(outputPath, exist_ok=True)

        schemaFile = importlib.import_module('schema.' + name)
        headers = schemaFile.headers
        schemas = []
        rows = []
        
        for header in headers:
            schemas.append(eval('schemaFile.' + header))
            rows.append(list())
        
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

            i = 0
            while i < totalEntries:
                i += 1
                print(i)
                chunks = data.split(b'\x00', maxsplit=1)
                data = io.BytesIO(chunks[1])
                header = chunks[0].decode('utf-8')
                schema = schemas[headers.index(header)]
                fieldNames = list(schema.keys())
                length = int.from_bytes(data.read(2), 'little')
                headerData = io.BytesIO(data.read(length))

                rowData = list()
                row = {}

                for key in fieldNames:
                    if schema[key].startswith('d'):
                        if len(schema[key]) > 1:
                            n = int(schema[key][1:])
                            hexText = headerData.read(n).hex()
                        else:
                            hexText = headerData.read().hex()
                        hexText = ' '.join(hexText[j:j+2] for j in range(0, len(hexText), 2)).upper()
                        rowData.append(hexText)
                    elif schema[key] == 'b':
                        rowData.append(int.from_bytes(headerData.read(1), 'little'))
                    elif schema[key] == 's':
                        rowData.append(int.from_bytes(headerData.read(2), 'little'))
                    elif schema[key] == 'S':
                        rowData.append(int.from_bytes(headerData.read(2), 'little', signed=True))
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
                                loopAmount = -1
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

                            while loopAmount != 0:
                                originalPos = data.tell()
                                text = data.read(len(moduleName)).decode('utf-8')
                                data.read(1)
                                if text != moduleName:
                                    loopAmount = 0
                                    data.seek(originalPos)
                                    continue
                                if loopAmount > 0:
                                    loopAmount -= 1
                                i += 1
                                length = int.from_bytes(data.read(2), 'little')
                                subData = io.BytesIO(data.read(length))

                                subRowData = list()
                                subRow = {}

                                for subKey in subFieldNames:
                                    if moduleSchema[subKey].startswith('d'):
                                        if len(moduleSchema[subKey]) > 1:
                                            n = int(moduleSchema[subKey][1:])
                                            hexText = subData.read(n).hex()
                                        else:
                                            hexText = subData.read().hex()
                                        hexText = ' '.join(hexText[j:j+2] for j in range(0, len(hexText), 2)).upper()
                                        subRowData.append(hexText)
                                    elif moduleSchema[subKey] == 'b':
                                        subRowData.append(int.from_bytes(subData.read(1), 'little'))
                                    elif moduleSchema[subKey] == 's':
                                        subRowData.append(int.from_bytes(subData.read(2), 'little'))
                                    elif moduleSchema[subKey] == 'S':
                                        subRowData.append(int.from_bytes(subData.read(2), 'little', signed=True))
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
                rows[headers.index(header)].append(row)

                data = data.read()
            
            for i in range(len(headers)):
                header = headers[i]
                schema = schemas[i]
                rowList = rows[i]
                with open(outputPath + header + '.csv', 'w', newline='', encoding='utf-8') as headerFile:
                    fieldNames = list(schema.keys())
                    writer = csv.DictWriter(headerFile, fieldnames=fieldNames)
                    writer.writeheader()
                    writer.writerows(rowList)
                    