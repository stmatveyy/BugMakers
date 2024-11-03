from team_actions.src.utils.action_router import ActionRouter

# Import actions module for new system here
from team_actions.src.actions.Todoist import actions as todoist_actions
from team_actions.src.actions.Kaiten import actions as kaiten_actions
from team_actions.src.actions.LAMA import actions as LLAMA_actions
from team_actions.src.actions.Clockify import actions as Clockify_actions

# Add your module to the router
ActionRouter.add_actions_for_module(todoist_actions)
ActionRouter.add_actions_for_module(kaiten_actions)
ActionRouter.add_actions_for_module(LLAMA_actions)
ActionRouter.add_actions_for_module(Clockify_actions)

# Keep it as is
action_router = ActionRouter()
