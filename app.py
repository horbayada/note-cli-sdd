#!/usr/bin/env python3
import argparse
import json
import os
import sys

NOTES_FILE = os.path.expanduser("~/.notes.json")


def load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r") as f:
        return json.load(f)


def save_notes(notes):
    with open(NOTES_FILE, "w") as f:
        json.dump(notes, f, indent=2)


def add_note(content):
    content = content.strip()
    if not content:
        print("Error: Note content cannot be empty.", file=sys.stderr)
        sys.exit(1)
    notes = load_notes()
    new_id = (max(n["id"] for n in notes) + 1) if notes else 1
    note = {"id": new_id, "content": content}
    notes.append(note)
    save_notes(notes)
    print(f"Note added with ID {new_id}.")


def list_notes():
    notes = load_notes()
    if not notes:
        print("No notes found.")
        return
    for note in notes:
        print(f"[{note['id']}] {note['content']}")


def delete_note(note_id):
    notes = load_notes()
    matching = [n for n in notes if n["id"] == note_id]
    if not matching:
        print(f"Error: No note found with ID {note_id}.", file=sys.stderr)
        sys.exit(1)
    updated = [n for n in notes if n["id"] != note_id]
    save_notes(updated)
    print(f"Note {note_id} deleted.")


def main():
    parser = argparse.ArgumentParser(description="CLI Note-Taking App")
    subparsers = parser.add_subparsers(dest="command")

    add_parser = subparsers.add_parser("add", help="Add a new note")
    add_parser.add_argument("content", help="The content of the note")

    subparsers.add_parser("list", help="List all notes")

    delete_parser = subparsers.add_parser("delete", help="Delete a note by ID")
    delete_parser.add_argument("id", type=int, help="The ID of the note to delete")

    args = parser.parse_args()

    if args.command == "add":
        add_note(args.content)
    elif args.command == "list":
        list_notes()
    elif args.command == "delete":
        delete_note(args.id)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()