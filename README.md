# Project Taskmaster

A "simple" task/todo list.

## Overview

The overarching idea/plan is to build a simple ToDo manager using Django,
then extend it with extra features, then ultimately use this as a
"portfolio" application.

The project will be built starting from a plain vanilla install of Django,
no cookie-cutter starting point.  The web UI will initially be very
simple, nothing fancy with improvements made later.  Each step should be
built on a branch and then merged into the production branch via PR.


## Target Features and Ideas

- Simple Web based UI
- Simple REST API
- Notifications via email/webhook/etc
- RSS syndication of task lists (todo and done)
- Task Prioritization
- Task Categorization
- Tags
- Individual User Accounts


## Initial Roadmap

- MVP

  Requirements for MVP are:

    - User Accounts (built into Django)
    - Tasks/To-Dos
    - Simple REST API for managing tasks

- Phase 2

  Notifications

    - Simple email notifications
    - Simple webhook notifications
      Notifications for new/deleted/done
    - RSS syndication for todos
    - RSS syndication for done task

- Phase 3 (TBD)

  Categorization

    - Determine tags or categories
      Spike to determine if tags are food enough or if we need actual categories

- Phase 4 (TBD)

  ...
