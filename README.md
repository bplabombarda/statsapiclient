# statsapiclient: A client for the NHL stats API

[![CircleCI](https://circleci.com/gh/bplabombarda/statsapiclient.svg?style=svg)](https://circleci.com/gh/bplabombarda/statsapiclient)

## Purpose

To provide a Python client to access the NHL's JSON API including game, play, and player data.


## Installation

    pip install statsapiclient


## Modules

### Schedule

`get_games`

Returns a list of games contained within the instantiated date or date range.


### Games

#### game

`get_box_score`

`get_line_score`

`get_play_by_play`


### Teams

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
    games = s.get_games()

    print(games[0]['gamePk'])    # 2018020612

Game data:

    from statsapiclient.games.game import Game

    g = Game('2018020612')

    box_score = g.get_box_score()
    line_score = g.get_line_score()
    play_by_play = g.get_play_by_play()
