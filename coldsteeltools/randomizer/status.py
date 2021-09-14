import random, csv
from .base import BaseRandomizer

class StatusRandomizer(BaseRandomizer):
    def __init__(self, projectName=None, seed=None, programMode=True) -> None:
        super().__init__(projectName=projectName, seed=seed, programMode=programMode)
        random.seed(self.seed)
        self.inputPath += 'status'

    def randomize(self, enableBase=True, baseVariance=30, enableGrowth=True, growthVariance=30, excludeGuest=False):
        baseVariance = (100 - baseVariance)/100
        growthVariance = (100 -growthVariance)/100
        with open('result.txt', 'a', encoding='utf-8') as resultFile:
            resultFile.write('\nStats Randomizer Results:\n')

            inputPath = self.inputPath
            with open(f'{inputPath}/status_p.csv', newline='', encoding='utf-8') as statusFile:
                statusReader = csv.DictReader(statusFile)
                headers = statusReader.fieldnames
                statuses = list(statusReader)

            skipId = 16 if excludeGuest else 48
            stats = ['hp', 'str', 'def', 'ats', 'adf', 'dex', 'agi', 'spd']
            resultFile.write(f'Stats: {stats}\n')

            for character in statuses:
                if int(character['character_id']) >= skipId: continue
                printable = True
                baseProb = [336, 59, 29, 54, 27, 34, 24, 37]
                growthProb = [10600, 572, 282, 532, 220, 14, 14, 53]

                if not character['name']: printable = False

                if printable:
                    resultFile.write(f'\n{character["name"]}:\n')

                if enableBase:
                    newProb = [random.randint(i - int((1-baseVariance) * i), i + int((1-baseVariance) * i)) for i in baseProb]
                    temp = newProb[1:]
                    random.shuffle(temp)
                    newProb[1:] = temp

                    statSum = 0
                    for stat in stats:
                        statSum += int(character[f'{stat}_base'])
                        character[f'{stat}_base'] = 0
                    statSum = random.randint(int(statSum*0.9), int(statSum*1.1))
                    for _ in range(statSum):
                        stat = random.choices(stats, weights=newProb)[0]
                        character[f'{stat}_base'] += 1
                    result = [character[f'{i}_base'] for i in stats]
                    if printable:
                        resultFile.write(f'Base: {result}\n')

                if enableGrowth:
                    newProb = [random.randint(i - int((1-baseVariance) * i), i + int((1-baseVariance) * i)) for i in growthProb]
                    temp = newProb[1:5]
                    random.shuffle(temp)
                    newProb[1:5] = temp

                    statSum = 0
                    for stat in stats:
                        statValue = float(character[f'{stat}_growth'])
                        statSum += int(statValue * 100)
                        character[f'{stat}_growth'] = 0
                    statSum = random.randint(int(statSum*0.9), int(statSum*1.1))
                    for _ in range(statSum):
                        stat = random.choices(stats, weights=newProb)[0]
                        character[f'{stat}_growth'] += 0.01

                    result = [float("{:.2f}".format(character[f'{i}_growth'])) for i in stats]
                    if printable:
                        resultFile.write(f'Growth: {result}\n')
        
        with open(f'{inputPath}/status_p.csv', 'w', newline='', encoding='utf-8') as statusFile:
            writer = csv.DictWriter(statusFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(statuses)