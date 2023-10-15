"""This is a toy repository intended for git + GitHub introductory sessions.
Good thing in those courses is, most people know one thing or two about our solar system.
"""
import random
from planets import mars


def sparkle():
    # Define a set of sparkling characters.
    sparkling_chars = '*+.o:°~ '
    
    # Generate a string of 40 random sparkling characters.
    line = "".join(random.choice(sparkling_chars) for _ in range(40))
    
    print(line)


if __name__ == "__main__":
    sparkle()
    print(">>>>  Welcome to our solar system  <<<<")
    sparkle()
    print(f"\n{mars.NAME}:")
    print(mars.DESCRIPTION)
    sparkle()
