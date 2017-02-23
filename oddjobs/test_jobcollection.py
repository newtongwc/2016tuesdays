from Job import Job
from jobCollection import JobCollection

import pytest


def test_empty_collection():
    collection = JobCollection()
    jobs = JobCollection.get_jobs()
    assert len(jobs) == 0

def test_add_job():
    a = Job("Dusting my Chihuahuas", "Bart", "from midnight till dawn", "central park's blood stone")
    JobCollection.add_job(a)
    assert len(JobCollection) == 1
    assert a in JobCollection

    a_copy = Job("Dusting my Chihuahuas", "Bart", "from midnight till dawn", "central park's blood stone")
    assert a_copy in JobCollection

    b = Job("Doing math homework", "Daisy", "6-8 on weekdays", "Gatsby's house")
    JobCollection.add_job(b)
    assert len(JobCollection) == 2
    assert b in JobCollection

    JobCollection.add_job(a_copy)
    assert len(JobCollection) == 2
