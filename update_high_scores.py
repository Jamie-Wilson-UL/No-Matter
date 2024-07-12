import json
import os
import requests
from datetime import datetime

# Fetch the current high scores from the GitHub repository
response = requests.get('https://raw.githubusercontent.com/Jamie-Wilson-UL/No-Matter/main/high_score.json')
high_scores = response.json()

# The new score to be added, replace with actual data
new_score = {"name": os.getenv('PLAYER_NAME'), "score": int(os.getenv('PLAYER_SCORE'))}

# Update the high scores list
high_scores.append(new_score)
high_scores = sorted(high_scores, key=lambda x: x['score'], reverse=True)[:3]

# Write the updated high scores back to the JSON file
with open('high_score.json', 'w') as file:
    json.dump(high_scores, file, indent=4)

# Commit and push the changes back to the repository
os.system('git config --global user.email "github-actions[bot]@users.noreply.github.com"')
os.system('git config --global user.name "github-actions[bot]"')
os.system('git add high_score.json')
os.system('git commit -m "Update high scores: {}"'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
os.system('git push')