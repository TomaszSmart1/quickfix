def send_heartbeat(sessionID):
    heartbeat = fix.Message()
    heartbeat.getHeader().setField(fix.BeginString("FIX.4.4"))
    heartbeat.getHeader().setField(fix.MsgType("0"))  # MsgType "0" is Heartbeat
    fix.Session.sendToTarget(heartbeat, sessionID)