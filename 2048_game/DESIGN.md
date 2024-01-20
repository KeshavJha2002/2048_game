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

## ClassList

### Class `Board`

- **Attributes:**
  - `__board`: 4*4 integer matrix
- **Methods:**
  - ***Private methods:***
    - __print_prompt()
    - __adjust_row(self, row_ind, order)
    - __adjust_col(self, col_ind, order)
    - __generate_value_for_random_position(self)
    - __reflect_move(self, input_move)
    - __check_winner_or_loser(self)
  - ***Public methods:***
    - move_master(self)
    - get_arrow_key()
  - ***Class methods:***
    - None
  - ***Static methods:***
    - __print_prompt()
    - get_arrow_key()
  - ***Instance methods:***
    - __adjust_row(self, row_ind, order)
    - __adjust_col(self, col_ind, order)
    - __generate_value_for_random_position(self)
    - __reflect_move(self, input_move)
    - __check_winner_or_loser(self)
    - - move_master(self)

## Functions List

### Function `__adjust_row(self, row_ind, order)`

- **Params:**
  - `row_ind`: int
  - `order`: str
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function `__adjust_col(self, col_ind, order)`

- **Params:**
  - `col_ind`: int
  - `order`: str
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function `__generate_value_for_random_position(self)`

- **Params:**
  - None
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function `__reflect_move(self, input_move)`

- **Params:**
  - `input_move`: str
- **Return Type:** None
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function `__check_winner_or_loser(self)`

- **Params:**
  - None
- **Return Type:** str
- **Interfaces:** Private method
- **Access Specifier:** Instance method

### Function `__print_prompt()`

- **Params:**
  - None
- **Return Type:** str
- **Interfaces:** Private method
- **Access Specifier:** Static method

### Function `get_arrow_key()`

- **Params:**
  - None
- **Return Type:** str
- **Interfaces:** Public method
- **Access Specifier:** Static method

### Function `print_board(self)`

- **Params:**
  - None
- **Return Type:** None
- **Interfaces:** Public method
- **Access Specifier:** Instance method

### Function `move_master(self)`

- **Params:**
  - None
- **Return Type:** None
- **Interfaces:** Public method
- **Access Specifier:** Instance method

### Function `main()`

- **Params:**
  - None
- **Return Type:** None
- **Interfaces:** Public method
- **Access Specifier:** Global method
