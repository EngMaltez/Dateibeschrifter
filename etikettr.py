#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Labels file.

time spent: 🍅

@author Miguel Maltez Jose
@date 20231105
"""
import hashlib
import sqlite3
import logging
import argparse

def main():
	"""There can be only one!"""
	parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
	parser.add_argument("file"
		, type=argparse.FileType('rb')
		)
	parser.add_argument("--db"
		, help="database file"
		, default="test.db"
		)
	args = parser.parse_args()
	#
	md5 = hashlib.md5(args.file.read()).hexdigest()
	print(md5, args.file.name)
	with sqlite3.connect(args.db) as conn:
		cur = conn.execute("SELECT * FROM md5_label WHERE md5=?", (md5,))
		for row in cur.fetchall():
			print(f"\t{row[1]}")
		while True:
			new_label = input("label: ")
			if new_label:
				conn.execute("INSERT INTO md5_label VALUES(?,?)", (md5, new_label))
			else:
				break

if __name__ == "__main__":
	logging.basicConfig(level=logging.DEBUG)
	main()
