#!/usr/bin/env python

from git import Repo
from dateutil.parser import isoparse
import datetime


def scan_commits(start_date, committer_name):
    repo = Repo("./")
    commits = repo.iter_commits()
    end_date = datetime.datetime.now().timestamp()
    date_range = end_date - start_date.timestamp()

    # filter between dates
    committs = repo.iter_commits()
    final_result = [i
                    for i in committs
                    if i.committed_date <= end_date and i.committed_date >= start_date.timestamp()
                    ]

    if committer_name:
        final_result = [i
                        for i in final_result
                        if i.committer.name.startswith(committer_name)
                        ]
    for i in final_result:
        print(datetime.datetime.fromtimestamp(i.committed_date), ' -- ' , i.message)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("start_date", help="Collect committs starting with this date")
    parser.add_argument("committer_name", help="Select committs done by this committer")
    args = parser.parse_args()
    scan_commits(isoparse(args.start_date)
                            , args.committer_name)








