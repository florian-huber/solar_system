"""This is a toy repository intended for git + GitHub introductory sessions.
Good thing in those courses is, most people know one thing or two about our solar system.
"""
import random
from planets import mars


def sparkle(width: int = 60, num_sparkle_lines: int = 2):
    # Define a set of sparkling characters.
    sparkling_chars = "*+.°^><o°~\'" + 100 * " "  # more spaces means more cosmic emptyness
    
    for _ in range(num_sparkle_lines):
        # Generate a string of `width` random sparkling characters.
        line = "".join(random.choice(sparkling_chars) for _ in range(width))
        print(line)


if __name__ == "__main__":
    sparkle(num_sparkle_lines=3)
    print(f"{8 * '<>'} Welcome to our solar system {8 * '<>'}")
    sparkle(num_sparkle_lines=3)
    print(f"{mars.NAME.upper()}:")
    print(mars.DESCRIPTION)
    sparkle()
