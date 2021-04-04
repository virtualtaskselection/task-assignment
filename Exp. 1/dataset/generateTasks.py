#This script generates the combination of images to be used in the tasks

import random

class DataSet:
	def __init__(self, set1, set2, set3):
	    self.set1 = set1
	    self.set2 = set2
	    self.set3 = set3

#filenames from the Caltech-UCSD Birds 200 images data set
brewersBlackbird=["Brewer_Blackbird_0001_13030268.jpg", "Brewer_Blackbird_0002_2999630226.jpg", "Brewer_Blackbird_0003_327559139.jpg", "Brewer_Blackbird_0004_13489955.jpg", "Brewer_Blackbird_0005_2600344465.jpg", "Brewer_Blackbird_0006_409296172.jpg", "Brewer_Blackbird_0007_2467073350.jpg", "Brewer_Blackbird_0008_2916336305.jpg", "Brewer_Blackbird_0009_327560725.jpg", "Brewer_Blackbird_0010_2487470293.jpg", "Brewer_Blackbird_0011_2586016547.jpg", "Brewer_Blackbird_0012_743374198.jpg", "Brewer_Blackbird_0013_1947920591.jpg", "Brewer_Blackbird_0014_2560745108.jpg", "Brewer_Blackbird_0015_469388537.jpg", "Brewer_Blackbird_0016_162093642.jpg", "Brewer_Blackbird_0017_192822407.jpg", "Brewer_Blackbird_0018_253049825.jpg", "Brewer_Blackbird_0019_2423872869.jpg", "Brewer_Blackbird_0020_2521712243.jpg", "Brewer_Blackbird_0021_2600945880.jpg", "Brewer_Blackbird_0022_2498669546.jpg", "Brewer_Blackbird_0023_2405792169.jpg", "Brewer_Blackbird_0024_3031249630.jpg", "Brewer_Blackbird_0025_2873028499.jpg", "Brewer_Blackbird_0026_223907458.jpg"]

redWingedBlackbird=["Red_winged_Blackbird_0001_2370065784.jpg", "Red_winged_Blackbird_0002_138027313.jpg", "Red_winged_Blackbird_0003_2435737741.jpg", "Red_winged_Blackbird_0004_2209034288.jpg", "Red_winged_Blackbird_0005_865242258.jpg", "Red_winged_Blackbird_0006_2376861574.jpg", "Red_winged_Blackbird_0007_495139194.jpg", "Red_winged_Blackbird_0008_469101650.jpg", "Red_winged_Blackbird_0009_2472004320.jpg", "Red_winged_Blackbird_0010_465415726.jpg", "Red_winged_Blackbird_0011_495139158.jpg", "Red_winged_Blackbird_0012_2472606189.jpg", "Red_winged_Blackbird_0013_139596958.jpg", "Red_winged_Blackbird_0014_144916612.jpg", "Red_winged_Blackbird_0015_469101656.jpg", "Red_winged_Blackbird_0016_102414646.jpg", "Red_winged_Blackbird_0017_583846699.jpg", "Red_winged_Blackbird_0018_2477592974.jpg", "Red_winged_Blackbird_0019_398266170.jpg", "Red_winged_Blackbird_0020_474690970.jpg", "Red_winged_Blackbird_0021_2529270051.jpg", "Red_winged_Blackbird_0022_2179939448.jpg", "Red_winged_Blackbird_0023_519203903.jpg", "Red_winged_Blackbird_0024_16024607.jpg", "Red_winged_Blackbird_0025_2460801057.jpg", "Red_winged_Blackbird_0026_2201165026.jpg", "Red_winged_Blackbird_0027_2419463190.jpg"]

bronzedCowbird=["Bronzed_Cowbird_0001_2660673621.jpg", "Bronzed_Cowbird_0002_2660673463.jpg", "Bronzed_Cowbird_0003_446682575.jpg", "Bronzed_Cowbird_0004_2407136000.jpg", "Bronzed_Cowbird_0005_816113586.jpg", "Bronzed_Cowbird_0006_483532429.jpg", "Bronzed_Cowbird_0007_424570095.jpg", "Bronzed_Cowbird_0008_815138925.jpg", "Bronzed_Cowbird_0009_815138425.jpg", "Bronzed_Cowbird_0010_816113556.jpg", "Bronzed_Cowbird_0011_815138541.jpg", "Bronzed_Cowbird_0012_815138567.jpg", "Bronzed_Cowbird_0013_2417085161.jpg", "Bronzed_Cowbird_0014_2256262769.jpg", "Bronzed_Cowbird_0015_59207957.jpg", "Bronzed_Cowbird_0016_815138575.jpg", "Bronzed_Cowbird_0017_2417906344.jpg", "Bronzed_Cowbird_0018_59205913.jpg", "Bronzed_Cowbird_0019_3092637207.jpg", "Bronzed_Cowbird_0020_3092637605.jpg", "Bronzed_Cowbird_0021_3056098406.jpg", "Bronzed_Cowbird_0022_3055262329.jpg", "Bronzed_Cowbird_0023_2740056869.jpg", "Bronzed_Cowbird_0024_446633377.jpg", "Bronzed_Cowbird_0025_446633937.jpg"]

rustyBlackbird=["Rusty_Blackbird_0001_2997059133.jpg", "Rusty_Blackbird_0002_2170471346.jpg", "Rusty_Blackbird_0003_1837259916.jpg", "Rusty_Blackbird_0004_1848793704.jpg", "Rusty_Blackbird_0005_2993973180.jpg", "Rusty_Blackbird_0006_1847962479.jpg", "Rusty_Blackbird_0007_2393337841.jpg", "Rusty_Blackbird_0008_105553567.jpg", "Rusty_Blackbird_0009_62306686.jpg", "Rusty_Blackbird_0010_3077782792.jpg", "Rusty_Blackbird_0011_1847956717.jpg", "Rusty_Blackbird_0012_501238584.jpg", "Rusty_Blackbird_0013_62306687.jpg", "Rusty_Blackbird_0014_501239850.jpg", "Rusty_Blackbird_0015_2302384820.jpg", "Rusty_Blackbird_0016_344778530.jpg", "Rusty_Blackbird_0017_2961421713.jpg", "Rusty_Blackbird_0018_3070162963.jpg", "Rusty_Blackbird_0019_2281281703.jpg", "Rusty_Blackbird_0020_2505459830.jpg", "Rusty_Blackbird_0021_1922903657.jpg", "Rusty_Blackbird_0022_968932549.jpg", "Rusty_Blackbird_0023_2202235567.jpg", "Rusty_Blackbird_0024_2152893106.jpg", "Rusty_Blackbird_0025_1922906301.jpg", "Rusty_Blackbird_0026_2393065469.jpg", "Rusty_Blackbird_0027_2230061718.jpg"]

def generateCombinations(imageSet1, imageSet2):
	combinations = set()
	for x in imageSet1:
		for y in imageSet2:
			str = x + ", " + y
			combinations.add(str)
	return combinations


def getTasks(dataset, n):
#n = number of tasks to select per set
#total number of tasks to be returned is n * 3

	tasks = set()

	set1Q = random.sample(dataset.set1, k=n)
	tasks.update(set1Q)
	dataset.set1 = dataset.set1.difference(set1Q)

	set2Q = random.sample(dataset.set2, k=n)
	tasks.update(set2Q)
	dataset.set2 = dataset.set2.difference(set2Q)

	set3Q = random.sample(dataset.set3, k=n)
	tasks.update(set3Q)
	dataset.set3 = dataset.set3.difference(set3Q)
	
	return tasks

def main():

	ds = DataSet(generateCombinations(redWingedBlackbird, bronzedCowbird), generateCombinations(bronzedCowbird, brewersBlackbird), generateCombinations(brewersBlackbird, rustyBlackbird))

	#randomly select 15 tasks for the qualification test 
	qualifTest = getTasks(ds, 5)
	print('Qualification Test')
	for x in qualifTest:
		print(x)

	#randomly select 15 tasks for the post test
	postTest = getTasks(ds, 5)
	print('\n\nPost Test')
	for x in postTest:
		print(x)

	#randomly select 120 tasks for the qualification tests
	treatmentTest = getTasks(ds, 40)
	print('\n\nTreatment Test')
	for x in treatmentTest:
		print(x)


main()