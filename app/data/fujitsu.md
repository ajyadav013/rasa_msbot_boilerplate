##i am fine sotry
* _greet
    - action_utter_greet
* _affirm
    - utter_affirm

## Invalid Text
* _invalid
    - utter_invalid

## Anonymous Text
* _anonymous
    - action_utter_anonymous_text

##i am fine story with contact affirm
* _greet
    - action_utter_greet
* _affirm
    - utter_affirm
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

##i am fine story with contact deny
* _greet
    - action_utter_greet
* _affirm
    - utter_affirm
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

##goodbye
* _goodbye
    - action_utter_goodbye

##goodbye
* _goodbye
    - action_utter_goodbye

## create incident deny
* _deny
    - utter_create_incident
* _deny
    - utter_ask_helpmore
* _deny
    - utter_deny

## create incident deny
* _deny
    - utter_create_incident
* _deny
    - utter_ask_helpmore
* _deny
    - utter_deny

## create incident deny
* _deny
    - utter_create_incident
* _deny
    - utter_ask_helpmore
* _deny
    - utter_deny

## create incident deny with contact affirm
* _deny
    - utter_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## create incident deny with contact deny
* _deny
    - utter_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## create incident affirm
* _deny
    - utter_create_incident
* _deny
        - utter_ask_helpmore
* _affirm
    - utter_affirm

## create incident affirm
* _deny
    - utter_create_incident
* _deny
        - utter_ask_helpmore
* _affirm
    - utter_affirm

## thanks with deny
* _thanks
    - utter_thanks
    - utter_ask_helpmore
* _deny
    - utter_deny

## thanks with deny with contact affirm
* _thanks
    - utter_thanks
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## thanks with deny with contact deny
* _thanks
    - utter_thanks
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## thanks with affirm
* _thanks
    - utter_thanks
    - utter_ask_helpmore
* _affirm
    - utter_affirm

##I have another query
* _on_more_query
    - utter_affirm

##I have another query
* _on_more_query
    - utter_affirm

##I have another query
* _on_more_query
    - utter_affirm

## Knowledge 1
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _affirm
    - action_utter_great

## Knowledge 1 copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _affirm
    - action_utter_great

## Knowledge 1 copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _affirm
    - action_utter_great

## Knowledge 2
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _deny
    - action_knowledge_incident_condition_check
* _affirm
> check1
> check2

## Knowledge 3 affirm
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0030885]
    - action_knowledge_incident_condition_check
* _affirm
    - action_utter_great

## Knowledge 3 deny
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0030810]
    - action_knowledge_incident_condition_check
* _deny
> check1
> check2

## Knowledge 2 copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _deny
    - action_knowledge_incident_condition_check
* _affirm
> check1
> check2

## Knowledge 3 affirm copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0030845]
    - action_knowledge_incident_condition_check
* _affirm
    - action_utter_great

## Knowledge 3 deny copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0030812]
    - action_knowledge_incident_condition_check
* _deny
> check1
> check2

## Knowledge 2 copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _deny
    - action_knowledge_incident_condition_check
* _affirm
> check1
> check2

## Knowledge 3 affirm copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0030100]
    - action_knowledge_incident_condition_check
* _affirm
    - action_utter_great

## Knowledge 3 deny copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0030500]
    - action_knowledge_incident_condition_check
* _deny
> check1
> check2

## Knowledge 2 copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _deny
    - action_knowledge_incident_condition_check
* _affirm
> check1
> check2

## Knowledge 3 affirm copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0039999]
    - action_knowledge_incident_condition_check
* _affirm
    - action_utter_great

## Knowledge 3 deny copy
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _knowledge[knowledge_id=KB0020000]
    - action_knowledge_incident_condition_check
* _deny
> check1
> check2

check1{"knowledge_post_reply": True}
     - action_before_create
     - utter_creating_incident
     - utter_ask_short_description
   * _info
     - action_create_incident_ask_short_description
     - utter_ask_impact
   * _info[value=high]
     - action_middle_action
     - utter_ask_urgency
   * _info[value=high]
     - action_create_incident

check2{"knowledge_post_reply": False}
     - action_utter_great

## Knowledge 1
* _knowledge
    - action_search_knowledge
    - action_post_knowledge_reply
* _deny
    - action_knowledge_incident_condition_check
* _deny
    - utter_affirm

## Create incident 5
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _invlaid
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 5
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _status
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 5
* _greet
  - action_utter_greet
* _create
  - action_before_create
  - utter_creating_incident
  - utter_ask_short_description
* _invalid
  - action_create_incident_ask_short_description
  - utter_ask_impact
* _info[value=high]
  - action_middle_action
  - utter_ask_urgency
* _info[value=low]
  - action_create_incident
* _thanks
  - utter_thanks

## Create incident 1
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _deny
    - utter_cancel

## Create incident 1
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _deny
    - utter_cancel

## Create incident 1
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=1]
    - action_middle_action
    - utter_ask_urgency
* _deny
    - utter_cancel

## Create incident 1
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=1]
    - action_middle_action
    - utter_ask_urgency
* _info[value=2]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 1
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=2]
    - action_middle_action
    - utter_ask_urgency
* _info[value=3]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 1 with contact affirm
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=2]
    - action_middle_action
    - utter_ask_urgency
* _info[value=3]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Create incident 1 with contact deny
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=2]
    - action_middle_action
    - utter_ask_urgency
* _info[value=3]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## Create incident 1
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=3]
    - action_middle_action
    - utter_ask_urgency
* _info[value=1]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 1
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 2
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=medium]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 2 with contact affirm
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=medium]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Create incident 2 with contact deny
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=medium]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## Create incident 3
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=high]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 3 with contact affirm
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=high]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Create incident 3 with contact deny
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=high]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## Create incident 4
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=medium]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 4 with contact affirm
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=medium]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Create incident 4 with contact deny
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=medium]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## Create incident 5
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _thanks
    - utter_thanks

## Create incident 5 with contact affirm
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Create incident 5 with contact deny
* _greet
    - action_utter_greet
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## Create incident 6
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=high]
    - action_create_incident

## Create incident 6 with contact affirm
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=high]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Create incident 6 with contact deny
* _create
    - action_before_create
    - utter_creating_incident
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=high]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

##status with state
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state

## no to are you satisfied
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state

## no to are you satisfied with contact affirm
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## no to are you satisfied with contact deny
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_affirm

## status with state
* _greet
    - action_utter_greet
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state

## status with state
* _greet
    - action_utter_greet
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state

## status with state and contact affirm
* _greet
    - action_utter_greet
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with state and contact deny
* _greet
    - action_utter_greet
* _status[state=open]
    - utter_telllatestincidents
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_deny

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0000002,state=open]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0000002,state=open]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and state and contact affirm
* _greet
    - action_utter_greet
* _status[application_id=INC0000002,state=open]
    - utter_ack_dosearch
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and state and contact deny
* _greet
    - action_utter_greet
* _status[application_id=INC0000002,state=open]
    - utter_ack_dosearch
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0010030,state=close]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and state and contact affirm
* _greet
    - action_utter_greet
* _status[application_id=INC0010030,state=close]
    - utter_ack_dosearch
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and state and contact deny
* _greet
    - action_utter_greet
* _status[application_id=INC0010030,state=close]
    - utter_ack_dosearch
    - action_search_status_with_state
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0010030,state=close]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0010001,state=open]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0010001,state=open]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0010051,state=close]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and state
* _greet
    - action_utter_greet
* _status[application_id=INC0010051,state=close]
    - utter_ack_dosearch
    - action_search_status_with_state

## status with id and priority 1
* _greet
    - action_utter_greet
* _status[application_id=all,priority=moderate]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with id and priority 1 with contact affirm
* _greet
    - action_utter_greet
* _status[application_id=all,priority=moderate]
    - utter_ack_dosearch
    - action_search_status_with_priority
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and priority 1 with contact deny
* _greet
    - action_utter_greet
* _status[application_id=all,priority=moderate]
    - utter_ack_dosearch
    - action_search_status_with_priority
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_deny

## status with id and priority 1
* _greet
    - action_utter_greet
* _status[application_id=all,priority=moderate]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with id and priority 2
* _status[application_id=all,priority=high]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with id and priority 2 with contact affim
* _status[application_id=all,priority=high]
    - utter_ack_dosearch
    - action_search_status_with_priority
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and priority 2 with contact deny
* _status[application_id=all,priority=high]
    - utter_ack_dosearch
    - action_search_status_with_priority
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with id and priority 2
* _status[application_id=all,priority=high]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with id and priority
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,priority=high]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with id and priority
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,priority=high]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with id and priority
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,priority=low]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with id and priority with contact affirm
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,priority=low]
    - utter_ack_dosearch
    - action_search_status_with_priority
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and priority with contact deny
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,priority=low]
    - utter_ack_dosearch
    - action_search_status_with_priority
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with id and priority
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,priority=low]
    - utter_ack_dosearch
    - action_search_status_with_priority

## status with priority
* _greet
    - action_utter_greet
* _status[priority=low]
    - utter_on_it
    - action_search_status_with_priority

## status with priority
* _greet
    - action_utter_greet
* _status[priority=low]
    - utter_on_it
    - action_search_status_with_priority

## status for all incidents
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status

## status for all incidents with contact affirm
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status for all incidents with contact deny
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status for all incidents
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status

## status with id
* _greet
    - action_utter_greet
* _status[application_id=INC00001]
    - utter_ack_dosearch
    - action_search_status

## status with id with contact affirm
* _greet
    - action_utter_greet
* _status[application_id=INC00001]
    - utter_ack_dosearch
    - action_search_status
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id with contact deny
* _greet
    - action_utter_greet
* _status[application_id=INC00001]
    - utter_ack_dosearch
    - action_search_status
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with id
* _greet
    - action_utter_greet
* _status[application_id=INC00001]
    - utter_ack_dosearch
    - action_search_status

## status with id
* _greet
    - action_utter_greet
* _status[application_id=INC00001]
    - utter_ack_dosearch
    - action_search_status

## status with id
* _greet
    - action_utter_greet
* _status[application_id=INC00001]
    - utter_ack_dosearch
    - action_search_status

## status without id
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status

## status without id with contact affirm
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status without id with contact affirm
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status without id
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status

## Generated Story 5878303772628450798
* _status[application_id=INC02121]
    - utter_ack_dosearch
    - action_search_status

## Generated Story 5878303772628450798
* _status[application_id=INC02121]
    - utter_ack_dosearch
    - action_search_status

## Generated Story 4180839707546290107
* _status
    - utter_telllatestincidents
    - action_search_status

## Generated Story 4180839707546290107
* _status
    - utter_telllatestincidents
    - action_search_status

## Generated Story -1642594182023298385
* _status[application_id=INC00022]
    - utter_ack_dosearch
    - action_search_status

## Generated Story -1642594182023298385
* _status[application_id=inc0010073]
    - utter_ack_dosearch
    - action_search_status

## status with all as a application_id
* _status[application_id=all]
    - utter_telllatestincidents
    - action_search_status

## status with all as a application_id with contact affirm
* _status[application_id=all]
    - utter_telllatestincidents
    - action_search_status
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with all as a application_id with contact eny
* _status[application_id=all]
    - utter_telllatestincidents
    - action_search_status

* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with all as a application_id
* _status[application_id=all]
    - utter_telllatestincidents
    - action_search_status

## status for all incidents
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status

## status for all incidents
* _greet
    - action_utter_greet
* _status
    - utter_telllatestincidents
    - action_search_status

## Update incident without id 1
* _greet
    - action_utter_greet
* _update
    - action_before_update
    - utter_ask_tellapplicationid
* _value[application_id=INC0010040]
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _thanks
    - utter_thanks
    - utter_ask_helpmore

## Update incident without id 1 with contact affirm
* _greet
    - action_utter_greet
* _update
    - action_before_update
    - utter_ask_tellapplicationid
* _value[application_id=INC0010040]
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Update incident without id 1 with contact deny
* _greet
    - action_utter_greet
* _update
    - action_before_update
    - utter_ask_tellapplicationid
* _value[application_id=INC0010040]
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=low]
    - action_middle_action
    - utter_ask_urgency
* _info[value=low]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## Update incident without id 2
* _greet
    - action_utter_greet
* _update
    - action_before_update
    - utter_ask_tellapplicationid
* _value[application_id=INC0010022]
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=medium]
    - action_create_incident
* _thanks
    - utter_thanks

## Update incident without id 2 with contact affirm
* _greet
    - action_utter_greet
* _update
    - action_before_update
    - utter_ask_tellapplicationid
* _value[application_id=INC0010022]
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=medium]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## Update incident without id 2 with contact deny
* _greet
    - action_utter_greet
* _update
    - action_before_update
    - utter_ask_tellapplicationid
* _value[application_id=INC0010022]
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=medium]
    - action_create_incident
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## Update incident with id 1
* _greet
    - action_utter_greet
* _update[application_id=INC0010022]
    - action_before_update
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=high]
    - action_middle_action
    - utter_ask_urgency
* _info[value=medium]
    - action_create_incident
* _thanks
    - utter_thanks

## Update incident with id 1
* _greet
    - action_utter_greet
* _update[application_id=INC0000001]
    - action_before_update
    - utter_ask_short_description
* _knowledge
    - action_create_incident_ask_short_description
    - utter_ask_impact
* _info[value=medium]
    - action_middle_action
    - utter_ask_urgency
* _info[value=high]
    - action_create_incident
* _thanks
    - utter_thanks

## status with id and preference impact 1
* _greet
    - action_utter_greet
* _status[application_id=all,preference=impact,prefernce_value=low]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference impact 1 with contact affirm
* _greet
    - action_utter_greet
* _status[application_id=all,preference=impact,prefernce_value=low]
    - utter_ack_dosearch
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and preference impact 1 with contact deny
* _greet
    - action_utter_greet
* _status[application_id=all,preference=impact,prefernce_value=low]
    - utter_ack_dosearch
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks


## status with id and preference impact 1
* _greet
    - action_utter_greet
* _status[application_id=all,preference=impact,prefernce_value=low]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference impact 2
* _status[application_id=all,preference=impact,preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference impact 2 with contact affirm
* _status[application_id=all,preference=impact,preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and preference impact 2 with contact deny
* _status[application_id=all,preference=impact,preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with id and preference impact 2
* _status[application_id=all,preference=impact,preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference impact
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,preference=impact,preference_value=medium]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference impact
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,preference=impact,preference_value=medium]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference impact with contact affirm
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,preference=impact,preference_value=medium]
    - utter_ack_dosearch
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with id and preference impact with contact deny
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,preference=impact,preference_value=medium]
    - utter_ack_dosearch
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with id and preference impact
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,preference=impact, preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference impact
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,preference=impact, preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with preference impact
* _greet
    - action_utter_greet
* _status[preference=impact,preference_value=medium]
    - utter_on_it
    - action_search_status_with_preference

## status with preference impact
* _greet
    - action_utter_greet
* _status[preference=impact,preference_value=medium]
    - utter_on_it
    - action_search_status_with_preference

## status with id and preference urgency 1
* _greet
    - action_utter_greet
* _status[application_id=all,preference=urgency,prefernce_value=low]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference urgency 1
* _greet
    - action_utter_greet
* _status[application_id=all,preference=urgency,prefernce_value=low]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference urgency 2
* _status[application_id=all,preference=urgency,preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference urgency 2
* _status[application_id=all,preference=urgency,preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference urgency
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,preference=urgency,preference_value=medium]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference urgency
* _greet
    - action_utter_greet
* _status[application_id=INC0000001,preference=urgency,preference_value=medium]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference urgency
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,preference=urgency, preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with id and preference urgency
* _greet
    - action_utter_greet
* _status[application_id=INC0000011,preference=urgency, preference_value=high]
    - utter_ack_dosearch
    - action_search_status_with_preference

## status with preference urgency
* _greet
    - action_utter_greet
* _status[preference=urgency,preference_value=medium]
    - utter_on_it
    - action_search_status_with_preference

## status with preference urgency with contact affirm
* _greet
    - action_utter_greet
* _status[preference=urgency,preference_value=medium]
    - utter_on_it
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## status with preference urgency with contact deny
* _greet
    - action_utter_greet
* _status[preference=urgency,preference_value=medium]
    - utter_on_it
    - action_search_status_with_preference
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## status with preference urgency
* _greet
    - action_utter_greet
* _status[preference=urgency,preference_value=medium]
    - utter_on_it
    - action_search_status_with_preference

## when issue will be resolve/close/solve 1
* _greet
    - action_utter_greet
* _resolve_time
    - action_resolve_time

## when issue will be resolve/close/solve 2
* _greet
    - action_utter_greet
* _status[application_id=INC0010073]
    - utter_ack_dosearch
    - action_search_status
* _resolve_time
    - action_resolve_time

## when issue will be resolve/close/solve 2
* _greet
    - action_utter_greet
* _resolve_time
    - action_resolve_time
* _status[application_id=INC0010103]
    - action_resolve_time

## when issue will be resolve/close/solve 2
* _greet
    - action_utter_greet
* _resolve_time
    - action_resolve_time
* _status[application_id=INC0000012]
    - action_resolve_time

## when issue will be resolve/close/solve 2
* _greet
    - action_utter_greet
* _resolve_time
    - action_resolve_time
* _status[application_id=INC0010141]
    - action_resolve_time

## when issue will be resolve/close/solve 2 with contact affirm
* _greet
    - action_utter_greet
* _status[application_id=INC0010073]
    - utter_ack_dosearch
    - action_search_status
* _resolve_time
    - action_resolve_time
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## when issue will be resolve/close/solve 2 with contact deny
* _greet
    - action_utter_greet
* _status[application_id=INC0010073]
    - utter_ack_dosearch
    - action_search_status
* _resolve_time
    - action_resolve_time
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks

## when user requests to contact 1
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _affirm
    - utter_affirm

## when user requests to contact 2
* _contact
    - action_utter_contact
    - utter_ask_helpmore
* _deny
    - utter_thanks
