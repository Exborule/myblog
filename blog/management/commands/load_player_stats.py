import csv
from django.core.management.base import BaseCommand
from blog.models import PlayerStat
import os

class Command(BaseCommand):
    help = 'Load NHL player stats from CSV into the database'

    def handle(self, *args, **kwargs):
        # Clear existing PlayerStat data
        PlayerStat.objects.all().delete()

        # Path to the CSV file
        csv_file_path = os.path.join(
            os.path.dirname(__file__),  # Directory of this file
            '../../../nhl_player_stats.csv'  # Path to CSV file relative to the current file
        )

        csv_file_path = os.path.abspath(csv_file_path)

        # Open the CSV file and read the data
        with open(csv_file_path, 'r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)

            # Print header to debug
            headers = reader.fieldnames
            self.stdout.write(self.style.SUCCESS(f'CSV Headers: {headers}'))

            for row in reader:
                # Extract data from each row
                player = row['player']
                age = int(row['age']) if row['age'] else None
                team = row['team']
                position = row['position']
                games_played = int(row['gp']) if row['gp'] else None
                goals = int(row['g']) if row['g'] else None
                assists = int(row['a']) if row['a'] else None
                points = int(row['pts']) if row['pts'] else None
                plus_minus = int(row['+/-']) if row['+/-'] else None
                penalty_minutes = int(row['pim'].strip().replace(',', '')) if row['pim'] else None
                even_goals = int(row['evg']) if row['evg'] else None
                power_play_goals = int(row['ppg']) if row['ppg'] else None
                short_hand_goals = int(row['shg']) if row['shg'] else None
                game_winning_goals = int(row['gwg']) if row['gwg'] else None
                even_strength = int(row['ev']) if row['ev'] else None
                power_play = int(row['pp']) if row['pp'] else None
                short_hand = int(row['sh']) if row['sh'] else None
                shots_on_goal = int(row['sog']) if row['sog'] else None
                shooting_percentage = float(row['spct']) if row['spct'] else None
                total_shots_attempted = int(row['tsa']) if row['tsa'] else None
                time_on_ice = convert_time_to_minutes(row['toi'])
                average_time_on_ice = convert_time_to_minutes(row['atoi'])
                faceoff_wins = int(row['fow']) if row['fow'] else None
                faceoff_losses = int(row['fol']) if row['fol'] else None
                faceoff_percentage = float(row['fo_percent']) if row['fo_percent'] else None
                blocked_shots = int(row['bl']) if row['bl'] else None
                hits = int(row['hit']) if row['hit'] else None
                takeaways = int(row['take']) if row['take'] else None
                giveaways = int(row['give']) if row['give'] else None

                # Create PlayerStat instances
                PlayerStat.objects.create(
                    player=player,
                    age=age,
                    team=team,
                    position=position,
                    games_played=games_played,
                    goals=goals,
                    assists=assists,
                    points=points,
                    plus_minus=plus_minus,
                    penalty_minutes=penalty_minutes,
                    even_goals=even_goals,
                    power_play_goals=power_play_goals,
                    short_hand_goals=short_hand_goals,
                    game_winning_goals=game_winning_goals,
                    even_strength=even_strength,
                    power_play=power_play,
                    short_hand=short_hand,
                    shots_on_goal=shots_on_goal,
                    shooting_percentage=shooting_percentage,
                    total_shots_attempted=total_shots_attempted,
                    time_on_ice=time_on_ice,
                    average_time_on_ice=average_time_on_ice,
                    faceoff_wins=faceoff_wins,
                    faceoff_losses=faceoff_losses,
                    faceoff_percentage=faceoff_percentage,
                    blocked_shots=blocked_shots,
                    hits=hits,
                    takeaways=takeaways,
                    giveaways=giveaways
                )

        self.stdout.write(self.style.SUCCESS('Successfully loaded player stats from CSV'))

    def to_int(self, value):
        try:
            return int(value.strip().replace(',', '')) if value else None
        except ValueError:
            return None

    def to_float(self, value):
        try:
            return float(value.strip().replace(',', '')) if value else None
        except ValueError:
            return None

    def parse_time(self, value):
        """Parse time in 'MM:SS' format and convert to total seconds."""
        if value:
            try:
                minutes, seconds = value.strip().split(':')
                return int(minutes) * 60 + int(seconds)
            except ValueError:
                return None
        return None
    
def convert_time_to_minutes(time_str):
    if time_str:
        try:
            # Handle cases where the time format might be incorrect or have extra spaces
            time_str = time_str.strip()
            parts = time_str.split(':')
            if len(parts) == 2:
                minutes, seconds = parts
                return int(minutes) + int(seconds) / 60
            else:
                # If the format isn't correct, return None or handle as needed
                return None
        except ValueError:
            # If conversion to int fails, return None
            return None
    return None

