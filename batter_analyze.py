# Major League Baseball Statistical Analysis for Batters
import csv
def main():
	batters = []
	try:
		with open("/Users/jasonbarba/Projects/MLB_Statistics_Analysis/WhiteSox_Batting_2022.csv", 'r') as file:
			csvreader = csv.reader(file)
			for batter in csvreader:
				batters.append(batter)
	except:
		print("Could not open file")
		return None
	# print(contents)
	print(batters[1])
	

if __name__ == "__main__":
	main()