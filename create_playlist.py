#!/usr/bin/env python3

# Utility function
def get_keypress(timeout=10.0):
	"""
	Checks if a key was pressed during the timeout period.
	Returns the key as a string if pressed, otherwise None.

	Args
	----
	timeout: float
		How many seconds to wait before registering any input from the user

	Returns
	-------
	user input
		The character inputted by the user within timeout duration, if no input found then returns None
	"""
	
	fd = sys.stdin.fileno() # 0 -> File descriptor for std input, required for low-level operations
	old_settings = termios.tcgetattr(fd) # Store the current terminal settings
	
	try:
		tty.setcbreak(fd)  # Set terminal to character-by-character mode (no need to press enter to register input)
		rlist, _, _ = select.select([fd], [], [], timeout)
		if rlist:
			return sys.stdin.read(1)
		return None
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings) # Restore the old terminal settings
		
def create_playlist(audio_dir_path: str):
	"""
	Plays .mp3 songs randomly from a given directory from command line.
	Press 's' to skip the current song.
	If the song is skipped then move it to the skipped folder.
	
	Args
	----
	audio_dir_path: str
		Directory path containing atleast one .mp3 songs
	
	Returns
	-------
	None
	"""
	
	audio_dir_path = Path(audio_dir_path)
	
	#-----------------------------------------------
	# Creating directory to move skipped songs
	#-----------------------------------------------
	SKIPPED_DIR_PATH = audio_dir_path.parents[0] / "skipped-songs" # Directory where skipped songs will be moved
	SKIPPED_DIR_PATH.mkdir(parents=True, exist_ok=True)
	
	#-----------------------------------------------
	# Listing all the songs in the directory
	#-----------------------------------------------
	songs = list((audio_dir_path).rglob("*.mp3")) # Get list of all the songs in the directory
	if not songs:
		raise FileNotFoundError(f"No mp3 files in the directory {audio_dir_path}")
	
	random.shuffle(songs)
	
	#-----------------------------------------------
	# Initiating music player
	#-----------------------------------------------
	for song in songs:
		song_duration = File(str(song)).info.length
		print(f"\nNow playing: {song.name} || {song_duration:.0f} sec")
		
		process = subprocess.Popen(
			["mpg123", str(song)],
			stdout=subprocess.DEVNULL,
			stderr=subprocess.DEVNULL
		) # Plays the song using mpg123 library
		
		while process.poll() is None: # .pool return None if the process is going on
			key = get_keypress(timeout=0.5)
			if key == 's':
				process.terminate()
				shutil.move(src=song, dst=SKIPPED_DIR_PATH / song.name)				
				print(f"The song is skipped and moved to {SKIPPED_DIR_PATH} folder.")
				break # Jump to next song
			
	print("\n-----------All songs played.----------------")

if __name__ == "__main__":
	import sys
	from pathlib import Path
	import argparse
	import select
	import termios
	import tty
	import subprocess
	import random
	import shutil
	from mutagen import File # Can read the metadata of audio file, using it to get audio duration without loading the song into memory
	
	parser = argparse.ArgumentParser(description="Music Player - Press 's' to skip the song")
	parser.add_argument("-i", "--input", type=str, required=True, help="Path to directory containing .mp3 files")
	args = parser.parse_args()
	create_playlist(args.input)