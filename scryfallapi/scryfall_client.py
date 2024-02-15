from typing import List

import json
import requests
import time
import os

from scryfallapi.scryfall_card import Card


BASE_SETS = 'https://api.scryfall.com/sets/'



def get_cards_from_page(page:object) -> List[Card]:
    cards_in_page = []
    print('--------------------------------')
    print('TOTAL CARDS IN PAGE', len(page['data']))
    print('--------------------------------')
    for card in page['data']:
        if 'card_faces' in card:
            combined_oracle_text = ""
            for card_face in card['card_faces']:
                combined_oracle_text += card_face["oracle_text"] + " "
            oracle_text = combined_oracle_text
        else:
            oracle_text = card['oracle_text']
        print(card['name'])
        cards_in_page.append(Card(
                        card['id'],
                        card['type_line'],
                        card['colors'],
                        oracle_text,
                        card['set'],
                        card['name'],
                        card['image_uris']['normal'],
                    ))
    return cards_in_page


class ScryfallClient:
    def __init__(self) -> None:
        pass
       
    def get_entire_set(set_code:str) -> List[Card]:
        cards_in_set = []
        response = requests.get(BASE_SETS+set_code)
        if response.status_code == 200:
            current_page = requests.get(response.json()['search_uri']).json()
            print('--------------------------------')
            print('CURRENT PAGE', current_page['next_page'])
            print('--------------------------------')
            cards_in_page = get_cards_from_page(current_page)
            cards_in_set.append(cards_in_page)
            has_more_pages = True if current_page['has_more'] == 'true' else False
            i = 0
            while has_more_pages == True:
                print('ENTERS ON THE LOOP', i)
                i = i+1
                next_page_url = current_page['next_page']
                current_page = requests.get(next_page_url).json()
                cards_in_page = get_cards_from_page(current_page)
                cards_in_set.append(cards_in_page)
                has_more_pages = True if current_page['has_more'] == 'true' else False
        print('--------------------------------')
        print('TOTAL CARDS', len(cards_in_set))
        print('--------------------------------')
        return cards_in_set

