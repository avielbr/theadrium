from locators.headline_locator import HeadlineLocator


class HeadlineParser:
    def __init__(self, parent):
        self.parent = parent

    @property
    def headline(self):
        locator = HeadlineLocator.HEADLINE
        return self.parent.select_one(locator).string
