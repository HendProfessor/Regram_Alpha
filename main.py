import eel
import server.server

#Run server
server.server.Server_core

#eel Run app
eel.init("web")
eel.start("message.htm", size=(800, 800))
