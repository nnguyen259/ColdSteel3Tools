import random, csv, json
from randomizer.base import BaseRandomizer

class SlotRandomizer(BaseRandomizer):
    def __init__(self, projectName=None, seed=None, programMode=True) -> None:
        super().__init__(projectName=projectName, seed=seed, programMode=programMode)
        random.seed(self.seed)
        self.inputPath += 'slot'

    def randomize(self, randomizeBase=True, randomizeGrowth=True, excludeGuest=False):
        with open('result.txt', 'a', encoding='utf-8') as resultFile, open('ref/char.json') as charFile:
            chars = json.load(charFile)
            resultFile.write('\nEP Randomizer Results:\n')

            inputPath = self.inputPath
            with open(f'{inputPath}/SlotEp.csv', newline='', encoding='utf-8') as epFile:
                statusReader = csv.DictReader(epFile)
                headers = statusReader.fieldnames
                slots = list(statusReader)

            skipId = 16 if excludeGuest else 48

            for slot in slots:
                charId = slot['character_id']
                if int(charId) >= skipId: continue
                resultFile.write(f'\n{chars[charId]}:\n')

                if randomizeBase:
                    baseEp = random.randrange(50, 251, 5)
                    slot['base_ep'] = baseEp
                    resultFile.write(f'Base EP: {baseEp}\n')

                if randomizeGrowth:
                    growthEp = [random.randrange(0, 161, 5) for _ in range(7)]
                    growthEp.sort()
                    for i in range(7):
                        slot[f'increase_{i + 1}'] = growthEp[i]
                    resultFile.write(f'EP Growth: {growthEp}\n')

        with open(f'{inputPath}/SlotEp.csv', 'w', newline='', encoding='utf-8') as epFile:
            writer = csv.DictWriter(epFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(slots)