#!/usr/bin/env python

"""Fetch and display a Giphy image in an iTerm 2 window"""

import random
import sys
import warnings

import giphypop
import iterm2_tools
import requests


def get_random_giphy(phrase):
    """Return the URL of a random GIF related to the phrase, if possible"""
    with warnings.catch_warnings():
        warnings.simplefilter('ignore')

        giphy = giphypop.Giphy()

    results = giphy.search_list(phrase=phrase, limit=100)

    if not results:
        raise ValueError('There were no results for that phrase')

    return random.choice(results).media_url


def fetch_image(url):
    """Return a URL's contents"""
    return requests.get(url).content


def display(image):
    """Display an image on an iTerm 2 window"""
    print(iterm2_tools.images.display_image_bytes(image))


def handle_command_line():
    """Display an image for the phrase in sys.argv, if possible"""
    phrase = ' '.join(sys.argv[1:]) or 'random'

    try:
        giphy = get_random_giphy(phrase)
    except ValueError:
        sys.stderr.write('Unable to find any GIFs for {!r}\n'.format(phrase))
        sys.exit(1)

    display(fetch_image(giphy))


if __name__ == '__main__':
    handle_command_line()
