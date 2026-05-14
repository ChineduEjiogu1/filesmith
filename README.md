# FileSmith

FileSmith is a vanilla Python file generation engine for creating images and reports from one shared source of truth.

## Phase 1 Goal

Generate a checkerboard project and export it as:

- PPM image
- TXT report

## Project Idea

FileSmith follows a simple pipeline:

```text
Project data
↓
Image generator
↓
Report generator
↓
Exporters
↓
Generated files