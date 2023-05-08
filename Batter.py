# Class Representing Each Batter

class Batter:
	def __init__(self, first_name, last_name, games, atbats,
	       runs, hits, doubles, triples, homeruns, rbi, tb, bb, so, sb, ave, obp, slg, ops, war):
		self.first_name = first_name
		self.last_name = last_name
		self.games = games
		self.atbats = atbats
		self.runs = runs
		self.hits = hits
		self.doubles = doubles
		self.triples = triples
		self.homeruns = homeruns
		self.rbi = rbi
		self.tb = tb
		self.bb = bb
		self.so = so
		self.sb = sb
		self.ave = ave
		self.obp = obp
		self.slg = slg
		self.ops = ops

	def __str__(self):
		return self.first_name + " " + self.last_name + " " + self.grade + " " + self.classroom + " " + self.bus + " " + self.gpa + " " + self.teacher_last + " " + self.teacher_first