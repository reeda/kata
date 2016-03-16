import unittest

class Game():

	def __init__(self):
		self.rolls = []

	def roll(self, pins):
		self.rolls.append(pins)

	def get_score(self):
		score = 0
#		print(self.rolls)
		frameIndex = 0
		for frame in range(10):
			if (self.is_strike(frameIndex)):
				score += 10 + self.strike_bonus(frameIndex)
				frameIndex += 1
			elif (self.is_spare(frameIndex)):
				score += 10 + self.spare_bonus(frameIndex)
				frameIndex += 2
			else:
				score += self.sum_of_balls_in_frame(frameIndex)
				frameIndex += 2

		return score

	def is_spare(self, frameIndex):
		return self.rolls[frameIndex] + self.rolls[frameIndex + 1] == 10

	def is_strike(self, frameIndex):
		return self.rolls[frameIndex] == 10

	def strike_bonus(self, frameIndex):
		return self.rolls[frameIndex + 1] + self.rolls[frameIndex + 2]

	def spare_bonus(self, frameIndex):
		return self.rolls[frameIndex + 2]

	def sum_of_balls_in_frame(self, frameIndex):
		return self.rolls[frameIndex] + self.rolls[frameIndex + 1]

class TestBowlingGame(unittest.TestCase):
	def setUp(self):
		self.g = Game()
	def test_gutter_game(self):
		self.rollMany(20, 0)
		self.assertEqual(self.g.get_score(), 0)

	def test_all_ones(self):
		self.rollMany(20, 1)
		self.assertEqual(self.g.get_score(), 20)

	def test_one_spare(self):
		self.rollSpare()
		self.g.roll(3)
		self.rollMany(17, 0)
		self.assertEqual(self.g.get_score(), 16)

	def test_one_strike(self):
		self.rollStrike()
		self.g.roll(3)
		self.g.roll(4)
		self.rollMany(17, 0)
		self.assertEqual(self.g.get_score(), 24)

	def test_perfect_game(self):
		self.rollMany(12, 10)
		self.assertEqual(self.g.get_score(), 300)

	def rollMany(self, n, pins):
		for i in range(n):
			self.g.roll(pins)

	def rollSpare(self):
		self.g.roll(5)
		self.g.roll(5)

	def rollStrike(self):
		self.g.roll(10)

if __name__ == '__main__':
    unittest.main()
