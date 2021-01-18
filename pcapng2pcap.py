from pathlib import Path

import click
from joblib import Parallel, delayed
from scapy.all import *
from config import *
from utils import read_pcap


def transform_pcap(path, output_path: Path = None):
    if Path(str(output_path.absolute())).exists():
        print(output_path, 'Done')
        return

    pkt = read_pcap(path)
    wrpcap(str(output_path) + ".pcap", pkt)


@click.command()
@click.option('-s', '--source', default=pcapng_path, help='path to the directory containing pcapng files',
              required=False)
@click.option('-f', '--target', default=pcap_path, help='path to the directory to save pcap files',
              required=False)
@click.option('-n', '--njob', default=-1, help='num of executors', type=int)
def main(source, target, njob):
    data_dir_path = Path(source)
    target_dir_path = Path(target)
    target_dir_path.mkdir(parents=True, exist_ok=True)
    Parallel(n_jobs=njob)(
        delayed(transform_pcap)(pcapng_path, target_dir_path / pcapng_path.name[:-7]) for pcapng_path in
        sorted(data_dir_path.iterdir()))


if __name__ == '__main__':
    main()
