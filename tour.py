import sys

class Tour:
    """Class to handle Knight's tour problem"""

    def __init__(self, width, height):
        """Initialize a tour class
		
        - width: int: The width of the board
        - height: int: The height of the board
        """

		# Create instance variables for width and height
        self.width = width
        self.height = height

		
        self.chess_board = []
        self._initialize_board()

    def _initialize_board(self):
        """Zero out each element in the chess board
		
        This is so we can keep track of each element touched
        """
	
        for _ in range(self.height):
            self.chess_board.append([0] * self.width)

    def print_board(self):
        """Print the chess board by iterating through list"""
		
        for element in self.chess_board:
            print(element)
        print("\n")

    def _find_legal_moves(self, board_position):
        """Find the moves that are possible for this specific position"""
	
        possible_pos = []
		
		# These are all 'possible moves' that a knight can make
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

		# Iterate through each possible move and determine if it 
		# is valid for the specific position we are at
        for move in move_offsets:
            new_x = board_position[0] + move[0]
            new_y = board_position[1] + move[1]

            if (new_x >= self.height) or \
               (new_y >= self.width) or \
			   (new_x < 0) or \
			   (new_y < 0):
                continue
            else:
                possible_pos.append((new_x, new_y))
        return possible_pos

    def _sort_possible_moves(self, to_visit):
        """Create a list of the best paths to go to"""

        neighbor_list = self._find_legal_moves(to_visit)
        unvisited_neighbors = []

		# Go through each legal move and determine if the new position
		# knight would be placed at is empty. If so, append to list of empty neighbors
        for neighbor in neighbor_list:
            np_value = self.chess_board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                unvisited_neighbors.append(neighbor)

		# Now, iterate through every unvisited neighbors and determine the possible moves
		# for that spot. This will help us determine the path that is the best to go to.
        scores = []
        for empty_neigh in unvisited_neighbors:
            score = [empty_neigh, 0]
            moves = self._find_legal_moves(empty_neigh)
            for m in moves:
                if self.chess_board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

		# Create a sorted list of best neighbors to go to,
		# which was determined by the score --> the number of open spots it has open
        scores_sort = sorted(scores, key=lambda s: s[1])
        sorted_neighbors = [s[0] for s in scores_sort]
        return sorted_neighbors

    def tour(self, board_spot=(0,0), path=[], visited_num=1):
        """This is the main function to find the tour of the knight.

        The function takes in a board_spot, which is the current spot on the board
        and path, which is the path the knight has taken.
		
        The function returns the path that was taken by knight
        """

		# We made it one step closer through tour, place the current number
		# in the current slot and appent the tupled spot in board
        self.chess_board[board_spot[0]][board_spot[1]] = visited_num
        path.append(board_spot)
		
		# Base case of recursion --> if the number visited is equal to the 
		# height times the width of the board, we know we completed the tour
		# return the path of the tour after printing current outlook of board
        if visited_num == self.width * self.height:
            self.print_board()
            return path
			
		# Not at the end yet --> find next possible moves to make
        else:
            sorted_neighbors = self._sort_possible_moves(board_spot)
            for neighbor in sorted_neighbors:
                final = self.tour(neighbor, path, visited_num + 1)
                if final: return final
            
			# The current path we are leading on did not lead to results
			# We need to remove the current board spot from path and peel back
            self.chess_board[board_spot[0]][board_spot[1]] = 0
            try:
	            path.pop()
            except IndexError:
                sys.exit(1)
        return None
		
if __name__ == '__main__':

    sys.setrecursionlimit(10000)
    tour = Tour(10, 10)
    path = tour.tour()
    print(path)