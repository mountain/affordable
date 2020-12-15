#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import gym_xxxxx

import gym
import argparse

from gym import wrappers, logger


parser = argparse.ArgumentParser()
parser.add_argument("-n", type=int, default=1000, help="number of epochs of training")
opt = parser.parse_args()


if __name__ == '__main__':

    logger.set_level(logger.INFO)

    env = gym.make('samples-xxxxx-v0')

    outdir = 'results'
    env = wrappers.Monitor(env, directory=outdir, force=True)
    env.seed(0)
    game = env.game

    episode_count = opt.n
    reward = 0
    done = False

    for i in range(episode_count):
        ob = env.reset()
        while True:
            action = game.act(ob, reward, done)
            ob, reward, done, _ = env.step(action)
            if done:
                break
            env.render(mode='rgb_array')

    # Close the env and write monitor result info to disk
    env.close()
