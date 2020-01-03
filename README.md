# statsapiclient: A client for the NHL stats API

[![PyPI version](https://badge.fury.io/py/statsapiclient.svg)](https://pypi.org/project/statsapiclient)

[![CircleCI](https://circleci.com/gh/bplabombarda/statsapiclient.svg?style=svg)](https://circleci.com/gh/bplabombarda/statsapiclient)

## Purpose

To provide a Python client to access the NHL's JSON API including game, play, and player data.


## Installation

    pip install statsapiclient


## Modules

### Schedule

`games`

A list of games contained within the instantiated date or date range.


### Games

#### game

`json`

Raw JSON response data.

`box_score`

Box score object.

`line_score`

Line score object.

`plays`

Play object.


### Team

`get_active`

Returns a list of all active teams.

`get_active_by_conference`

Returns a list of all active teams in a given conference.

`get_active_by_division`

Returns a list of all active teams in a given division.


### Examples

Games from date:
      
    from statsapiclient.schedule import Schedule


    s = Schedule('2019-01-01')
    print(s.games[0]['gamePk'])    # 2018020612

Game data:

    from statsapiclient.games.game import Game

    g = Game('2018020612')

    box_score = g.box_score
    line_score = g.line_score
    play_by_play = g.plays

Play data:

    g.plays.all_plays                   # All plays
    g.plays.get_plays_by_period(1)      # All plays in the first period
    g.plays.get_penalty_plays()         # All penalty plays
    g.plays.get_scoring_plays()         # All scoring plays
