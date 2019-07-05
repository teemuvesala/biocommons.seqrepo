#!/usr/bin/env python3
import psycopg2
from biocommons.seqrepo import SeqRepo
import psycopg2.extras

conn = psycopg2.connect(dbname="dumptest", user="testuser", password="q1w2e3r4a", host="localhost", cursor_factory=psycopg2.extras.DictCursor)
sr = SeqRepo('/usr/local/share/seqrepo/2019-06-20', db=conn, sqlparam="%s")

print("IIIIIIIK "+ str(sr.fetch('NM_001285399.2', 326, 327)))

