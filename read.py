"""
File: readersandwriters.py
Project 10.7
Demonstrates shared data synchonization for the readers and writers
problem.
"""

import time, random
from threading import Thread
from sharedcell import SharedCell
from counter import Counter

class Writer(Thread):
    """Increments a counter in a shared cell."""

    def __init__(self, cell, number):
        Thread.__init__(self, name = "Writer" + str(number))
        self.cell = cell

    def run(self):
        """Sleep for a random interval and then increment
        the counter in the cell."""
        #print("%s starting up" % self.getName())
        print("%s starting up" % self.name)
        time.sleep(random.randint(1, 4))
        value = self.cell.write(lambda counter: counter.increment())
        print("%s is done incrementing to %d" % \
              #(self.getName(), value)
              (self.name, value))

class Reader(Thread):
    """Reads the value of a counter in a shared cell."""

    def __init__(self, cell, number):
        Thread.__init__(self, name = "Reader" + str(number))
        self.cell = cell

    def run(self):
        """Sleep for a random interval and then get
        the value of the counter in the cell."""
        #print("%s starting up" % self.getName())
        print("%s starting up" % self.name)
        time.sleep(random.randint(1, 4))
        value = self.cell.read(lambda counter: counter.getValue())
        #print("%s is done getting %d" % (self.getName(), value))
        print("%s is done getting %d" % (self.name, value))

def main():
    """Creates a shared cell on a Counter object, and reader and
    writer threads to increment it and observe its value."""
    counter = Counter()
    cell = SharedCell(counter)
    threads = []
    print("Creating reader threads.")
    for i in range(1, 5):
        threads.append(Reader(cell, i))
    print("Creating writer threads.")
    for i in range(1, 3):
        threads.append(Writer(cell, i))
    print("Starting the threads.")
    for thread in threads:
        thread.start()
    
if __name__ == "__main__":
    main()

