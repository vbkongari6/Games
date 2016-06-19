# classic arcade game "Pong"

import simplegui
import random

# initialize
WIDTH = 600; 	HEIGHT = 400;	PAD_WIDTH = 8; 	PAD_HEIGHT=80;	BALL_RADIUS = 20;
LEFT = False; 	RIGHT = True;	
HALF_PAD_WIDTH = PAD_WIDTH/2; 	HALF_PAD_HEIGHT = PAD_HEIGHT / 2; 
ball_pos =[WIDTH/2, HEIGHT/2]; 	ball_vel = [0/60.0, 0/60.0]

def spawn_ball(direction):
    global ball_pos, ball_vel
    ball_pos = [WIDTH / 2, HEIGHT / 2] # ball to be in middle of table
    if direction == RIGHT: # if direction is RIGHT, the ball's velocity is upper right
        ball_vel = [random.randrange(120, 240) / 60.0, -random.randrange(60, 180) / 60.0]
    elif direction == LEFT: # else (if left,) upper left								
        ball_vel = [-random.randrange(120, 240) / 60.0, -random.randrange(60, 180) / 60.0]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, score1, score2
    paddle1_pos = HEIGHT/2-HALF_PAD_HEIGHT; paddle2_pos = HEIGHT/2-HALF_PAD_HEIGHT; 
    paddle1_vel = 0.0;	paddle2_vel = 0.0;	score1 = 0;	 score2 = 0;
    spawn_ball(LEFT)
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # ball updates
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collision and reflection at top and bottom of canvas
    if (ball_pos[1] <= BALL_RADIUS) or (ball_pos[1] >= (HEIGHT - BALL_RADIUS)):
        ball_vel[1] = - ball_vel[1]
    # respawning the ball in the center of the table which heads towards the opposite gutter
    if ball_pos[0] <= (BALL_RADIUS + PAD_WIDTH): # at left gutter
        # determining whether paddle and ball will collide or not
        if ball_pos[1] >= paddle1_pos and ball_pos[1] <= paddle1_pos + PAD_HEIGHT :
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += 0.1*ball_vel[0]
        else:
            score2 += 1
            spawn_ball(RIGHT)
    if ball_pos[0] >= (WIDTH - (BALL_RADIUS + PAD_WIDTH)): # at right gutter
        if ball_pos[1] >= paddle2_pos and ball_pos[1] <= paddle2_pos + PAD_HEIGHT :
            ball_vel[0] = - ball_vel[0]
            ball_vel[0] += 0.1*ball_vel[0]
        else:
            score1 += 1
            spawn_ball(LEFT)
            
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # paddle updates keeping the paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel
    if paddle1_pos >= HEIGHT-PAD_HEIGHT: paddle1_pos = HEIGHT-PAD_HEIGHT
    if paddle2_pos >= HEIGHT-PAD_HEIGHT: paddle2_pos = HEIGHT-PAD_HEIGHT
    if paddle1_pos <= 0: paddle1_pos = 0
    if paddle2_pos <= 0: paddle2_pos = 0
        
    # draw paddles
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos], 
                     [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, 'White')
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], 
                     [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, 'White')

    # draw scores
    canvas.draw_text(str(score1), (135, 50), 45, 'White')
    canvas.draw_text(str(score2), (432, 50), 45, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"]: paddle1_vel -= 360/60.0
    elif key == simplegui.KEY_MAP["s"]:	paddle1_vel += 360/60.0
    elif key == simplegui.KEY_MAP["up"]: paddle2_vel -= 360/60.0
    elif key == simplegui.KEY_MAP["down"]: paddle2_vel += 360/60.0
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]: paddle1_vel = 0
    elif key==simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]: paddle2_vel = 0

# frame creation
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)    
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 200)

new_game()
frame.start() # frame start