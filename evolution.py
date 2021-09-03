from player import Player
import numpy as np
from config import CONFIG
from copy import deepcopy
import random
import datetime

REPORT_DIR = "./reports"


class Evolution():

    def __init__(self, mode):
        self.mode = mode

    # calculate fitness of players
    def calculate_fitness(self, players, delta_xs):
        for i, p in enumerate(players):
            p.fitness = delta_xs[i]

    def mutate(self, child):

        # TODO
        # child: an object of class `Player`
        n = random.random()
        prob = 0.2
        # width_of_distribution = 5
        if n <= prob:
            child.nn.w1 += np.random.normal(0,np.random.random(),child.nn.w1.shape)
        n = random.random()
        if n <= prob:
            child.nn.w2 += np.random.normal(0,np.random.random(),child.nn.w2.shape)
        n = random.random()
        if n <= prob:
            child.nn.b1 += np.random.normal(0,np.random.random(),1)
        n = random.random()
        if n <= prob:
            child.nn.b2 += np.random.normal(0,np.random.random(),1)
        return child


    def generate_new_population(self, num_players, prev_players=None):

        # in first generation, we create random players
        if prev_players is None:
            return [Player(self.mode) for _ in range(num_players)]

        else:

            # TODO
            # num_players example: 150
            # prev_players: an array of `Player` objects

            # TODO (additional): a selection method other than `fitness proportionate`
            # TODO (additional): implementing crossover

            #mutate 
            # new_players = []
            # tot = sum([x.fitness for x in prev_players])
            #rw
            # new_players = np.random.choice(prev_players, num_players, p=[x.fitness/tot for x in prev_players])
            # for i, player in enumerate(new_players):
            #     child = deepcopy(player)
            #     child = self.mutate(child)
            #     new_players[i] = child
            # new_players = list(new_players)

            # #select all
            # new_players = []
            # for player in prev_players:
            #     player = deepcopy(player)
            #     player = self.mutate(player)
            #     new_players.append(player)



            # #select random
            # new_players = []
            # for i in range(num_players):
            #     player = random.select(prev_players)
            #     player = deepcopy(player)
            #     player = self.mutate(player)
            #     new_players.append(player)

            # return new_players



            #crossover
            new_players = []
            fathers = []
            tot = sum([x.fitness for x in prev_players])
            fathers = np.random.choice(prev_players, num_players*2, p=[x.fitness/tot for x in prev_players])
            for i in range(num_players):
                child = deepcopy(fathers[2*i])
                child.nn.w2 = fathers[2*i+1].nn.w2
                child.nn.b2 = fathers[2*i+1].nn.b2
                child = self.mutate(child)
                new_players.append(child)
            return new_players

    def next_population_selection(self, players, num_players, gen_num, report_name):

        # TODO
        # num_players example: 100
        # players: an array of `Player` objects

        # TODO (additional): a selection method other than `top-k`
        # TODO (additional): plotting

        #find the best and worst
        players.sort(key= lambda x: x.fitness, reverse = True)
        best = players[0]
        worst = players[-1]
        avg_fitness = sum([x.fitness for x in players]) / len(players)
        with open(REPORT_DIR+"/"+report_name+".txt", "a") as f:
            f.write(f"{gen_num-1},{best.fitness},{worst.fitness},{avg_fitness}\n")
            
        





        chosen = []
        while len(chosen) != num_players:
            selected = random.sample(players, 10)
            selected.sort(key= lambda x: x.fitness, reverse=True)
            for i in range(len(selected)):
                if selected[i] not in chosen:
                    chosen.append(selected[i])
                    break
        return chosen
        return players[: num_players]
