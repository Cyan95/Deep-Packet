from pathlib import Path

import click
from joblib import Parallel, delayed
from scapy.all import *
from config import *

from utils import should_omit_packet, read_pcap, PREFIX_TO_APP_ID, PREFIX_TO_TRAFFIC_ID


def transform_pcap(path, output_path: Path = None):
    if Path(output_path.name + ".pcap").exists():
        print(output_path, 'Done')
        return

    print('transform', path.name)
    pkt = read_pcap(path)
    wrpcap(output_path.name + ".pcap", pkt)
    print(output_path, 'Done')


@click.command()
@click.option('-s', '--source', default=pcapng_path, help='path to the directory containing raw pcap files',
              required=False)
@click.option('-t', '--target', default=pcap_path, help='path to the directory for persisting preprocessed files',
              required=False)
@click.option('-n', '--njob', default=-1, help='num of executors', type=int)
def main(source, target, njob):
    data_dir_path = Path(source)
    target_dir_path = Path(target)
    target_dir_path.mkdir(parents=True, exist_ok=True)
    Parallel(n_jobs=njob)(
        delayed(transform_pcap)(pcapng_path, target_dir_path / (pcapng_path.name + '.pcap')) for pcapng_path in
        sorted(data_dir_path.iterdir()))


if __name__ == '__main__':
    main()
