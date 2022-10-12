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


@click.group()
def cli():

    """
    Log CLI
    """

    pass


@click.command(name="bookmark")
@click.option(
    "--url", prompt="Bookmark URL", help="URL of a bookmark including http(s)"
)
@click.option(
    "--title", prompt="Bookmark/Entry Title", help="Title of log entry for bookmark"
)
@click.option("--archive", is_flag=True, help="Take a single page snapshot the URL")
@click.option(
    "--summary", prompt="Summary of bookmark", help="Description/summary of bookmark"
)
def bookmark(url, title, archive, summary):

    """
    Add a bookmark entry
    """

    # Bookmark Flow
    # =============
    # Ask for:
    # - Entry Title
    # - URL
    # - Archive URL?
    # - Screenshot or SingleFile
    # - Instruct archive.is to run against URL
    # - Summary/Description
    # - Manual
    # - HTML Head Description (Ask if ok to use)
    # - Tags?

    url = url
    title = title
    summary = summary
    print(url)
    print(title)
    print(summary)


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

    docs_root = os.environ.get("DOCS_ROOT")
    log_entry_path = f"{docs_root}/log/content/{entry_id}.md"

    with open(log_entry_path, "w") as todo_file:
        todo_file.write(frontmatter)

        print(f"Entry saved to: {log_entry_path}")

    if edit == True:

        default_editor = os.environ.get("EDITOR")
        subprocess.run([default_editor, log_entry_path])


# Commands:
cli.add_command(bookmark)
cli.add_command(todo)

# Call the CLI:
cli()
