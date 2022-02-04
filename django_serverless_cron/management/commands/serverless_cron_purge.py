from django.core.management import BaseCommand
from django_serverless_cron.models import JobRun


class Command(BaseCommand):
    help = "Deletes old jobs from the Database"

    def add_arguments(self, parser):
        parser.add_argument('-n', type=int, help='Number of jobs to remove from the least recent to the most recent')

    def handle(self, *args, **kwargs):
        try:
            n = kwargs['n']
            jobs = JobRun.objects.all().order_by('time_attempted_running')[:n]
            jobs.delete()
            self.stdout.write(self.style.SUCCESS(f'Successfully purged the last {n} old jobs'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(e))
