##i am fine sotry
* _greet
    - action_utter_greet
* _affirm
    - utter_affirm

##goodbye
* _goodbye
    - action_utter_goodbye

## thanks with deny
* _thanks
    - utter_thanks
    - utter_ask_helpmore
* _deny
    - utter_deny

## thanks with affirm
* _thanks
    - utter_thanks
    - utter_ask_helpmore
* _affirm
    - utter_affirm

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
