"""Eric Bronner, Paul Tai, Patrick Wu"""

import math

class heap(object):

	"""Array-based binary heap implementation"""	

	def __init__(self):
		"""Initialize data to an empty list, set size to 0"""
		self.heap_data = []
		self.size = 0

	def add(self, data):
		"""Add new data to the end of the list and sift it up"""
		self.heap_data.append(data)
		self.size += 1
		self.sift_up(len(self.heap_data) - 1)

	def delete(self):
		"""Remove and return smallest data from the heap"""
		temp = self.heap_data[0]
		self.heap_data[0] = self.heap_data[len(self.heap_data) - 1]
		del(self.heap_data[-1])
		self.size -= 1
		self.sift_down(0)
		return temp

	def sift_up(self, index):
		"""Move data up the list to its proper placement"""
		while index != 0:
			p = self.parent(index)
			p = int(p)
			if self.heap_data[index] < self.heap_data[p]:
				self.swap(index, p)
				index = p
			else:
				break

	def sift_down(self, index):
		"""Move data down the list to its proper placement"""
		r_index = self.right_child(index)
		l_index = self.left_child(index)
		#if the root is less than both of its children, it is in the correct position; break
		if self.heap_data[index] < self.heap_data[r_index] and self.heap_data[index] < self.heap_data[l_index]:
			return
		else:
			if self.heap_data[r_index] < self.heap_data[l_index]:
				smaller = r_index
			else:
				smaller = l_index
			self.swap(index, smaller)
		self.sift_down(smaller)

	def heapsort(self):
		"""Heapsort the heap"""
		for i in self.size:
			self.sift_up(i)
		for i in self.size:
			self.sift_down(self.size - i -1)	

	def swap(self, ind1, ind2):
		temp = self.heap_data[ind1]
		self.heap_data[ind1] = self.heap_data[ind2]
		self.heap_data[ind2] = temp

	def parent(self, index):
		"""Returns index of another index's parent"""
		return math.floor((index - 1) / 2)

	def left_child(self, index):
		"""Returns index of another index's left child"""
		return ((index * 2) + 1)

	def right_child(self, index):
		"""Returns index of another index's right child"""
		return ((index * 2) + 2)

h = heap()
h.add(3)
h.add(4)
h.add(2)
h.add(8)
h.add(6)
h.add(12)
h.add(10)
h.add(5)
print h.heap_data
print h.delete()
print h.heap_data
