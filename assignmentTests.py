from bs4 import BeautifulSoup
import htmlconv

def listImages(images):
    result = ''
    for image in images:
        result += htmlconv.imageHandler(image)
    return result



class assignmentTests(object):
    """docstring for assignmentTests."""
    def __init__(self):
        super(assignmentTests, self).__init__()


    def __printImages(self, images):
        for image in images:
            print(htmlconv.imageHandler(image))
        return

    def testHead(soup):
        if len(soup.findAll('head')) == 0:
            return(htmlconv.makeHTML('p', 'You should have a <code>&lthead&gt</code> section in your HTML5', 'text-danger'))
        elif len(soup.findAll('head')) == 1:
            return(htmlconv.makeHTML('p', 'Single <code>&lthead&gt</code> section found for page; &#10004', 'text-success'))
        else:
            return(htmlconv.makeHTML('p', 'You should only have a single <code>&lthead&gt</code> section per page.  You have used more than one on this page', 'text-danger'))

    def testNav(soup):
        if len(soup.findAll('nav')) == 0:
            return(htmlconv.makeHTML('p', 'You should have a nav section in your HTML5', 'text-danger'))
        elif len(soup.findAll('nav')) == 1:
            return(htmlconv.makeHTML('p', 'Single <code>&ltnav&gt</code> section found for page; &#10004', 'text-success'))
        else:
            return(htmlconv.makeHTML('p', 'You should only have a single <code>&ltnav&gt</code> tag per page.  You have used more than one on this page', 'text-danger') )

    def testArticle(soup):
        if len(soup.findAll('article')) == 0:
            return(htmlconv.makeHTML('p', 'You should have <code>&ltarticle&gt</code> tags in your HTML5', 'text-danger'))
        elif len(soup.findAll('article')) > 0:
            return(htmlconv.makeHTML('p', (str(len(soup.findAll('article'))) + ' HTML5 <code>&ltarticle&gt</code> tags found')))

    def testSection(soup):
        if len(soup.findAll('section')) == 0:
            return(htmlconv.makeHTML('p', 'You should have <code>&ltsection&gt</code> tags in your HTML5', 'text-danger'))
        elif len(soup.findAll('section')) > 0 and len(soup.findAll('article')) == 0:
            return(htmlconv.makeHTML('p', 'You should not have <code>&ltsection&gt</code> without <code>&ltarticle&gt</code>', 'text-danger'))
        else:
            return(htmlconv.makeHTML('p', (str(len(soup.findAll('section'))) + ' HTML5 <code>&ltsection&gt</code> tags found')))

    def testFooter(soup):
        if len(soup.findAll('footer')) == 0:
            return(htmlconv.makeHTML('p', 'You should have a <code>&ltfooter&gt</code> section in your HTML5', 'text-danger'))
        elif len(soup.findAll('footer')) == 1:
            return(htmlconv.makeHTML('p', 'Single <code>&ltfooter&gt</code> section found for page; &#10004', 'text-success'))
        else:
            return(htmlconv.makeHTML('p', 'You should only have a single <code>&ltfooter&gt</code> section per page.  You have used more than one on this page', 'text-danger'))

    def imageTitle(soup):
        if len(soup.findAll('img', title=False))>0:
            images = soup.findAll('img', title=False)
            listImages(images)
            return(htmlconv.makeHTML('h3', 'NO TITLE FOUND ON THE FOLLOWING IMAGES (class)', 'text-warning') + listImages(images))
        else:
            return(htmlconv.makeHTML('p', 'TITLE found on all images &#10004', 'text-success'))

    def imageAlt(soup):
        if len(soup.findAll('img', alt=False))>0:
            images = soup.findAll('img', alt=False)
            return(htmlconv.makeHTML('h3', 'NO ALT FOUND ON THE FOLLOWING IMAGES (class)', 'text-danger') + listImages(images))
        else:
            return(htmlconv.makeHTML('p', 'ALT found on all images &#10004', 'text-success'))

    def imageSource(soup):
        if len(soup.findAll('img', src=False))>0:
            images = soup.findAll('img', src=False)
            return(htmlconv.makeHTML('h3', 'NO SOURCE FOUND ON THE FOLLOWING IMAGES', 'text-danger') + listImages(images))
        else:
            return(htmlconv.makeHTML('p', 'Source found on all images &#10004', 'text-success'))

    def imageHeight(soup):
        if len(soup.findAll('img', height=True))>0:
            images = soup.findAll('img', height=True)
            return(htmlconv.makeHTML('h3', 'HEIGHT SET ON THE FOLLOWING IMAGES', 'text-danger') + listImages(images))
        else:
            return(htmlconv.makeHTML('p', 'Height not set on any images &#10004', 'text-success'))

    def imageWidth(soup):
        if len(soup.findAll('img', width=True))>0:
            images = soup.findAll('img', width=True)
            return(htmlconv.makeHTML('h3', 'WIDTH SET ON THE FOLLOWING IMAGES', 'text-danger') + listImages(images))
        else:
            return(htmlconv.makeHTML('p', 'Width not set on any images &#10004', 'text-success'))
