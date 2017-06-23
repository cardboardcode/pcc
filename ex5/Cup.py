#!/usr/bin/env python

class Cup:
	coffee = 0

	def _init_(self):
		self.coffee = 0

	def check(self):
		print("The cup has " + str(self.coffee) + "cm3 of coffee.")

	def empty(self):
		self.coffee = 0

	def topupfull(self):
		self.coffee = 20

	def topuphalf(self):
		self.coffee = 10

	def topup(self, add):
		if ((self.coffee + add)< 20):
			self.coffee += add
		else:
			print("You will spill coffee.")

	def observe(self):
		if (self.coffee == 10):
			print("The cup is half full.")
		else:
			print("The cup is not half full")

	
		