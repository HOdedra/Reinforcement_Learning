"""
Reinforcement Learning using table lookup Q-learning method.
An agent "Blue circle" is positioned in a grid and must make its way to the 
green square. This is the end goal. Each time the agent should imporve its 
strategy to reach the final Square. There are two traps the red and the wall 
which will reset the agent. 
"""
import turtle
import pandas as pd
import numpy as np
import time

np.random.seed(2)

""" Setting Parameters """

#N_STATES = 12   # the size of the 2D world
ACTIONS = ['left', 'right', 'down','up']     # available actions
EPSILON = 0.9   # greedy police (randomness factor)
ALPHA = 0.1     # learning rate 
GAMMA = 0.9    # discount factor
MAX_EPISODES = 13   # maximum episodes
FRESH_TIME = 0.3    # fresh time for one move


def isGoal():
    if player.xcor() == -25 and player.ycor() == 225:
        player.goto(-175,125)
        status_func(1)
        S_ = 'terminal'
        R = 1
        interaction = 'Episode %s: total_steps = %s' %(episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r', end='')
        return S_, R
    else:
        pass
    

def isFire():
    if player.xcor() == -25 and player.ycor() == 175:
        player.goto(-175,125)
        status_func(3)
        S_ = 'terminal'
        R = -1
        interaction = 'Episode %s: total_steps = %s' %(episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r', end='')
        return S_, R
    else:
        pass 
    

def isWall():
    if player.xcor() == -125 and player.ycor() == 175:
        player.goto(-175,125)
        status_func(2)
        S_ = 'terminal'
        R = -1
        interaction = 'Episode %s: total_steps = %s' %(episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r', end='')
        return S_, R
    else:
        pass
    
    
""" Player Movement """

playerspeed = 50

""" Create the token object """
    
player = turtle.Turtle()
player.color("blue")
player.shape("circle")
player.penup()
player.speed(0)
player.setposition(-175,125)
player.setheading(90)



#Move the player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -175:
        x = -175
    player.setx(x)
    isGoal()
    isFire()
    isWall()
    S_ = player.pos()
    R = 0
    
def move_right():
    x = player.xcor()
    x += playerspeed
    if x > -25:
        x = -25
    player.setx(x)
    isGoal()
    isFire()
    isWall()
    S_ = player.pos()
    R = 0
    
def move_up():
    y = player.ycor()
    y += playerspeed
    if y > 225:
        y = 225
    player.sety(y)
    isGoal()
    isFire()
    isWall()
    S_ = player.pos()
    R = 0
    
def move_down():
    y = player.ycor()
    y -= playerspeed
    if y < 125:
        y = 125
    player.sety(y)
    isGoal()
    isFire()
    isWall()
    S_ = player.pos()
    R = 0
    
#Create Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(move_up, "Up")
turtle.onkey(move_down, "Down")

def build_q_table(n_states, actions):
    table = pd.DataFrame(
        np.zeros((n_states, len(actions))),     # q_table initial values
        columns=actions,    # actions's name
    )
    # print(table)    # show table
    return table


def choose_action(state, q_table):
    # This is how to choose an action
    state_actions = q_table.iloc[state, :]
    # act non-greedy or state-action have no value
    if (np.random.uniform() > EPSILON) or ((state_actions == 0).all()): 
        action_name = np.random.choice(ACTIONS)
    else:   # act greedy
        # replace argmax to idxmax as argmax means a different function 
        action_name = state_actions.idxmax()    
    return action_name



def get_env_feedback(A):
    if A == 'right':
        move_right()
    elif A == 'left':
        move_left()
    elif A == 'up':
        move_up()
    else: #down 
        move_down()
    return S_, R
    
    

def update_env(S, episode):
    wn = turtle.Screen()
    wn.bgcolor("white")
    wn.title("test")
    
    """ Create the Grid """
    
    greg = turtle.Turtle()
    greg.speed(0)
    
    def create_square(size,color="black"):
        greg.color(color)
        greg.pd()
        for i in range(4):
            greg.fd(size)
            greg.lt(90)
        greg.pu()
        greg.fd(size)
    
    def row(size,color="black"):
        for i in range(4):
            create_square(size)
    
    def board(size,color="black"):
        greg.pu()
        greg.goto(-(size*4),(size*4))
        for i in range(3):
            row(size)
            greg.bk(size*4)
            greg.rt(90)
            greg.fd(size)
            greg.lt(90)
    
    def color_square(start_pos,distance_sq, sq_width, color):
        greg.pu()
        greg.goto(start_pos)
        greg.fd(distance_sq)
        greg.color(color)
        greg.begin_fill()
        for i in range(4):
            greg.fd(sq_width)
            greg.lt(90)
        greg.end_fill()
        greg.pu()
        
    def initiate_grid(): 
        board(50)
        color_square((-200,200),150, 50,color="green")
        color_square((-200,150),50, 50,color="black")
        color_square((-200,150),150, 50,color="red")
        greg.hideturtle()
    
    initiate_grid()
    
    """ Create the token object """
    
    player = turtle.Turtle()
    player.color("black")
    player.shape("circle")
    player.penup()
    player.speed(0)
    player.setposition(S)
    player.setheading(90)
    
    
    
    
def rl():
    possible_states = {0:(-175,125),
                      1:(-175,175),
                      2:(-175,225),
                      3:(-125,125),
                      4:(-125,175),
                      5:(-125,225),
                      6:(-75,125),
                      7:(-75,175),
                      8:(-75,225),
                      9:(-25,125),
                      10:(-25,175),
                      11:(-25,225)}
    
    inv_possible_states = {v:k for k,v in possible_states.items()}
    
    #build the qtable 
    q_table = build_q_table(len(possible_states),ACTIONS)
    for episode in range(MAX_EPISODES):
        #step_counter = 0
        which_state = 0
        S = possible_states[which_state]
        is_terminated = False
        update_env(S,episode)
        while not is_terminated:
            
            A = choose_action(which_state, q_table)
            # take action & get next state and reward
            S_, R = get_env_feedback(A) 
            q_predict = q_table.loc[which_state, A]
            if S_ != 'terminal':
                S_ = inv_possible_states[S_]
                # next state is not terminal
                q_target = R + GAMMA * q_table.iloc[S_, :].max()   
            else:
                q_target = R     # next state is terminal
                is_terminated = True    # terminate this episode

            q_table.loc[S, A] += ALPHA * (q_target - q_predict)  # update
            S = S_  # move to next state

            update_env(S, episode)
            #step_counter += 1
    return q_table



rl()
    