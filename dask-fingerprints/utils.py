from dask.array.core import Array as dask_array
import dask.array as da
from dask import delayed
from time import sleep
from os import getpid


def simulate_trajectory(
    positions: list[float], scale: float = 0.1, length: int = 1_000_000
) -> dask_array:
    return da.random.normal(
        positions, scale=positions * scale, size=(length, len(positions))
    )


def rmsf(traj: dask_array) -> float:
    ref = traj[0]
    return ((traj - ref) ** 2).mean(axis=0).compute()


def rmsd(traj: dask_array) -> dask_array:
    ref = traj[0]
    return da.sqrt(((traj - ref) ** 2).mean(axis=1)).compute()


@delayed
def worker_pid(sleep_time: float = 1e-6):
    sleep(sleep_time)
    return getpid()
