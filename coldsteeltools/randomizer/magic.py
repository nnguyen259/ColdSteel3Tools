import csv, random, json
from .base import BaseRandomizer

class MagicRandomizer(BaseRandomizer):
    def __init__(self, projectName=None, seed=None, programMode=True) -> None:
        super().__init__(projectName=projectName, seed=seed, programMode=programMode)
        random.seed(self.seed)
        self.inputPath += 'magic'

    def randomize(self, enableCraft=True, excludeGuestCraft=False, enableOrder=True, excludeGuestOrder=False,
                enableSCraft=True, excludeGuestSCraft=False):
        inputPath = self.inputPath
        with open(f'{inputPath}/magic.csv', newline='', encoding='utf-8') as magicFile:
            magicReader = csv.DictReader(magicFile)
            headers = magicReader.fieldnames
            magic = list(magicReader)

        if enableCraft:
            crafts = [i for i in magic if i['category'] == '30' and not i['character_restriction'] == '65535' and not i['name'] == 'Spirit Unification']
            if excludeGuestCraft:
                crafts = [i for i in crafts if int(i['character_restriction']) < 16]
            craftsData = [(i['id'], i['character_restriction'], i['level_learn'], i['animation'], i['juna_specific'], i['sort_id'], i['name']) for i in crafts]

            random.shuffle(crafts)

            with open('result.txt', 'a', encoding='utf-8') as resultFile, open('ref/char.json') as charFile:
                chars = json.load(charFile)
                resultFile.write('\nCraft Randomizer Results: \n')
                for data in craftsData:
                    craft = crafts.pop()
                    index = magic.index(craft)
                    entry = magic[index]
                    resultFile.write(f'{chars[data[1]]}: {data[-1]} -> {craft["name"]}\n')
                    entry['id'] = data[0]
                    entry['character_restriction'] = data[1]
                    entry['level_learn'] = data[2]
                    entry['animation'] = data[3]
                    entry['juna_specific'] = data[4]
                    entry['sort_id'] = data[5]

        if enableOrder:
            with open(f'{inputPath}/magicbo.csv', newline='', encoding='utf-8') as magicFile:
                magicBoReader = csv.DictReader(magicFile)
                boHeaders = magicBoReader.fieldnames
                magicBos = list(magicBoReader)
            boIndexes = {i['id'] : magicBos.index(i) for i in magicBos}

            orders = [i for i in magic if i['category'] == '32' and not i['character_restriction'] == '65535']
            if excludeGuestOrder:
                orders = [i for i in orders if int(i['character_restriction']) < 16]
            ordersData = [(i['id'], i['character_restriction'], i['animation'], i['sort_id'], i['name']) for i in orders]

            random.shuffle(orders)
            with open('result.txt', 'a', encoding='utf-8') as resultFile, open('ref/char.json') as charFile:
                chars = json.load(charFile)
                resultFile.write('\nBrave Orders Randomizer Results: \n')
                for data in ordersData:
                    order = orders.pop()
                    index = magic.index(order)
                    entry = magic[index]
                    boIndex = boIndexes[order['id']]
                    boEntry = magicBos[boIndex]
                    resultFile.write(f'{chars[data[1]]}: {data[-1]} -> {order["name"]}\n')
                    boEntry['id'] = data[0]
                    entry['id'] = data[0]
                    entry['character_restriction'] = data[1]
                    entry['animation'] = data[2]
                    entry['sort_id'] = data[3]
                with open(f'{inputPath}/magicbo.csv', 'w', newline='', encoding='utf-8') as magicFile:
                    writer = csv.DictWriter(magicFile, fieldnames=boHeaders)
                    writer.writeheader()
                    writer.writerows(magicBos)

        if enableSCraft:
            scrafts = [i for i in magic if i['category'] == '31' and not i['character_restriction'] == '65535']
            if excludeGuestSCraft:
                scrafts = [i for i in scrafts if int(i['character_restriction']) < 16]
            scraftsData = [(i['id'], i['character_restriction'], i['level_learn'], i['animation'], i['juna_specific'], i['sort_id'], i['name']) for i in scrafts]

            random.shuffle(scrafts)

            with open('result.txt', 'a', encoding='utf-8') as resultFile, open('ref/char.json') as charFile:
                chars = json.load(charFile)
                resultFile.write('\nS-Craft Randomizer Results: \n')
                for data in scraftsData:
                    scraft = scrafts.pop()
                    index = magic.index(scraft)
                    entry = magic[index]
                    resultFile.write(f'{chars[data[1]]}: {data[-1]} -> {scraft["name"]}\n')
                    entry['id'] = data[0]
                    entry['character_restriction'] = data[1]
                    entry['level_learn'] = data[2]
                    entry['animation'] = data[3]
                    entry['juna_specific'] = data[4]
                    entry['sort_id'] = data[5]


        with open(f'{inputPath}/magic.csv', 'w', newline='', encoding='utf-8') as magicFile:
            writer = csv.DictWriter(magicFile, fieldnames=headers)
            writer.writeheader()
            writer.writerows(magic)