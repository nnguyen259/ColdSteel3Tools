import random, csv, json
from randomizer.base import BaseRandomizer

class OrbRandomizer(BaseRandomizer):
    def __init__(self, projectName, seed, programMode=True) -> None:
        super().__init__(projectName=projectName, seed=seed, programMode=programMode)
        self.inputPath += 'orb'
        random.seed(self.seed)

    def randomize(self, maxLine=7, minEleSlot=0, maxEleSlot=7, excludeGuest=False):
        inputPath = self.inputPath
        with open(f'{inputPath}/BaseList.csv', newline='') as orbFile:
            reader = csv.DictReader(orbFile)
            headers = reader.fieldnames
            orbs = list(reader)

        with open('result.txt', 'a', encoding='utf-8') as resultFile, open('ref/char.json') as charFile, open('ref/element.json') as elementFile:
            chars = json.load(charFile)
            elementNames = json.load(elementFile)
            resultFile.write('\nOrbment Line Randomizer Results: \n')

            for orb in orbs:
                charId = orb['character_id']
                if int(charId) > 24: continue
                if excludeGuest and int(charId) > 15: continue
                lineCount = random.randint(1, maxLine)
                orb['line_count'] = lineCount
                sizes = []
                for i in range(lineCount - 1):
                    try:
                        sizes.append(random.randint(1, 7 - sum(sizes) - lineCount + i))
                    except ValueError:
                        sizes.append(1)
                sizes.append(7 - sum(sizes))
                sizes.sort(reverse=True)
                resultFile.write(f'{chars[charId]}: {sizes}')

                elements = 7 * [0]

                numEleSlot = random.randint(minEleSlot, maxEleSlot) if minEleSlot <= maxEleSlot else random.randint(maxEleSlot, minEleSlot)

                for i in range(numEleSlot):
                    elements[i] = random.randint(1, 7)
                random.shuffle(elements)
                
                for i in range(7):
                    orb[f'slot_{i + 1}_element'] = elements[i]
                    if elements[i] > 0:
                        resultFile.write(f' {i + 1}-{elementNames[str(elements[i])]}')
                resultFile.write('\n')

                with open(f'{inputPath}/OrbLineList/{charId}.csv', 'w', newline='') as lineFile:
                    lineHeaders = ['character_id', 'line_number', 'slot_1_order', 'slot_2_order', 'slot_3_order', 'slot_4_order', 'slot_5_order', 'slot_6_order', 'slot_7_order']
                    writer = csv.writer(lineFile)
                    writer.writerow(lineHeaders)
                    counter = 2
                    for idx, size in enumerate(sizes):
                        order = 7 * [65535]
                        for j in range(size):
                            order[j] = counter
                            counter += 1

                        line = list()
                        line.append(int(charId))
                        line.append(idx)
                        line.extend(order)
                        writer.writerow(line)

        with open(f'{inputPath}/BaseList.csv', 'w', newline='') as orbFile:
            writer = csv.DictWriter(orbFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(orbs)