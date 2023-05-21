from utils import simulate_trajectory, rmsf, rmsd, worker_pid
import pytest
from os import getpid
from dask.distributed import Client
import multiprocessing


@pytest.fixture
def trajectory_single_frame():
    return simulate_trajectory([1, 2, 3], length=1)


@pytest.fixture
def trajectory_many_frames(client):
    return simulate_trajectory([1, 2, 3], length=10_000)


# @pytest.fixture
# def dask_client_with_maximum_workers_as_threads():
# from dask.distributed import Client
# import multiprocessing
#
# client = Client(n_workers=multiprocessing.cpu_count(), processes=False)
# return client


def test_worker_pid_is_not_the_same():
    from dask.distributed import Client

    _ = Client(n_workers=1)
    current_pid = getpid()
    work_pid = worker_pid().compute()

    assert current_pid != work_pid, (current_pid, work_pid)


def test_pids_are_same_if_use_threads():
    from dask.distributed import Client

    _ = Client(n_workers=1, processes=False)
    current_pid = getpid()
    work_pid = worker_pid().compute()

    assert current_pid == work_pid, (current_pid, work_pid)


def test_number_of_pids_equals_number_of_workers():
    from dask.distributed import Client

    ncpu = multiprocessing.cpu_count()
    _ = Client(n_workers=ncpu)
    current_pid = getpid()
    worker_pids = [worker_pid().compute() for _ in range(50)]
    worker_pids = set(worker_pids)

    assert current_pid not in worker_pids, (current_pid, worker_pids)
    assert len(worker_pids) == ncpu, (worker_pids, ncpu)
