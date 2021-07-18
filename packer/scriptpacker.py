import os, json
from frames.packer import Frame

def pack(frame: Frame,path=None, projectName=None, randomizer=False, moduleList=[], decompiler=True):
    projectDir = f'projects/{projectName}/tmp/scripts' if randomizer else f'projects/{projectName}/scripts'
    for scriptFolder in moduleList:
        gamePath = f'{path}/data/scripts/{scriptFolder}/dat_en'
        os.makedirs(gamePath, exist_ok=True)

        if not decompiler:
            for filename in [f.name for f in os.scandir(f'{projectDir}/{scriptFolder}') if f.is_dir()]:
        
                files = [f.name for f in os.scandir(f'{projectDir}/{scriptFolder}/{filename}') if f.is_file() and not f.name == 'summary.json']
                files.sort(key=lambda x: int(x.split('.')[0]))

                names = list()
                datas = list()

                for file in files:
                    with open(f'{projectDir}/{scriptFolder}/{filename}/{file}', 'rb') as inFile:
                        datas.append(inFile.read())

                        name = ""
                        if '.' in file:
                            name = file.split('.', maxsplit=1)[1]
                        names.append(name)
                
                with open(f'{gamePath}/{filename}', 'w+b') as outputFile, open(f'{projectDir}/{scriptFolder}/{filename}/summary.json', 'r') as summaryFile:
                    summary = json.load(summaryFile)
                    num32 = 32

                    outputFile.write(num32.to_bytes(4, 'little'))
                    outputFile.write(num32.to_bytes(4, 'little'))

                    fname = filename.split('.')[0]

                    fileLength = len(fname)
                    startOffset = num32 + fileLength + 1
                    outputFile.write(startOffset.to_bytes(4, 'little'))

                    fileCount = len(files)
                    table1Length = 4 * fileCount
                    outputFile.write(table1Length.to_bytes(4, 'little'))

                    startOffset2 = startOffset + table1Length
                    outputFile.write(startOffset2.to_bytes(4, 'little'))
                    outputFile.write(fileCount.to_bytes(4, 'little'))

                    outputFile.seek(startOffset2 + 2 * fileCount - 1)
                    outputFile.write(b'\x00')

                    for i in range(len(names)):
                        offset = outputFile.seek(0, os.SEEK_END)
                        outputFile.write(names[i].encode('utf-8') + b'\x00')
                        outputFile.seek(startOffset2 + 2 * i)
                        outputFile.write(offset.to_bytes(2, 'little'))

                    offset = outputFile.seek(0, os.SEEK_END)
                    for i in range(summary['diff']):
                        outputFile.write(b'\x00')
                    outputFile.seek(24)
                    outputFile.write(offset.to_bytes(4, 'little'))

                    version = 2882400000
                    outputFile.write(version.to_bytes(4, 'little'))
                    outputFile.write(fname.encode('utf-8') + b'\x00')
                    
                    for i in range(len(datas)):
                        offset = outputFile.seek(0, os.SEEK_END)
                        outputFile.write(datas[i])
                        outputFile.seek(startOffset + 4 * i)
                        outputFile.write(offset.to_bytes(4, 'little'))

        else:
            import subprocess
            for filename in [f.name for f in os.scandir(f'{projectDir}/{scriptFolder}') if f.is_file()]:
                frame.status.set(f'Packing {scriptFolder}/{filename}...')
                subprocess.run(["decompiler/SenScriptsDecompiler.exe", "CS3", f'{projectDir}/{scriptFolder}/{filename}', gamePath])