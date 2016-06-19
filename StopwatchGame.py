#"Stopwatch: The Game"

import simplegui

global time, minutes, seconds, x, y
time = 0; minutes = 0; seconds = 0.0; x = 0; y = 0

def format(t):
    global time, seconds, minutes
    minutes = t // 600
    seconds = t % 600.0
    if seconds > 99:
        time = str(minutes) + ":" + str(seconds/10)
    else:
        time = str(minutes) + ":0" + str(seconds/10)
    return time
    
def start_handler():
    timer.start()
    
def stop_handler():
    global time, x, y, seconds
    if timer.is_running():
        y += 1
        if ((seconds % 10) == 0):
            x += 1
    timer.stop()
    
def reset_handler():
    global time, minutes, seconds, x, y
    minutes = 0; seconds = 0.0; x =0; y = 0
    timer.stop()

def timer_handler():
    global time, minutes, seconds, k
    seconds += 1
    if seconds == 599:
        minutes += 1
        seconds = 0.0    

def draw_handler(canvas):
    if seconds > 99:
        canvas.draw_text((str(minutes) + ":" + str(seconds/10)), (100, 110), 48, "White")
    else:
        canvas.draw_text((str(minutes) + ":0" + str(seconds/10)), (100, 110), 48, "white")
    canvas.draw_text((str(x) + "/" + str(y)), (240, 25), 30, "Green")
    
frame = simplegui.create_frame("Stopwatch: The Game", 300, 200)

timer = simplegui.create_timer(100, timer_handler)

frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler, 60)
frame.add_button("Stop", stop_handler, 60)
frame.add_button("Reset", reset_handler, 60)

frame.start()