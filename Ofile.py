#output file handler.
import htmlconv

class Ofile:
	def __init__(self, filename, text):
		self.filename = filename
		self.text = text

	def append(self, text):
		self.text +=(text + '\n')

	def writeout(self):
		f = open(self.filename, 'w')
		f.write(self.text)

	def seed25(self):

		self.text += (htmlconv.h1('Report 40%') + '\n')
		self.text += (htmlconv.h2('Wireframes 10%') + '\n')
		self.text += (htmlconv.p('********') + '\n')
		self.text += (htmlconv.h2('Report 30%') + '\n')
		self.text += (htmlconv.p('********') + '\n')
		self.text += (htmlconv.h1('Website 60%') + '\n')
		self.text += (htmlconv.h2('Usability et. al. 15%') + '\n')
		self.text += (htmlconv.p('********') + '\n')
		self.text += (htmlconv.h2('Design Aesthetic 10%') + '\n')
		self.text += (htmlconv.p('********') + '\n')
		self.text += (htmlconv.h2('Responsive Design 15%') + '\n')
		self.text += (htmlconv.p('********') + '\n')
		self.text += (htmlconv.h2('Professional Chrome 10%') + '\n')
		self.text += (htmlconv.p('********') + '\n')
		self.text += (htmlconv.h2('HTML Validation 5%') + '\n')
		self.text += (htmlconv.p('********') + '\n')
		self.text += (htmlconv.h2('CSS Validation 5%') + '\n')
		self.text += (htmlconv.p('********') + '\n')


		self.text += ('<table>' + '\n')
		self.text += ('' + '\n')
		self.text += ('<th>' + '\n')
		self.text += ('<td>Element</td>' + '\n')
		self.text += ('<td>% Allocation</td>' + '\n')
		self.text += ('<td>% Mark</td>' + '\n')
		self.text += ('</th>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>Report</td><td>30%</td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>Wireframes</td>10%<td></td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>Usability</td>15%<td></td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>Design Aesthetic</td><td>10%</td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>Responsive Design</td>15%<td></td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>Professional Chrome</td>10%<td></td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>HTML Validation</td>5%<td></td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>CSS Validation</td>5%<td></td><td></td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('</table>' + '\n')



	def seed50(self):

		self.text += htmlconv.toH1('Overall Result - xx%')
		self.text += htmlconv.toH2('Report 25%')
		self.text += htmlconv.toP('Comments')
		self.text += htmlconv.toH2('Website 50%')
		self.text += htmlconv.toP('Comments')
		self.text += htmlconv.toH2('Learner Implementations 15%')
		self.text += htmlconv.toP('Comments')
		self.text += htmlconv.toH2('Presentation 10%')
		self.text += htmlconv.toP('Comments')
