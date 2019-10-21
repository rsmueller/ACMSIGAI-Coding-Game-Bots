import TronGame.environment as environment
import TronGame.basic_ai as basic_ai
from time import sleep

env = environment.environment(2)
ai_1 = basic_ai.basic_ai()
ai_2 = basic_ai.basic_ai()

while len(env.dead_players) == 0:
    print('-------------BATTLE--------------')
    print(env.render())
    move1 = ai_1.next_move(2, 0, env.player_coordinates)
    move2 = ai_2.next_move(2,1,env.player_coordinates)
    env.move(0,move1)
    env.move(1,move2)
    sleep(.5)

print('Winner!')
print(env.render())