# lambda in a box


im working on this for hosting computation for mutliplayer apps: [rubox](https://dkormann.com/rubox_app)


## usage

I want the absoulute simplest experience to host a function on my server.

requirements:

write a full app in a single file.

write a function for the backend write a function for the frontend, some shared data types, some light html view.

just send it and its online.

also apps hosted together should be able to interact effortless.


working prototype:
[chess](https://dkormann.com/rubox_app/chess) app where you can play chess against a chat partner. [chat](https://dkormann.com/rubox_app/chat) is its own app that gets called from chess app.


its super simple to use and still wayy to hard.

## security

each app runs in its storage space.
they can only work with each other through an exposed api.

apps should be hosted on a trusted domain and only be able to submit html for view, not have full access to the webpage.

aps exposing an api should have fine grained control. for example the chat should be able to allow chess to read username but not send message. Or ask the user if app wants message access.

## cost

storage and compute should be metered per developer and or user.
this should be done simply and transparently.

already can have a flops counter for compute. storage and compute is neatly separated per app.

todo: emulation and conceptual simplicity.
