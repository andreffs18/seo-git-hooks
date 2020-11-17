#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import sys


global ERROR
ERROR = 0
def _warning(message):
    global ERROR
    ERROR += 1
    print(message)


def check_title_length(html, max_length=65):
    """
    Search on given `html` file for any <title> tags and check if the title length is greater
    than `max_length`.
    """
    titles = re.findall(r"<title>(.*?)</title>", html)
    for title in titles:
        if len(title) > max_length:
            _warning(u"{}: ⚠️ No title {} length more than {}!".format(filepath, title, max_length))


def check_alt_prop(html):
    """
    Search on given `html` file for all <img> tags and alert if:
    - img tag has "alt=" attribute but without content (eg: alt="")
    - img tag does not have "atl=" attribute
    """
    alt_texts = re.findall(r"<img.*?alt=[\'\"](.*?)[\'\"][^>]*>", html)
    for alt in alt_texts:
        if not alt:
            _warning(u"{}: ⚠️  No alt text!".format(filepath))

    missing_alt_texts = re.findall(r"<img(?!.*?alt=([\'\"]).*?)[^>]*>", html)
    for missing in missing_alt_texts:
        _warning(u"{}: ⚠️  No alt attribute!".format(filepath))


def check_canonical_urls(html):
    """
    Search on given `html` file for all <a> tags and check if configured href is canonical. (absolute url)
    This also accepts urls when href starts with "mailto:" or expected characters: "#", "{", "%", ""
    """
    urls = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', html)
    for url in urls:
        if any([
            url == "",  # empty url is accepted
            map(lambda rule: url.startswith(rule), ["http", "mailto:", "#", "{", "%"],),
        ]):
            continue
        _warning(u"({}) ⚠️ Relative URL {}!".format(filepath, url))


if __name__ == "__main__":
    for filepath in sys.argv[1:]:
        with open(filepath, "r+") as html:
            html = html.read()
        check_alt_prop(html)
        check_canonical_urls(html)
        check_title_length(html)

    if ERROR:
        sys.exit(1)
