# -*- coding: utf-8 -*-
"""
Created on Thu Jan 13 11:53:48 2022

@author: izzitMichaela

Building off of the code snippet by rib0rb from reddit
https://www.reddit.com/r/MagicArena/comments/ok1gw4/bulk_download_of_high_res_card_image_from_skryfall/

Simply run the code in a python environment


"""
import tkinter as tk
from tkinter import filedialog
import re
import json
import requests
import os
import sys

def extract_card_info_from_file(file_path):
    """Pull card names, or collector number/set pairs, out of file"""
    cards = []
    with open(file_path) as f:
        for line in f:
            line_info = re.match("^\d+ (.+[^ (\r\n])( \((\w+)\))?( (\d+))?$", line, re.MULTILINE)
            if line_info:
                card_data = {}
                line_groups = [grp for grp in line_info.groups() if grp]
                if len(line_groups) == 1:
                    card_data['name'] = line_groups[0]
                elif len(line_groups) > 1:
                    card_data['set'], card_data['collector_number'] = (line_groups[2], line_groups[4])
                cards.append(card_data)
    return cards

def get_card_images(card_data):
    dir_name = 'DeckPictures'
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    all_not_found = []

    # Use the /cards/collection endpoint to grab all the card data at once from Scryfall
    # This endpoint only takes 75 identifiers at a time
    while len(card_data) > 0:
        bucket = card_data[:75]
        del card_data[:75]
        response = requests.post('http://api.scryfall.com/cards/collection', json={'identifiers': bucket})
        response_data = json.loads(response.text)


        not_found = response_data['not_found']
        if len(not_found) > 0:
            all_not_found.extend(not_found)
        
        # Pull down all the images
        for card in response_data['data']:
            name = card['name'].replace("//", "&")
            if 'image_uris' in card:
                r = requests.get(card['image_uris']['border_crop'])
                card_file_name=f"{card['collector_number']}_{name}.jpg"
                open(f'./{dir_name}/{card_file_name}', 'wb').write(r.content)
            elif 'card_faces' in card:
                for face in card['card_faces']:
                    r = requests.get(face['image_uris']['border_crop'])
                    card_file_name=f"{card['collector_number']}_{name}-({face['name']}).jpg"
                    open(f'./{dir_name}/{card_file_name}', 'wb').write(r.content)

    if len(not_found) > 0:
        print(f"Could not find images for the following {len(not_found)} cards: ")
        for nf_card in not_found:
            print(nf_card)
    else:
        print("Done!") 

def ask_for_file_path_tkinter():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()

def main():
    file_path = sys.argv[1]
    card_data = extract_card_info_from_file(file_path)
    get_card_images(card_data)

if __name__ == "__main__":
    main()