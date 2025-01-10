#!/usr/bin/env python3

import sys
import os

def trim_trailing_spaces(filename):
    """Trim trailing spaces (but not tabs) from each line in the file."""
    # Read all lines
    with open(filename, 'r', encoding='utf-8') as f:
        original_lines = f.readlines()

    new_lines = []
    changes_detected = False

    for idx, line in enumerate(original_lines):
        # We want to keep the newline if it exists, so let's handle that carefully
        has_newline = line.endswith('\n')
        
        # Separate out the newline for easy trailing-space trimming
        if has_newline:
            line_without_newline = line[:-1]
        else:
            line_without_newline = line

        # Remove only trailing spaces
        trimmed_line = line_without_newline.rstrip(' ')

        # Re-append newline if it was originally present
        if has_newline:
            trimmed_line += '\n'

        new_lines.append(trimmed_line)

        # Check if a change was made
        if trimmed_line != line:
            changes_detected = True
            print(f"Line {idx + 1} changed:")
            print(f"  Original: {repr(line)}")
            print(f"  New:      {repr(trimmed_line)}")

    # Overwrite original file if at least one change was detected
    if changes_detected:
        with open(filename, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
    else:
        print("No trailing spaces found. No changes made.")

def main():
    if len(sys.argv) < 2:
        print("Usage: python trim_trailing_spaces.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    if not os.path.isfile(filename):
        print(f"Error: '{filename}' is not a valid file.")
        sys.exit(1)

    trim_trailing_spaces(filename)

if __name__ == "__main__":
    main()
