from bs4.element import Tag
import htmlconv


class OOPAssignmentTests(Tag):
    """docstring for OOPAssignmentTests."""
    def __init__(self):
        super().__init__(self)

    def testHead(self):
        return len(self.findAll('head'))

    def testNav(self):
        return len(self.findAll('nav'))

    def testArticle(self):
        return len(self.findAll('article'))

    def testSection(self):
        return len(self.findAll('section'))

    def testFooter(self):
        return len(self.findAll('footer'))

    def imageTitle(self):
        return len(self.findAll('img', title=False))

    def imageAlt(self):
        return len(self.findAll('img', alt=False))

    def imageSource(self):
        return len(self.findAll('img', src=False))

    def imageHeight(self):
        return len(self.findAll('img', height=True))

    def imageWidth(self):
        return len(self.findAll('img', width=True))
