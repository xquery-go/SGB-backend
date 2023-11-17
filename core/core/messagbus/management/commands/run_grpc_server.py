# -*- coding: utf-8 -*-
import re

from django.core.management.base import BaseCommand
from django.utils.regex_helper import _lazy_re_compile

naiveip_re = _lazy_re_compile(r"""^(?:
(?P<ipv6>\[[a-fA-F0-9:]+\])
:)?(?P<port>\d+)$""", re.X)


class Command(BaseCommand):
    help = 'Starts a gRPC server.'

    # Validation is called explicitly each time the server is reloaded.
    # requires_system_checks = False
    default_addr = '[::]'
    default_port = '50051'

    def add_arguments(self, parser):
        parser.add_argument(
            'address', type=str,
        )
        parser.add_argument(
            '--max-workers', type=int, default=10, dest='max_workers',
            help='Number of maximum worker threads.'
        )

    def handle(self, *args, **options):
        print(f"Starting gRPC server at {options['address']}")


