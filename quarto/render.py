
import sys
import subprocess

from quarto.quarto import find_quarto

def render(input):
  args = ["render", input]
  process = subprocess.Popen([find_quarto()] + args)
  process.wait()


