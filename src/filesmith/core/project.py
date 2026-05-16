'''
This file defines the Project object used to track one FileSmith generation run.

A Project stores:
- title
- description
- image
- created date/time
- generated file names
'''

from datetime import datetime

class Project:
    def __init__(self, title="Untitled Project", description="", notes =""):
        self.title = title
        self.description = description
        self.image = None
        self.created_at = datetime.now()
        self.generated_files = []

    
    def set_image(self, image):
        self.image = image

    def add_export_path(self, filepath):
        if filepath and filepath not in self.generated_files:
            self.generated_files.append(filepath)
        elif not filepath:
            print(f"Warning: Attempted to add an empty file path to project tracking.")