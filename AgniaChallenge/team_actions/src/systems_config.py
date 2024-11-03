from typing import Dict, Any

from team_actions.src.registration import fetch_available_actions


systems_info: Dict[str, Any] = {
    "task_tracker": {
        "description": "Manages tasks, issues, and projects (e.g., Todoist, TeamFlame, Kaiten).",
        "systems": {
            "TeamFlame": "TeamFlame is a task tracking system where spaces hold projects, projects contain Kanban boards, and boards manage tasks across columns like 'To Do', 'In Progress' and 'Done'. Tasks have statuses such as epic, bug, etc., ensuring efficient organization and workflow control.",
            "Todoist": "Todoist is a task management app that organizes tasks into projects, allows setting due dates, priorities, and creating sub-tasks. It supports collaboration, custom filters, reminders, and tracks productivity across devices.",
            "Kaiten": "Kaiten is a task management app that organizes tasks (cards) into projects (boards) and spaces. It allows to organise tasks by custom statuses.",
        },
    },
    "version_control_system": {
        "description": "Tracks code changes, versions, and issues (e.g., GitHub, GitFlame).",
        "systems": {
            "GitFlame": "GitFlame is a version control and collaboration tool that integrates Git repositories with task management.",
        },
    
    },
    "time_tracker": {
        "description" : "A rool for time-management, productivity and team work",
        "systems": {
            "Clockify" : "Clockify is a time tracking service designed to help organizations track employee productivity, view their attendance and billable hours."
        }
    }
}

available_actions: Dict[str, Any] = fetch_available_actions()
