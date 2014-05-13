#! /usr/bin/env python
#
# This file is part of khmer, http://github.com/ged-lab/khmer/, and is
# Copyright (C) Michigan State University, 2009-2014. It is licensed under
# the three-clause BSD license; see doc/LICENSE.txt.
# Contact: khmer-project@idyll.org
#
import sys
import screed

N_count = 0
for n, record in enumerate(screed.open(sys.argv[1])):
    if n % 10000 == 0:
        print>>sys.stderr, '...', n

    sequence = record['sequence']
    name = record['name']

    if 'N' in sequence:
        N_count += 1
        continue

    print ">" + name
    print sequence

print>>sys.stderr, str(N_count) + " lines were dropped for 'N's in sequences."
