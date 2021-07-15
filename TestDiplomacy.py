# Unit tests for Diplomacy.py

from io import StringIO
from unittest import main, TestCase

from Diplomacy import diplomacy_solve

# -----------
# TestDiplomacy
# -----------

class TestDiplomacy (TestCase):
    # -----
    # solve
    # -----

	def test_solve_1(self):
		r = StringIO("A Chicago Hold\nB NewYork Move Chicago\nC Houston Support B\nD Dallas Support A\n")
		w = StringIO()
		diplomacy_solve(r, w)
		self.assertEqual(
			w.getvalue(), "A [dead]\nB [dead]\nC Houston\nD Dallas\n")

	def test_solve_2(self):
		r = StringIO("A Barcelona Hold\nB SanFrancisco Move Chicago\nC NewYork Support B\nD LosAngeles Support A\n")
		w = StringIO()
		with self.assertRaises(KeyError):
			diplomacy_solve(r, w)

	def test_solve_3(self):
		r = StringIO("A SanDiego Move SantaBarbara\nB Reno Move SantaBarbara\nC SantaBarbara Hold\nD Dallas Move Santa Barbara\n")
		w = StringIO()
		with self.assertRaises(KeyError):
			diplomacy_solve(r, w)

	def test_solve_4(self):
		r = StringIO("A Anchorage Support B\nB Fairbanks Move Juneau\nC Juneau Hold\nD Deadhorse Move Juneau\n")
		w = StringIO()
		diplomacy_solve(r, w)
		self.assertEqual(
			w.getvalue(), "A Anchorage\nB Juneau\nC [dead]\nD [dead]\n")

# ----
# main
# ----

if __name__ == "__main__": #pragma: no cover
    main()