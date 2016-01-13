#output file handler.
import htmlconv

class Ofile:
	def __init__(self, filename, text):
		self.filename = filename
		self.text = text

	def append(self, text):
		self.text +=text

	def writeout(self):
		f = open(self.filename, 'w')
		f.write(self.text)

	def seed25(self):
		self.text += htmlconv.style()
		self.text += htmlconv.h1('Report 40%')
		self.text += htmlconv.h2('Wireframes 10%')
		self.text += htmlconv.p('********')
		self.text += htmlconv.h2('Report 30%')
		self.text += htmlconv.p('********')
		self.text += htmlconv.h1('Website 60%')
		self.text += htmlconv.h2('Usability et. al. 15%')
		self.text += htmlconv.p('********')
		self.text += htmlconv.h2('Design Aesthetic 10%')
		self.text += htmlconv.p('********')
		self.text += htmlconv.h2('Responsive Design 15%')
		self.text += htmlconv.p('********')
		self.text += htmlconv.h2('Professional Chrome 10%')
		self.text += htmlconv.p('********')
		self.text += htmlconv.h2('HTML Validation 5%')
		self.text += htmlconv.p('********')
		self.text += htmlconv.h2('CSS Validation 5%')
		self.text += htmlconv.p('********')