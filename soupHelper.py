class soupHelper():
    """docstring for soupHelper."""
    def __init__(self):
        super().__init__(self)

    def countHead(self):
        return len(self.findAll('head'))

    def countNav(self):
        return len(self.findAll('nav'))

    def countArticle(self):
        return len(self.findAll('article'))

    def countSection(self):
        return len(self.findAll('section'))

    def countFooter(self):
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
