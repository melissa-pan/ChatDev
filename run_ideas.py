#!/usr/bin/env python3

import json
import subprocess

def main():
    # Load the data from ideas.json
    with open('project_ideas_v2.json', 'r') as f:
        ideas = json.load(f)

    # Iterate over each idea, building and running the command
    for item in ideas:
        project_name = item['project_name']
        description = item['description']

        command = [
            "python3",
            "run.py",
            "--task", description,
            "--name", project_name,
            "--model", "GPT_4O"
        ]
        
        print(f"Running: {' '.join(command)}")
        subprocess.run(command, check=True)

if __name__ == "__main__":
    main()
