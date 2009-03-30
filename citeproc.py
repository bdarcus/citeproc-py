
import json
from csl.processor import *
from lxml import etree
import os

styles_index = json.loads(open(os.path.expanduser('~/.csl/styles/index.json')).read())


def list_styles():
    print("\nStyles\n======\n")
    for id in styles_index:
        print(id)


def update_styles():
    """
    Updates the users' style repository.
    """
    for styles in styles_index['styles']:
        style.update(style['id'])


def old(style_id):
    """
    Compare the last update date-time-stamp against the server 
    version. 
    """
    return(style_id['updated'] == get_style_updated(style_id['link']))


def update(style_id):
    pass


def get_style(style_id):
    fn = styles_index[style_id]['file']
    path = os.path.expanduser('~/.csl/styles/' + fn) 
    return(open(path, 'rb'))


def validate_style(style_id):
    schema = open(os.path.expanduser('~/.csl/schema/csl.rng'), 'rb')
    relaxng = etree.RelaxNG(file=schema)
    style = get_style(style_id)
    return(relaxng.validate(etree.parse(style)))


def process_bibliography(style_id, references):
    """
    With a style ID/URI and a list of references, format the bibliography.

    >>> process_bibliography('http://zotero.org/styles/aag', '')
    'ERROR: your CSL style is not valid.'
    >>> process_bibliography('http://zotero.org/styles/apa', '')
    'OK, let's run it.'
    """
    if validate_style(style_id):
        print("OK, let's run it.")
    else:
        print("ERROR: your CSL style is not valid.")

