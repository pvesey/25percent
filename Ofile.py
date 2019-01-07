#output file handler.
import htmlconv
from htmlBuilder import htmlBuilder
from xml.dom import minidom

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

		self.text += ("<table class='table'>" + "\n")
		self.text += ('<tr>' + '\n')
		self.text += ('  <th>Element</th>' + '\n')
		self.text += ('  <th>% Allocation</th>' + '\n')
		self.text += ('  <th>% Mark</th>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Report</td><td>30%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Wireframes</td><td>10%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Usability</td><td>15%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Design Aesthetic</td><td>10%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Responsive Design</td><td>15%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Professional Chrome</td><td>10%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('  <tr>' + '\n')
		self.text += ('<td>HTML Validation</td><td>5%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>CSS Validation</td><td>5%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('<td>Totals</td><td>5%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')

		self.text += ('</table>' + '\n')

		itest = htmlBuilder('builder.html')
		print(itest)
		itest.writeHTML()

	def seed50(self):

		self.text += htmlconv.toH1('Overall Result - xx%')

		self.text += ("<table class='table'>" + "\n")
		self.text += ('<tr>' + '\n')
		self.text += ('  <th>Element</th>' + '\n')
		self.text += ('  <th>% Allocation</th>' + '\n')
		self.text += ('  <th>% Mark</th>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Report</td><td>25%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Website </td><td>50%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Learner Implementations</td><td>15%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('<tr>' + '\n')
		self.text += ('  <td>Design Presentation</td><td>10%</td><td>---</td>' + '\n')
		self.text += ('</tr>' + '\n')
		self.text += ('</table>' + '\n')
