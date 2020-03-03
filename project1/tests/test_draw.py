#!/bin/env python3.7
import sys
sys.path.append('../..')
from graph.graph import graph

graph.create_from_file().draw()
