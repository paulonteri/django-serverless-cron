from django.core.management import BaseCommand

from django_serverless_cron.services import purge_jobs


class Command(BaseCommand):
    help = "Deletes old jobs from the Database"

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='Number of jobs to remove from the least recent')

    def handle(self, *args, **kwargs):
        try:
            n = kwargs['n']
            purge_jobs(int(n))
            self.stdout.write(self.style.SUCCESS(f'Successfully purged the last {n} old jobs'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(e))
