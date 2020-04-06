from bs4 import BeautifulSoup

from locators.block_locator import BlockLocator
from parsers.headline import HeadlineParser


class Liveblogs:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def blocks(self):
        locator = BlockLocator.BLOCK
        block_tags = self.soup.select(locator)
        return [HeadlineParser(e) for e in block_tags]