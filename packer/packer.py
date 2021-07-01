import os
import importlib
import csv, json, struct

def pack(path=None, projectName=None, randomizer=False):
    projectDir = f'projects/{projectName}/tmp/text' if randomizer else f'projects/{projectName}/text'
    os.makedirs(f'{path}/data/text/dat_en', exist_ok=True)
    for name in [f.name for f in os.scandir(projectDir) if f.is_dir() and not f.name.startswith('tmp')]:
        file = path + '/data/text/dat_en/t_' + name + '.tbl'
        inputPath = f'{projectDir}/{name}/'

        schemaFile = importlib.import_module('schema.' + name)
        headers = schemaFile.headers
        schemas = []
        
        for header in headers:
            schemas.append(eval('schemaFile.' + header))
        
        with open(file, 'wb') as dataFile:
            with open(inputPath + 'summary.json', 'r') as summaryFile:
                summary = json.load(summaryFile)
                dataFile.write(int(summary['total']).to_bytes(2, 'little'))

                keys = list(summary.keys())[1:-1]
                dataFile.write(len(keys).to_bytes(2, 'little'))
                dataFile.write(b'\x00\x00')

                for key in keys:
                    dataFile.write(key.encode('utf-8'))
                    dataFile.write(b'\x00')
                    dataFile.write(summary[key].to_bytes(2, 'little'))
                    dataFile.write(b'\x00\x00')

            for i in range(len(headers)):
                header = headers[i]
                schema = schemas[i]
                with open(inputPath + header + '.csv', 'r', newline='', encoding='utf-8') as headerFile:
                    fieldNames = list(schema.keys())
                    data = list(csv.DictReader(headerFile))

                    for entry in data:
                        length = 0
                        for key in fieldNames:
                            if schema[key] == 'b':
                                length += 1
                            elif schema[key] == 's':
                                length += 2
                            elif schema[key] == 'i' or schema[key] == 'f':
                                length += 4
                            elif schema[key] == 't':
                                length += len(entry[key].encode('utf-8')) + 1
                            elif schema[key] == 'd':
                                length += len(entry[key].split(' '))
                        dataFile.write(header.encode('utf-8'))
                        dataFile.write(b'\x00')
                        dataFile.write(length.to_bytes(2, 'little'))

                        for key in fieldNames:
                            if schema[key] == 'd':
                                hexText = entry[key]
                                hexText = hexText.replace(' ', '')
                                byteText = bytes.fromhex(hexText)
                                dataFile.write(byteText)
                            elif schema[key] == 'b':
                                dataFile.write(int(entry[key]).to_bytes(1, 'little'))
                            elif schema[key] == 's':
                                dataFile.write(int(entry[key]).to_bytes(2, 'little'))
                            elif schema[key] == 'i':
                                dataFile.write(int(entry[key]).to_bytes(4, 'little'))
                            elif schema[key] == 'f':
                                dataFile.write(struct.pack('<f', float(entry[key])))
                            elif schema[key] == 't':
                                dataFile.write(entry[key].encode('utf-8'))
                                dataFile.write(b'\x00')
                            else:
                                moduleName = schema[key]
                                moduleSchema = eval('schemaFile.' + moduleName)

                                subPath = inputPath + moduleName + '/'

                                subFileName = None
                                if isinstance(moduleSchema['uid'], str):
                                    if moduleSchema['uid'][0] == '#':
                                        subFileName = entry[fieldNames[int(moduleSchema['uid'][1:])]]
                                else:
                                    subFileName = moduleSchema['uid']
                                subFieldNames = list(moduleSchema.keys())[2:]

                                with open(subPath + str(subFileName) + '.csv', 'r', newline='', encoding='utf-8') as subFile:
                                    subData = list(csv.DictReader(subFile))

                                    for subEntry in subData:
                                        length = 0
                                        for subKey in subFieldNames:
                                            if moduleSchema[subKey] == 'b':
                                                length += 1
                                            elif moduleSchema[subKey] == 's':
                                                length += 2
                                            elif moduleSchema[subKey] == 'i' or moduleSchema[subKey] == 'f':
                                                length += 4
                                            elif moduleSchema[subKey] == 't':
                                                length += len(subEntry[subKey].encode('utf-8')) + 1
                                            elif moduleSchema[subKey] == 'd':
                                                length += len(subEntry[subKey].split(' '))
                                        dataFile.write(moduleName.encode('utf-8'))
                                        dataFile.write(b'\x00')
                                        dataFile.write(length.to_bytes(2, 'little'))

                                        for subKey in subFieldNames:
                                            if moduleSchema[subKey] == 'd':
                                                hexText = subEntry[subKey]
                                                hexText = hexText.replace(' ', '')
                                                byteText = bytes.fromhex(hexText)
                                                dataFile.write(byteText)
                                            elif moduleSchema[subKey] == 'b':
                                                dataFile.write(int(subEntry[subKey]).to_bytes(1, 'little'))
                                            elif moduleSchema[subKey] == 's':
                                                dataFile.write(int(subEntry[subKey]).to_bytes(2, 'little'))
                                            elif moduleSchema[subKey] == 'i':
                                                dataFile.write(int(subEntry[subKey]).to_bytes(4, 'little'))
                                            elif moduleSchema[subKey] == 'f':
                                                dataFile.write(struct.pack('<f', float(subEntry[subKey])))
                                            elif moduleSchema[subKey] == 't':
                                                dataFile.write(subEntry[subKey].encode('utf-8'))
                                                dataFile.write(b'\x00')
    print('Pack Done')