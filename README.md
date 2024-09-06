# NYT Letterboxed Solver
Python3 scripts to solve NYT's Letterboxed (https://www.nytimes.com/puzzles/letter-boxed)

## Usage
`python solver.py` to find the shortest solution (fewest words)  
or  
`python solver-perfect.py` to find the shortest 12-letter solution (uses each letter once)  
  
`solver-perfect.py` requires [bitarray](https://pypi.org/project/bitarray/)  
both solvers return only the first optimal solution found


## Parameters
`wordlist` is a path to a newline-separated list of words to use in a solution (see `example-wordlist.txt`)  
`sides` is a comma separated string of usable letters (e.g. `sma,qlr,yoe,buv`), where each group of 3 represents a side of the box
