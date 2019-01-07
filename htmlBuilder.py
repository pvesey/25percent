from xml.dom import minidom
#from html import HTML

class htmlBuilder():
    """docstring for htmlBuilder."""
    def __init__(self, filename):
        super(htmlBuilder, self).__init__()
        self.filename = filename
        self.document = minidom.getDOMImplementation().createDocument(None, "html", None)
        top_element = self.document.documentElement
        head = self.document.createTextNode('head')

        top_element.appendChild(head)
        #self.document.appendChild('body')

        #print(self.document.toxml())

        # raise Exception("This is an exception")

    def appendChild(self, element):

        return

    def prependChild(self, element):

        return


    def writeHTML(self):
        o = open(self.filename, 'w')
        o.write(self.document.toxml())

        return
