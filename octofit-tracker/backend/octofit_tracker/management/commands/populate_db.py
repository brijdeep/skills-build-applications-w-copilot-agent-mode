from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create users
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel)
        captain = User.objects.create(name='Captain America', email='cap@marvel.com', team=marvel)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc)

        # Create activities
        Activity.objects.create(user=ironman, type='Running', duration=30, date='2025-11-01')
        Activity.objects.create(user=captain, type='Cycling', duration=45, date='2025-11-02')
        Activity.objects.create(user=superman, type='Swimming', duration=60, date='2025-11-03')
        Activity.objects.create(user=batman, type='Yoga', duration=20, date='2025-11-04')

        # Create workouts
        workout1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes.')
        workout2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility.')
        workout1.suggested_for.set([ironman, captain, superman])
        workout2.suggested_for.set([batman])

        # Create leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=90)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
