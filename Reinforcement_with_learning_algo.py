""" Basic Reinforcement Learning environment using Turtle Graphics """
    
#imported libraries required for this project
import turtle
import pandas as pd
import numpy as np
import time

def intro_screen():
    #initialise the screen using a turtle object
    wn = turtle.Screen()
    wn.bgcolor("black")
    
    #Draw Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("White")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
        
    border_pen.hideturtle()
    
    #draw the title
    title_pen = turtle.Turtle()
    title_pen.speed(0)
    title_pen.color("White")
    title_pen.penup()
    title_pen.setposition(0,250)
    titlename1 = "Reinforcement" 
    titlename2 = "Learning"
    title_pen.write(titlename1,False, align="center",font=("Arial",30,"normal"))
    title_pen.setposition(0,200)
    title_pen.write(titlename2,False, align="center",font=("Arial",30,"normal"))
    title_pen.hideturtle()
    
    agent = turtle.Turtle()
    agent.color("blue")
    agent.shape("circle")
    agent.penup()
    agent.speed(0)
    agent.setposition(0,100)
    
    wn.delay(500)
    
    
    title_pen.setposition(0,50)
    description1 = "This agent will learn and explore the 2D Environment"
    description2= "The Objective of the agent is to reach the green triangle its home"
    title_pen.write(description1,False, align="center",font=("Arial",14,"normal"))
    time.sleep(2)
    title_pen.setposition(0,0)
    title_pen.write(description2,False, align="center",font=("Arial",14,"normal"))
    wn.delay(100)
    
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
    greg.setposition(-150,-100)
    grid(50)
    
    goal = turtle.Turtle()
    goal.color("green")
    goal.shape("triangle")
    goal.penup()
    goal.speed(0)
    goal.setposition(125,-75)
    goal.setheading(90)
    
    agent.clear()
    agent.setposition(-125,-75)
    
    time.sleep(5)
    
    wn.clear()



def main_programme():
    """ Environment """
    
    #initialise the screen using a turtle object
    wn = turtle.Screen()
    wn.bgcolor("black")
    wn.title("Basic_Reinforcement_Learning_Environment")
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("White")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
        
    border_pen.hideturtle()
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
    
    player = turtle.Turtle()
    player.color("blue")
    player.shape("circle")
    player.penup()
    player.speed(0)
    player.setheading(90)
    
    goal = turtle.Turtle()
    goal.color("green")
    goal.shape("triangle")
    goal.penup()
    goal.speed(0)
    goal.setposition(125,25)
    goal.setheading(90)
    
    
    
    #def status_turtle(claim):
        #status_pen = turtle.Turtle()
        #status_pen.speed(0)
        #status_pen.color("White")
        #status_pen.penup()
        #status_pen.setposition(-150,-250)
        #statusname = claim
        #status_pen.write(statusname,False, align="center",font=("Arial",13,"normal"))
        
    
    def player_set(S):
        player.setposition(S)
    
        
        
    N_STATES = 6   # the length of the 1 dimensional world
    ACTIONS = ['left', 'right']     # available actions
    EPSILON = 0.9   # greedy police
    ALPHA = 0.1     # learning rate
    GAMMA = 0.9    # discount factor
    MAX_EPISODES = 15   # maximum episodes
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
            #status_turtle(interaction)
            print('\n{}'.format(interaction), end='')
            time.sleep(2)
            print('\r', end='')
        else:
            player_set(coords[S])
            #status_turtle("Status: Agent is Exploring")
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
    time.sleep(5)
    wn.clear()
    
def end_screen():
    wn = turtle.Screen()
    wn.bgcolor("black")
    #Draw Border
    border_pen = turtle.Turtle()
    border_pen.speed(0)
    border_pen.color("White")
    border_pen.penup()
    border_pen.setposition(-300,-300)
    border_pen.pendown()
    border_pen.pensize(3)
    
    for side in range(4):
        border_pen.fd(600)
        border_pen.lt(90)
        
    border_pen.hideturtle()
    
    end_pen = turtle.Turtle()
    end_pen.speed(0)
    end_pen.color("White")
    end_pen.penup()
    end_pen.setposition(0,250)
    endname1 = "Reinforcement" 
    endname2 = "Learning"
    end_pen.write(endname1,False, align="center",font=("Arial",30,"normal"))
    end_pen.setposition(0,200)
    end_pen.write(endname2,False, align="center",font=("Arial",30,"normal"))
    end_pen.setposition(0,150)
    endname3 = "Agent has now finished exploring"
    end_pen.write(endname3,False, align="center",font=("Arial",15,"normal"))
    end_pen.setposition(0,100)
    endname4 = "View console for Q-table"
    end_pen.write(endname4,False, align="center",font=("Arial",15,"normal"))

    

if __name__ == "__main__":
    intro_screen()
    main_programme()
    end_screen()