pagerduty_service_configs = [
  {
    name                   = "Default alert policy"
    escalation_policy_name = "Default alert"
  }
]

action_groups = [
  {
    name       = "default-action-group" # System_namespace prefix is added to this field.
    short_name = "dag"

    email_receiver = [] # Required field -  Use [] as default

    webhook_receiver = [] # Required field -  Use [] as default

    pagerduty_service_name = "Default alert policy"

  }
]
