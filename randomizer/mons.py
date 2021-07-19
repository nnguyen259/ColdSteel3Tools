import random, csv
from randomizer.base import BaseRandomizer

class MonsRandomizer(BaseRandomizer):
    def __init__(self, projectName=None, seed=None, programMode=True) -> None:
        super().__init__(projectName=projectName, seed=seed, programMode=programMode)
        random.seed(self.seed)
        self.inputPath += 'mons'

    def randomize(self, enableBase=True, baseVariance=30, enableGrowth=True, growthVariance=30, 
                  lowRollElemental=30, lowCapElemental=30, highCapElemental=200, randomizeElemental=True, 
                  lowRollStatus=30, lowCapStatus=30, highCapStatus=200, randomizeStatus=True, keepDeathblow=False, 
                  lowRollUnbalance=30, randomizeUnbalance=True):
        inputPath = self.inputPath
        baseVariance = (100 - baseVariance)/100
        growthVariance = (100 -growthVariance)/100

        with open(f'{inputPath}/status.csv', newline='', encoding='utf-8') as statusFile:
            statusReader = csv.DictReader(statusFile)
            headers = statusReader.fieldnames
            statuses = list(statusReader)

        stats = ['hp', 'str', 'def', 'ats', 'adf', 'dex', 'agi', 'spd']
        elements = ['earth', 'water', 'fire', 'wind', 'time', 'space', 'mirage']
        status = ['psn', 'seal', 'mute', 'blnd', 'slp', 'burn', 'frz', 'petr', 'fnt', 'conf', 'chrm', 'dblw', 'nmr', 'dlay', 'vnsh', 's-dwn']
        unbalances = ['slash', 'thurst', 'pierce', 'strike']
        unbalanceValues = [50, 100, 200, 400]

        for mon in statuses:
            if enableBase:
                prob = []
                for stat in stats:
                    prob.append(int(mon[f'{stat}_base']))
                    mon[f'{stat}_base'] = 0

                statSum = sum(prob)
                statSum = random.randint(int(statSum*0.8), int(statSum*1.2))
                prob = [random.randint(i - int((1-baseVariance) * i), i + int((1-baseVariance) * i)) for i in prob]

                for _ in range(statSum):
                    stat = random.choices(stats, weights=prob)[0]
                    mon[f'{stat}_base'] += 1

            if enableGrowth:
                prob = []
                for stat in stats:
                    prob.append(int(float(mon[f'{stat}_growth']) * 100))
                    mon[f'{stat}_growth'] = 0

                statSum = sum(prob)
                statSum = random.randint(int(statSum*0.8), int(statSum*1.2))
                prob = [random.randint(i - int((1-growthVariance) * i), i + int((1-growthVariance) * i)) for i in prob]

                for _ in range(statSum):
                    stat = random.choices(stats, weights=prob)[0]
                    mon[f'{stat}_growth'] += 0.01

            if randomizeElemental:
                if lowCapElemental > highCapElemental:
                    lowCapElemental, highCapElemental = highCapElemental, lowCapElemental
                if 'S' not in mon['flags']:
                    mon['flags'] += 'S'
                for element in elements:
                    if random.randint(1, 100) <= lowRollElemental:
                        mon[f'{element}_efficacy'] = random.randrange(0, lowCapElemental + 1, 5)
                    else:
                        mon[f'{element}_efficacy'] = random.randrange(lowCapElemental, highCapElemental + 1, 5)

            if randomizeStatus:
                if lowCapStatus > highCapStatus:
                    lowCapStatus, highCapStatus = highCapStatus, lowCapStatus
                for stat in status:
                    if keepDeathblow:
                        if stat in ['petr', 'dblw', 'vnsh']: continue
                    if random.randint(1, 100) <= lowRollStatus:
                        mon[f'{stat}_efficacy'] = random.randrange(0, lowCapStatus + 1, 5)
                    else:
                        mon[f'{stat}_efficacy'] = random.randrange(lowCapStatus, highCapStatus + 1, 5)

            if randomizeUnbalance:
                for unbalance in unbalances:
                    if random.randint(1, 100) <= lowRollUnbalance:
                        mon[f'{unbalance}_efficacy'] = random.choice([10, 50])
                    else:
                        mon[f'{unbalance}_efficacy'] = random.choice(unbalanceValues)

        with open(f'{inputPath}/status.csv', 'w', newline='', encoding='utf-8') as statusFile:
            writer = csv.DictWriter(statusFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(statuses)