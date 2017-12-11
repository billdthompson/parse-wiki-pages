# coding: utf-8

# Author:
# -----------
# Copyright (C) 2017 Bill Thompson (biltho@mpi.nl) 
# 
#
# Description:
# -----------
# Parses a Wikimedia sql dump of the page table (e.g. avwiki-latest-page.sql.gz) for a given wiki.
# Dumps hosted at e.g. "https://dumps.wikimedia.org/{0}wiki/latest/{0}wiki-latest-page.sql.gz".format(language_iso)
#
#
# Usage: 
# -----------
# python main.py -f avwiki-latest-page.sql.gz
# 
#
# Returns:
# -----------
# Writes out a csv with (page_id, target_language, paget_title) columns
#
# Notes:
# -----------
# Here at the fields in the page records:
#
# COLUMNS = ["page_id", "page_namespace", "page_title", "page_restrictions", "page_counter", 
#           "page_is_redirect", "page_is_new", "page_random", "page_touched", "page_links_updated",
#           "page_latest", "page_len", "page_no_title_convert", "page_content_model", "page_lang"]
# 
# This script extracts "page_id", "page_namespace", "page_title", and "page_len", but could easily be adapted to extract any field
# by adding to the indexing in lines 61 - 66
#

import argparse
import gzip
import pandas as pd

from time import strftime
TIMESTAMP = strftime("%Y-%m-%d__%H-%M-%S")

import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def parse(filename):
    logging.info("Pre-processing > Attempting parse on: {0}".format(filename))

    page_ids, page_namespaces, page_titles, page_lengths = [], [], [], []

    logging.info("Pre-processing > Unzipping: {0}".format(filename))
    with gzip.open(filename, 'r') as f:
        logging.info("Pre-processing > Unzip Success")

        logging.info("Parser > Looping over file")
        for line in f:

            if line.startswith('INSERT INTO `page` VALUES'):

                entries = line[26:].split('),(')

                for entry in entries:
                    fields = entry.strip('(').strip(')').split(',')
                    page_ids.append(fields[0])
                    page_namespaces.append(fields[1])
                    page_titles.append(fields[2])
                    page_lengths.append(fields[11])

    logging.info("Parser > Parse Complete")

    new_filename = '-'.join([filename.strip('.sql.gz'), 'parsed.csv'])

    logging.info("Post-processing > Writing dataframe out to: {0}".format(new_filename))

    results = pd.DataFrame(dict(page_id = page_ids, page_namespace = page_namespaces, page_title = page_titles, page_length = page_lengths))

    results.to_csv(new_filename, index = False, encoding = 'utf-8')

    logging.info("JOB COMPLETE.")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Parse a Wikimedia page dump into a csv of ("page_id", "page_namespace", "page_title", and "page_len") quadruplets.')
    parser.add_argument('-f', '--filename')
    args = parser.parse_args()
    parse(args.filename)