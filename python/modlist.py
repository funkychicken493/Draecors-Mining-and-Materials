# Creates a list of all mods in a markdown file, pulling from profile.json.

import json

# Define the output
markdown = ''

# Open profile.json
with open('profile.json', encoding='utf-8', errors='ignore') as f:
    profile = json.load(f)
    projects = profile['projects']
    print(f'Found {len(projects)} projects in profile.json')
    # Ensure that the metadata contains the project key
    for project in projects.copy():
        if 'project' not in projects[project]['metadata']:
            print(f'Project {project} does not contain project key in metadata, skipping...')
            projects.pop(project)
    # Sort projects by title
    projects = dict(sorted(projects.items(), key=lambda x: x[1]['metadata']['project']['title']))
    for project in projects:
        title = projects[project]['metadata']['project']['title']
        # Replace '[' and ']' with '\[' and '\]' respectively
        title = title.replace('[', '\[')
        title = title.replace(']', '\]')
        slug = projects[project]['metadata']['project']['slug']
        print(f'Adding {title} ({slug}) to list...')
        markdown += f'- [{title}](https://www.modrinth.com/mod/{slug})\n'

# Write to file
with open('modlist.md', 'w', encoding='utf-8', errors='ignore') as f:
    f.write(markdown)
        