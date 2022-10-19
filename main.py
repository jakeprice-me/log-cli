#!/usr/bin/python3

import click
import datetime
import re
import uuid
import os
import subprocess

# Get current date/time:
date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Remove all non-numeric characters from date/time to create a unique note id:
entry_id = str(date_time).replace(":", "").replace(" ", "").replace("-", "")

# Generate UUID:
uuid = uuid.uuid4()

# Document directory root:
docs_root = os.environ.get("DOCS_ROOT")

# Log entry path:
log_entry_path = f"{docs_root}/log/content/{entry_id}.md"
attachments_path = f"{docs_root}/log/static/attachments"


@click.group()
def cli():

    """
    Log CLI
    """

    pass


# ==== Bookmark ===============================================================


@click.command(name="bookmark")
@click.option(
    "--link",
    prompt="Bookmark URL",
    help="Bookmark URL",
    required=True,
)
@click.option("--title", prompt="Title", help="Title of the entry", required=True)
@click.option(
    "--pinned",
    prompt="Pin Entry?",
    help="Whether to pin the entry",
    type=click.Choice(["false", "true"]),
    default="false",
    required=True,
)
@click.option(
    "--tags", prompt="Tags", help="List of tags, separated by a comma", default=""
)
@click.option(
    "--summary",
    prompt="Summary",
    help="Description/summary of bookmark with more detail",
    default="",
)
@click.option(
    "--edit",
    prompt="Edit in Default Editor?",
    help="Open the todo entry in the default text editor",
    is_flag=True,
    default=False,
)
def bookmark(link, title, pinned, tags, summary, edit):

    """
    Add a bookmark entry
    """

    frontmatter = f"""---
id: {entry_id}
uuid: {uuid}
title: {title}
date: {date_time}
modified: {date_time}
types: bookmark
link: {link}
pinned: {pinned}
tags: [{tags}]
private: true
---

{summary}

"""

    with open(log_entry_path, "w") as todo_file:
        todo_file.write(frontmatter)

        print(f"Entry saved to: {log_entry_path}")

    if edit == True:

        default_editor = os.environ.get("EDITOR")
        subprocess.run([default_editor, log_entry_path])


# ==== Attachments ============================================================


@click.command(name="attachments")
@click.option(
    "--filemanager",
    prompt="File manager",
    help="Open attachments directory in provided file manager",
    type=click.Choice(["nautilus", "open"]),
)
def attachments(filemanager):

    """
    Open attachments directory
    """

    if filemanager:

        subprocess.Popen([filemanager, attachments_path])
        print(f"Attachments directory: {attachments_path}")


# ==== New Entry ==============================================================


@click.command(name="new")
@click.option(
    "--edit",
    prompt="Edit in Default Editor?",
    help="Open the entry in the default text editor",
    is_flag=True,
    default=False,
)
def new(edit):
    """
    Add a new entry
    """

    frontmatter = f"""---
id: {entry_id}
uuid: {uuid}
title: 
date: {date_time}
modified: {date_time}
types: 
link: 
pinned: false
tags: []
private: true
---



"""

    with open(log_entry_path, "w") as log_file:
        log_file.write(frontmatter)

        print(f"Entry saved to: {log_entry_path}")

    if edit == True:

        default_editor = os.environ.get("EDITOR")
        subprocess.run([default_editor, log_entry_path])


# ==== New Tech Note ==========================================================


@click.command(name="tech-note")
@click.option(
    "--filename",
    prompt="Tech Note filename (without .md)",
    help="Filename for the tech note",
    required=True,
)
@click.option(
    "--edit",
    prompt="Edit in Default Editor?",
    help="Open the tech note in the default text editor",
    is_flag=True,
    default=False,
)
def tech_note(filename, edit):
    """
    Add a new tech note
    """

    tech_note_entry_path = f"{docs_root}/log/content/tech-notes/{filename}.md"

    frontmatter = f"""---
id: {entry_id}
uuid: {uuid}
title: 
date: {date_time}
modified: {date_time}
types: tech-note
link: 
pinned: false
tags: []
private: true
---



"""

    with open(tech_note_entry_path, "w") as log_file:
        log_file.write(frontmatter)

        print(f"Tech Note saved to: {tech_note_entry_path}")

    if edit == True:

        default_editor = os.environ.get("EDITOR")
        subprocess.run([default_editor, tech_note_entry_path])


# ==== Todo ===================================================================


@click.command(name="todo")
@click.option("--title", prompt="Title", help="Title of the todo entry", required=True)
@click.option(
    "--types",
    prompt="Type",
    help="Type of todo entry",
    type=click.Choice(["todo-p", "todo-1", "todo-2", "todo-3", "done"]),
    default="todo-3",
    required=True,
)
@click.option(
    "--link",
    prompt="Link",
    help="A link supporting the todo entry",
    default="",
    required=False,
)
@click.option(
    "--pinned",
    prompt="Pin Entry?",
    help="Whether to pin the todo entry",
    type=click.Choice(["false", "true"]),
    default="false",
    required=True,
)
@click.option(
    "--tags", prompt="Tags", help="List of tags, separated by a comma", default=""
)
@click.option(
    "--summary",
    prompt="Summary",
    help="Description/summary of todo with more detail",
    default="",
)
@click.option(
    "--edit",
    prompt="Edit in Default Editor?",
    help="Open the todo entry in the default text editor",
    is_flag=True,
    default=False,
)
def todo(title, types, link, pinned, tags, summary, edit):

    """
    Add a new todo entry
    """

    frontmatter = f"""---
id: {entry_id}
uuid: {uuid}
title: {title}
date: {date_time}
modified: {date_time}
types: {types}
link: {link}
pinned: {pinned}
tags: [{tags}]
private: true
---

{summary}

"""

    with open(log_entry_path, "w") as todo_file:
        todo_file.write(frontmatter)

        print(f"Entry saved to: {log_entry_path}")

    if edit == True:

        default_editor = os.environ.get("EDITOR")
        subprocess.run([default_editor, log_entry_path])


# Commands:
cli.add_command(attachments)
cli.add_command(bookmark)
cli.add_command(new)
cli.add_command(tech_note)
cli.add_command(todo)

# Call the CLI:
cli()
