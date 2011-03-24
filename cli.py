#! /usr/bin/env python

import ai
import glob
import os
import mapobject
import world
import worldtalker
import itertools
import logging 
log = logging.getLogger("CLI")

LIFESPAN = 1000

import sys
import os

AI = []
def main(ai_classes=[]):
  w = world.World()
  wt = worldtalker.WorldTalker(w)

  for ai in ai_classes:
    AI.append(ai(wt))

  for ai in AI:
    ai._init()

  ai_cycler = itertools.cycle(AI)

  for ai in AI:
    b = mapobject.Building(wt)
    w.buildings[b] = next(ai_cycler)
    w.map.placeObject(b,
      w.map.getRandomSquare())

  for turn in xrange(LIFESPAN):
      for ai in AI:
          ai._spin()
  #            try:
  #                ai.spin()
  #            except Exception, e:
  #                log.info("AI raised exception %s, skipping this turn for it" % (e))

      w.Turn()
  log.info("Finished simulating the world, press Enter to exit")
  raw_input()

def end_game():
  for ai in AI:
    log.info("%s:%s", ai.__class__, ai.calculateScore())

if __name__ == "__main__":
  main()