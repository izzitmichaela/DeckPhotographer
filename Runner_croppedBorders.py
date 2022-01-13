# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:53:48 2022

@author: izzitMichaela

Building off of the code snippet by rib0rb from reddit
https://www.reddit.com/r/MagicArena/comments/ok1gw4/bulk_download_of_high_res_card_image_from_skryfall/

Simply run the code in a python environment and ensure your deck txt file contains cards with quantites in
only the single digits (e.g. 1 Abrade , not 15 Abrade)


"""

import json, requests

with open('./all-cards.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)


with open('Deck.txt') as f:
    deck = f.readlines()

print(deck)


for item in deck:
    currentCard = item[2:].strip()
    print(currentCard)
    found = 0

    for card in cards:
        if card['name'] == currentCard and card['lang'] == 'en' and found == 0:
            r = requests.get(card['image_uris']['png'])
            card_name=card["collector_number"] + "_" + card['name'] + '.jpg'
            open(card_name, 'wb').write(r.content)
            found = 1
            
    if found == 0:
        print(currentCard + 'not found')
        