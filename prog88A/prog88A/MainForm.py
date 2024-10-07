import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._label13 = System.Windows.Forms.Label()
		self._label14 = System.Windows.Forms.Label()
		self._label15 = System.Windows.Forms.Label()
		self._label16 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.GreenYellow
		self._label1.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label1.Location = System.Drawing.Point(12, 53)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(100, 29)
		self._label1.TabIndex = 0
		self._label1.Text = "label1"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.GreenYellow
		self._label2.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label2.Location = System.Drawing.Point(11, 99)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 29)
		self._label2.TabIndex = 1
		self._label2.Text = "label2"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.GreenYellow
		self._label3.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label3.Location = System.Drawing.Point(11, 145)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 29)
		self._label3.TabIndex = 2
		self._label3.Text = "label3"
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.GreenYellow
		self._label4.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label4.Location = System.Drawing.Point(14, 186)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(100, 29)
		self._label4.TabIndex = 3
		self._label4.Text = "label4"
		self._label4.Click += self.Label4Click
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.GreenYellow
		self._label5.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label5.Location = System.Drawing.Point(14, 228)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(100, 29)
		self._label5.TabIndex = 4
		self._label5.Text = "label5"
		self._label5.Click += self.Label5Click
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.GreenYellow
		self._label6.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label6.Location = System.Drawing.Point(14, 272)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(100, 29)
		self._label6.TabIndex = 5
		self._label6.Text = "label6"
		self._label6.Click += self.Label6Click
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.GreenYellow
		self._label7.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label7.Location = System.Drawing.Point(14, 316)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(100, 29)
		self._label7.TabIndex = 6
		self._label7.Text = "label7"
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.GreenYellow
		self._label8.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label8.Location = System.Drawing.Point(14, 357)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(100, 29)
		self._label8.TabIndex = 7
		self._label8.Text = "label8"
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.GreenYellow
		self._label9.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label9.Location = System.Drawing.Point(133, 53)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(100, 29)
		self._label9.TabIndex = 8
		self._label9.Text = "label9"
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.GreenYellow
		self._label10.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label10.Location = System.Drawing.Point(133, 99)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(100, 29)
		self._label10.TabIndex = 9
		self._label10.Text = "label10"
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.GreenYellow
		self._label11.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label11.Location = System.Drawing.Point(133, 145)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(100, 29)
		self._label11.TabIndex = 10
		self._label11.Text = "label11"
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.GreenYellow
		self._label12.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label12.Location = System.Drawing.Point(133, 186)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(100, 29)
		self._label12.TabIndex = 11
		self._label12.Text = "label12"
		# 
		# label13
		# 
		self._label13.BackColor = System.Drawing.Color.GreenYellow
		self._label13.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label13.Location = System.Drawing.Point(133, 228)
		self._label13.Name = "label13"
		self._label13.Size = System.Drawing.Size(100, 29)
		self._label13.TabIndex = 12
		self._label13.Text = "label13"
		# 
		# label14
		# 
		self._label14.BackColor = System.Drawing.Color.GreenYellow
		self._label14.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label14.Location = System.Drawing.Point(133, 272)
		self._label14.Name = "label14"
		self._label14.Size = System.Drawing.Size(100, 29)
		self._label14.TabIndex = 13
		self._label14.Text = "label14"
		# 
		# label15
		# 
		self._label15.BackColor = System.Drawing.Color.GreenYellow
		self._label15.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label15.Location = System.Drawing.Point(133, 316)
		self._label15.Name = "label15"
		self._label15.Size = System.Drawing.Size(100, 29)
		self._label15.TabIndex = 14
		self._label15.Text = "label15"
		# 
		# label16
		# 
		self._label16.BackColor = System.Drawing.Color.GreenYellow
		self._label16.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle
		self._label16.Location = System.Drawing.Point(133, 357)
		self._label16.Name = "label16"
		self._label16.Size = System.Drawing.Size(100, 29)
		self._label16.TabIndex = 15
		self._label16.Text = "label16"
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(14, 389)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(97, 46)
		self._button1.TabIndex = 16
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(136, 389)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(97, 46)
		self._button2.TabIndex = 17
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(254, 389)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(97, 46)
		self._button3.TabIndex = 18
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.SystemColors.ActiveBorder
		self.ClientSize = System.Drawing.Size(363, 448)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label16)
		self.Controls.Add(self._label15)
		self.Controls.Add(self._label14)
		self.Controls.Add(self._label13)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "prog88A"
		self.ResumeLayout(False)
		

	def Button1Click(self, sender, e): #calculate
		num1 = int(self._textBox1.Text)
		num2 = int(self._textBox2.Text)
		Sum = num1 + num2
		Dif = num1 - num2
		Abs = abs(Dif)
		Max = 0
		Min = 0
		if nim1 >= num2
			Max = num1
		else: #otherwise
			Max = num2
			
			if Max == num1:
				Min = num2
			else:
				Min = num1
				
		self._label15.Text = str(Max)
		self._label16.Text = str(Min)

	def Button2Click(self, sender, e): #clear
		self._textBox1.Text = ""
		self._textBox2.Text = ""
	def Button3Click(self, sender, e): #exit
		Application.Exit() 

	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label4Click(self, sender, e):
		pass

	def Label5Click(self, sender, e):
		pass

	def Label6Click(self, sender, e):
		pass