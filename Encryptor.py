import pyAesCrypt 
import os

files = os.listdir()

def main():
	passw = "solstice"
	bufferSize = 64 * 1024
	for file in files:
		try:
			pyAesCrypt.encryptFile(file, file + ".out", passw, bufferSize)
			print("Enccrypted")
		except:
			print("unsucessful")

if __name__ == "__main__":
	main()