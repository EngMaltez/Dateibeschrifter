#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Create md5_label table.

time spent: 🍅

@author Miguel Maltez Jose
@date 20231105
"""
import argparse
import sqlite3
import logging

def main():
	"""There can be only one!"""
	parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
	parser.add_argument("--db"
		, help="database file"
		, default="test.db"
		)
	args = parser.parse_args()
	#
	with sqlite3.connect(args.db) as conn:
		conn.execute("CREATE TABLE md5_label(md5 TEXT, label TEXT)")

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	main()
