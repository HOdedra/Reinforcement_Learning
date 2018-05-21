""" Basic Reinforcement Learning environment using Turtle Graphics """
    
#imported libraries required for this project
import turtle
import pandas as pd
import numpy as np
import time
#import numpy as np


""" Environment """

#initialise the screen using a turtle object
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Basic_Reinforcement_Learning_Environment")
#wn.bgpic("game_background.gif")

#this function initializes the 2D environment
def grid(size): 
    #this function creates one square
    def create_square(size,color="white"):
        greg.color(color)
        greg.pd()
        for i in range(4):
            greg.fd(size)
            greg.lt(90)
        greg.pu()
        greg.fd(size)
    #this function creates a row of sqaures based on simply one square
    def row(size,color="white"):
            for i in range(6):
                create_square(size)
            greg.hideturtle()
            
    row(size)       

greg = turtle.Turtle()
greg.speed(0)
greg.setposition(-150,0)
grid(50)


def player_set(S):
    player = turtle.Turtle()
    player.color("blue")
    player.shape("circle")
    player.penup()
    player.speed(0)
    player.setposition(S)
    player.setheading(90)
    
N_STATES = 6   # the length of the 1 dimensional world
ACTIONS = ['left', 'right']     # available actions
EPSILON = 0.9   # greedy police
ALPHA = 0.1     # learning rate
GAMMA = 0.9    # discount factor
MAX_EPISODES = 13   # maximum episodes
FRESH_TIME = 0.3    # fresh time for one move
    
#this functions builds a Q-table and initializes all values to 0
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


def get_env_feedback(S, A):
    # This is how agent will interact with the environment
    if A == 'right':    # move right
        if S == N_STATES - 2:   # terminate
            S_ = 'terminal'
            R = 1
        else:
            S_ = S + 1
            R = 0
    else:   # move left
        R = 0
        if S == 0:
            S_ = S  # reach the wall
        else:
            S_ = S - 1
    return S_, R

def update_env(S, episode, step_counter):            
    coords = [(-125,25),(-75,25),(-25,25),(25,25),(75,25),(125,25)]
    
    if S == 'terminal':
        interaction = 'Episode %s: total_steps = %s' %(episode+1, step_counter)
        print('\r{}'.format(interaction), end='')
        time.sleep(2)
        print('\r', end='')
    else:
        player_set(coords[S])
        time.sleep(FRESH_TIME)


def rl():
    q_table = build_q_table(N_STATES, ACTIONS)
    for episode in range(MAX_EPISODES):
        step_counter = 0
        S = 0
        is_terminated = False
        update_env(S, episode, step_counter)
        while not is_terminated:
            A = choose_action(S, q_table)
            S_, R = get_env_feedback(S,A)
            q_predict = q_table.loc[S,A]
            if S_ != 'terminal':
                q_target = R + GAMMA * q_table.iloc[S_, :].max() 
            else:
                q_target = R
                is_terminated = True
            
            q_table.loc[S, A] += ALPHA * (q_target - q_predict)
            S = S_
            update_env(S, episode, step_counter+1)
            step_counter += 1
        return q_table

rl()