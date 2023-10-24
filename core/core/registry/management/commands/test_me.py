# -*- coding: utf-8 -*-
import errno
import os
import re
import sys
from datetime import datetime

from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.utils import autoreload
from django.utils.regex_helper import _lazy_re_compile

naiveip_re = _lazy_re_compile(r"""^(?:
(?P<ipv6>\[[a-fA-F0-9:]+\])
:)?(?P<port>\d+)$""", re.X)


class Command(BaseCommand):
    help = 'Starts a gRPC server.'

    # Validation is called explicitly each time the server is reloaded.
    requires_system_checks = False
    default_addr = '[::]'
    default_port = '50051'

    def add_arguments(self, parser):
        parser.add_argument(
            'address', nargs='?',
            help='Optional address for which to open a port.'
        )
        parser.add_argument(
            '--max-workers', type=int, default=10, dest='max_workers',
            help='Number of maximum worker threads.'
        )
        parser.add_argument(
            '--prod', action='store_true', dest='production_mode',
            help=(
                'Run the server in development mode. This tells Django to use '
                'the auto-reloader and run checks.'
            )
        )

    def handle(self, *args, **options):

        print('Starting server')

        # if not options['address']:
        #     self.address, self.port = self.default_addr, self.default_port
        # else:
        #     m = re.match(naiveip_re, options['address'])
        #     if m is None:
        #         raise CommandError(
        #             '"%s" is not a valid port number or address:port pair.' % options['address']
        #         )
        #     self.address, self.port = m.groups()
        # self.run(**options)

