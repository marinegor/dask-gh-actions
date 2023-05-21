from utils import main
import argparse
import multiprocessing

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-r", "--radius", type=int, default=3, help="Fingerprint radius"
    )
    parser.add_argument(
        "-b", "--nbits", type=int, default=10, help="Number of bits in fingerprint"
    )
    parser.add_argument(
        "-n",
        "--nproc",
        type=int,
        default=multiprocessing.cpu_count(),
        help="Number of CPUs to parallelize across",
    )
    parser.add_argument(
        "--no-dask", action="store_true", help="Ignore dask parallelization"
    )
    parser.add_argument(
        "-o", "--output", type=str, default="fingerprints", help="Output file prefix"
    )
    parser.add_argument("input", type=str, help="Input file from Enamine")

    args = parser.parse_args()
    main(
        input=args.input,
        n_bits=args.nbits,
        radius=args.radius,
        nproc=args.nproc,
        output=args.output,
    )
