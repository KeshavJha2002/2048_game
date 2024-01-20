# Project Name

2048_game

## Brief Description of the Project

A fun game in python that tests player's mathematical skills

## Goals and Objectives of the Project

The main goal of the game is to create a simple,fun to play python game.

## User Journey

- A player will have 4 options/moves to play:
  - `up-arrow` : to move all the row to the most extreme top level possible in their respective column.
  - `down-arrow` : to move all the row to the most extreme bottom level possible in their respective column.
  - `left-arrow` : to move all the column to the most extreme left level possible in their respective row.
  - `right-arrow` : to move all the column to the most extreme right level possible in their respective row.

## Class Structure

## Functions List

### Function 1

- **Name:** `__adjust_row`
- **Params:**
  - `row_ind`: int
  - `order`: str
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function 2

- **Name:** `__adjust_col`
- **Params:**
  - `col_ind`: int
  - `order`: str
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function 3

- **Name:** `__generate_value_for_random_position`
- **Params:**
  - None
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function 4

- **Name:** `__reflect_move`
- **Params:**
  - `input_move`: str
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function 5

- **Name:** `__check_winner_or_loser`
- **Params:**
  - None
- **Return Type:** str
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function 6

- **Name:** `__print_prompt`
- **Params:**
  - None
- **Return Type:** str
- **Interfaces:** Private method
- **Access Specifier:** Static method
