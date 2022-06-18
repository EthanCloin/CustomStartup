# CustomStartup
Python utility to define sets of apps and websites to upon on startup.

## Libraries Utilized
- os
- webbrowser
- dotenv
- argparse
- dataclasses
- logging

## Usage
Run `main.py` with optional arguments to dictate which startup type to execute. Currently, I have defined two types "Default" and "Work". 
View the help message by running `main.py` with  `--help` or `-h` flag.

## Development Challenges
The greatest challenge for this initial version of CustomStartup was finding how to open sites in Chrome under different Profiles.

## Potential Features/Improvements
- Format into a Python Package which could be installed by `pip`
- Implement `asyncio` to open apps/sites one after the other instead of all at once. This may not be the right strategy, but the goal is to reduce the chaotic spam of apps opening.
- Accept new StartupTypes from json files that users define and either add to the project or supply as an argument. 
