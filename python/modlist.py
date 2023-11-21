# Creates a list of all mods in a markdown file, pulling from profile.json.

import json

# Define the output
markdown = ''

# Open profile.json
with open('profile.json', encoding='utf-8', errors='ignore') as f:
    profile = json.load(f)
    projects = profile['projects']
    # Sort projects by title
    projects = {k: v for k, v in sorted(projects.items(), key=lambda item: item[1]['metadata']['project']['title'])}
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
        