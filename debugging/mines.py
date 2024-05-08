#!/usr/bin/python3
import random
import os

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
	def __init__(self, width=10, height=10, mines=10):
		self.width = width
		self.height = height
		self.mines = set(random.sample(range(width * height), mines))
		self.field = [[' ' for _ in range(width)] for _ in range(height)]
		self.revealed = [[False for _ in range(width)] for _ in range(height)]

	def print_board(self, reveal=False):
		clear_screen()
		print('  ' + ' '.join(str(i) for i in range(self.width)))
		for y in range(self.height):
			print(y, end=' ')
			for x in range(self.width):
				if reveal or self.revealed[y][x]:
					if (y * self.width + x) in self.mines:
						print('*', end=' ')
					else:
						count = self.count_mines_nearby(x, y)
						print(count if count > 0 else ' ', end=' ')
				else:
					print('.', end=' ')
			print()

	def count_mines_nearby(self, x, y):
		count = 0
		for dx in [-1, 0, 1]:
			for dy in [-1, 0, 1]:
				nx, ny = x + dx, y + dy
				if 0 <= nx < self.width and 0 <= ny < self.height:
					if (ny * self.width + nx) in self.mines:
						count += 1
		return count

	def reveal(self, x, y):
		if (y * self.width + x) in self.mines:
			return False
		self.revealed[y][x] = True
		if self.count_mines_nearby(x, y) == 0:
			for dx in [-1, 0, 1]:
				for dy in [-1, 0, 1]:
					nx, ny = x + dx, y + dy
					if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
						self.reveal(nx, ny)
		return True
	
	def check_win(self):
		# Calculate the total number of non-mine cells
		non_mine_count = self.width * self.height - len(self.mines)
		
		# Count the number of revealed cells
		revealed_count = sum(sum(row) for row in self.revealed)
		
		# If all non-mine cells are revealed, it's a win
		return revealed_count == non_mine_count

	def play(self):
		while True:
			self.print_board()
			try:
				# Get the user's input for coordinates
				x = int(input("Enter x coordinate: "))
				y = int(input("Enter y coordinate: "))
				
				# If the player hits a mine, game over
				if not self.reveal(x, y):
					self.print_board(reveal=True)
					print("Game Over! You hit a mine.")
					break
				
				# Check if the player has won
				elif self.check_win():
					self.print_board()
					print("Congratulations! You revealed all non-mine cells. You win!")
					break
			
			except ValueError:
				print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
	game = Minesweeper()
	game.play()
