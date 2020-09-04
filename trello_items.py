import requests

from flask_config import Config
from item import Item


def get_items():
    """
    Fetches all saved items from the session.

    Returns:
        list: The list of saved items.
    """
    r = requests.get(f'https://api.trello.com/1/lists/{Config.LIST_ID}/cards?key={Config.KEY}&token={Config.TOKEN}')
    done_request = requests.get(
        f'https://api.trello.com/1/lists/{Config.DONE_LIST_ID}/cards?key={Config.KEY}&token={Config.TOKEN}')
    response = r.json()
    trello_items = []
    for item in response:
        trello_items.append(Item(item))
    for item in done_request.json():
        trello_items.append(Item(item))
    return trello_items


def add_item(title, descr):
    """
    Adds a new item with the specified title to the session.

    Args:
        title: The title of the item.

    Returns:
        item: The saved item.
    """
    url = "https://api.trello.com/1/cards"

    query = {
        'key': Config.KEY,
        'token': Config.TOKEN,
        'idList': Config.LIST_ID,
        'name': title,
        'desc': descr,
    }

    response = requests.request(
        "POST",
        url,
        params=query
    )

    print(response.text)


def save_item(item):
    """
    Updates an existing item in the session. If no existing item matches the ID of the specified item, nothing is saved.

    Args:
        item: The item to save.
    """
    existing_items = get_items()
    updated_items = [item if item['id'] == existing_item['id'] else existing_item for existing_item in existing_items]

    # session['items'] = updated_items

    return item


def move_to_done(itemId):
    url = f'https://api.trello.com/1/cards/{itemId}'

    headers = {
        "Accept": "application/json"
    }

    query = {
        'key': Config.KEY,
        'token': Config.TOKEN,
        'idList': Config.DONE_LIST_ID
    }

    response = requests.request(
        "PUT",
        url,
        headers=headers,
        params=query
    )
    print(response.text)