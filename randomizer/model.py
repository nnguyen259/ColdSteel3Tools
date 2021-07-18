import random, csv, json
from randomizer.base import BaseRandomizer

class ModelRandomizer(BaseRandomizer):
    def __init__(self, projectName, seed, programMode=True) -> None:
        super().__init__(projectName=projectName, seed=seed, programMode=programMode)
        random.seed(self.seed)

    def randomize(self, excludeGuest=False):
        skipId = 16 if excludeGuest else 27

        with open(f'{self.inputPath}name/NameTableData.csv', newline='') as nameFile:
            reader = csv.DictReader(nameFile)
            headers = reader.fieldnames
            names = list(reader)
        
        shuffleList = [(name['character_id'], name['animation'].upper()) for name in names if int(name['character_id']) < skipId]
        random.shuffle(shuffleList)

        with open('result.txt', 'a', encoding='utf-8') as resultFile, open('ref/char.json') as charFile:
            chars = json.load(charFile)
            resultFile.write('\nModel Randomizer Results: \n')
            for name in names:
                if int(name['character_id']) >= skipId: continue
                newId = shuffleList[int(name['character_id'])]
                resultFile.write(f'{chars[name["character_id"]]} -> {chars[newId[0]]}\n')
                name['model'] = f'C_{newId[1]}'
                name['face_default'] = f'C_{newId[1]}_FC1'
                name['face'] = f'FC_{newId[1]}'

        with open(f'{self.inputPath}name/NameTableData.csv', 'w', newline='') as nameFile:
            writer = csv.DictWriter(nameFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(names)

        with open(f'{self.inputPath}attach/AttachTableData.csv', newline='') as attachFile:
            reader = csv.DictReader(attachFile)
            headers = reader.fieldnames
            attachs = list(reader)

        for attach in attachs:
            if int(attach['character_id']) >= skipId: continue
            if int(attach['type']) != 5: continue
            if len(attach['model']) != 8: continue

            newId = shuffleList[int(attach['character_id'])]
            attach['model'] = f'C_{newId[1]}'

        with open(f'{self.inputPath}attach/AttachTableData.csv', 'w', newline='') as attachFile:
            writer = csv.DictWriter(attachFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(attachs)