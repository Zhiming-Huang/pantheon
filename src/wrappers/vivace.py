#!/usr/bin/env python

from subprocess import check_call

import arg_parser
import context
from helpers import kernel_ctl



def main():
    args = arg_parser.receiver_first()

    if args.option == 'deps':
        print 'iperf'
        return


    if args.option == 'receiver':
        cmd = ['iperf', '-Z', 'pcc', '-s', '-p', args.port]
        check_call(cmd)
        return

    if args.option == 'sender':
        cmd = ['iperf', '-Z', 'pcc', '-c', args.ip, '-p', args.port,
               '-t', '75']
        check_call(cmd)
        return


if __name__ == '__main__':
    main()
