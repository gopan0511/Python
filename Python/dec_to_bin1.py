def main():
		dec = 10
		bin = 0
		base =1

		while dec > 0:
				rem = dec%2
				bin = bin + rem*base
				base = base * 10
				dec = dec / 2
		print bin

main()