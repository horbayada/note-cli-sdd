# Specification

## Overview
This project is a single-user CLI note-taking application that runs locally in the terminal.

## Functional Requirements
- User must be able to add a note
- User must be able to list all the notes
- User must be able to delete a note by ID
- Notes must be listed with their ID clearly visible.

## Non-Functional Requirements
- The program must run in the terminal environment
- The system must handle invalid input gracefully.

## Data Model

A note contains:
- id (integer, auto-generated)
- content (string)

## Edge Cases
-Adding an empty note must not be allowed.
