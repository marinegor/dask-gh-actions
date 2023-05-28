from utils import simulate_trajectory, rmsf, rmsd, worker_pid
import pytest
from os import getpid
from dask.distributed import Client
import multiprocessing


@pytest.fixture
def trajectory_single_frame():
    return simulate_trajectory([1, 2, 3], length=1)


@pytest.fixture
def trajectory_many_frames():
    return simulate_trajectory([1, 2, 3], length=10_000)


@pytest.mark.parametrize("scheduler", ["distributed", "processes"], indirect=True)
def test_worker_pid_is_not_the_same(scheduler):
    current_pid = getpid()
    work_pid = worker_pid().compute()
    assert current_pid != work_pid, scheduler


@pytest.mark.parametrize("scheduler", ["synchronous"], indirect=True)
def test_pids_are_same_if_use_threads(scheduler):
    current_pid = getpid()
    work_pid = worker_pid().compute()

    assert current_pid == work_pid, (current_pid, work_pid)
