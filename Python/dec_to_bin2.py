dec = input('Enter a decimal number : ')
bin = 0
base = 1

def main():
		global dec
		global bin
		global base

		if dec > 0:
				rem = dec%2
				bin = bin + rem*base
				base = base * 10
				dec = dec / 2
		else:
				print bin
				exit(0)
		main()

main()
