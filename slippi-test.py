from slippi import Game
import pandas as pd
import numbers as np
import matplotlib.pyplot as plt
import os

def read(dir_path):
    objs = []
    i = 0
    for filenamme in os.listdir(dir_path):
        if i >= 1:
            break
        f = os.path.join(dir_path, filenamme)
        if os.path.isfile(f):
            objs.append(Game(f))
            i += 1
    return objs

def plot_duration(games):
    durations = []
    for game in games:
        durations.append(game.metadata.duration)
    plt.hist(durations, bins=5, edgecolor='black')
    plt.xlabel('durations')
    plt.ylabel('Game count')
    plt.show()

def main(path):
    games = read(path)
    print(len(games))
    print(games[0])
    #plot_duration(games)
    return



if __name__ == "__main__":
    path = 'D:\Slippi-Archive'
    # game.frames[-1].ports[1].leader.post.stocks
    main(path)