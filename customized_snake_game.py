import turtle
import random


width = 800     #X Axis
height = 600    #Y Axis
delay = 60 #milliseconds
food_size = 30

offsets = {
    "Up": (0, 20), 
    "Down": (0, -20), 
    "Left": (-20, 0), 
    "Right": (20, 0)
}

def bind_direction_keys():
    screen.onkey(lambda: set_snake_direction("Up"), "Up")
    screen.onkey(lambda: set_snake_direction("Down"), "Down")
    screen.onkey(lambda: set_snake_direction("Left"), "Left")
    screen.onkey(lambda: set_snake_direction("Right"), "Right")


def set_snake_direction(direction):
    global snake_direction
    if direction == "Up":
        if snake_direction != "Down": #No self-collision by pressing wrongkey
            snake_direction = "Up"
    elif direction == "Down":
        if snake_direction != "Up": #No self-collision by pressing wrongkey
            snake_direction = "Down"
    elif direction == "Left":
        if snake_direction != "Right": #No self-collision by pressing wrongkey
            snake_direction = "Left"
    elif direction == "Right":
        if snake_direction != "Left": #No self-collision by pressing wrongkey
            snake_direction = "Right"



def game_loop():
    stamper.clearstamps() #remove existing stamps make by stamper
    new_head = snake[-1].copy()
    new_head[0] += offsets[snake_direction][0]
    new_head[1] += offsets[snake_direction][1]

    #Check for collisions
    if new_head in snake or new_head[0] < - width/2 or new_head[0] > width/2 or new_head[1] < - height/2 or new_head[1] > height /2:
        #  Left Wall, Right Wall, Bottom Wall, Top Wall, 
        reset()
    else:
    #Add new head to snake body
        snake.append(new_head)

        #Check food collision
        if not food_collision():
            snake.pop(0)  #Keep the snake the same length unless fed

        for segment in snake:
            stamper.goto(segment[0], segment[1]) #X Y coordinates
            stamper.stamp()
        
        screen.title(f"Snake Game: Score = {score}")
        screen.update()

        #Rinse and repeat
        turtle.ontimer(game_loop, delay)

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    distance = ((y2 - y1)**2 + (x2-x1) **2) ** 0.5 #Pythagoras
    return distance

def reset():
    global score, snake, snake_direction, food_pos
    
    score = 0
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    snake_direction = "Up"
    food_pos=get_random_food_pos()
    food.goto(food_pos)
    game_loop()


def food_collision():
    global food_pos, score
    if get_distance(snake[-1], food_pos) < 20:
        score +=1 #score = score + 1
        food_pos = get_random_food_pos()
        food.goto(food_pos)
        return True
    return False


def get_random_food_pos():
    x = random.randint(-width / 2 + food_size, width / 2 - food_size)
    y = random.randint(-height / 2 + food_size, height / 2 - food_size)
    return (x, y)



#Creating the window where we do the game
screen = turtle.Screen()
screen.setup(width, height)
screen.title("Snake")
screen.bgcolor("yellow")
screen.tracer(0) #Disables automatic animation

#Event handlers
screen.listen()
bind_direction_keys()





#creating a turtle to do your bidding
stamper = turtle.Turtle()
stamper.shape("circle")
stamper.color("green")
stamper.penup()
score = 0


#Food

food = turtle.Turtle()
food.shape("triangle")
food.color("red")
food.shapesize(food_size /20)
food.penup()


#Set animation in motion
reset()
turtle.done()