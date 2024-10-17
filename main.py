import os
import requests
from string import punctuation

def get_delimiter(name):
    for c in name:
        if c in punctuation:
            return c


def add_common_prefix(prefix, name, prefixes):
    if common_prefix := os.path.commonprefix([name, prefix]):
        prefixes[common_prefix.strip(punctuation)] = [name]
    return prefixes


def add_name_to_prefixes(name, prefixes):
    prefixes[name] = [name]
    for prefix in list(prefixes):
        if prefix in name and prefix != name:
            prefixes[prefix].append(name)
        else:
            prefixes = add_common_prefix(prefix, name, prefixes)
    return prefixes


def remove_prefixes_with_single_name(prefixes):
    for prefix in list(prefixes):
        if (len(prefixes[prefix]) == 1):
            del prefixes[prefix]
    return prefixes


def remove_too_broad_prefixes(prefixes):
    for prefix in list(prefixes):
        if any(prefix in name and prefix != name for name in list(prefixes)):
            del prefixes[prefix]
    return prefixes


def get_prefixes(names):
    prefixes = {}
    for name in names:
        name = name.strip()
        if name:
            prefixes = add_name_to_prefixes(name, prefixes)

    prefixes = remove_prefixes_with_single_name(prefixes)
    prefixes = remove_too_broad_prefixes(prefixes)
    return prefixes


with open('names.csv') as names:
    for prefix, values in get_prefixes(names).items():
        folder = requests.post('http://127.0.0.1:8000/folders/', json={'title': prefix}).json()
        for value in values:
            requests.post('http://127.0.0.1:8000/names/', json={'name_text': value, 'folder': folder['id']})

