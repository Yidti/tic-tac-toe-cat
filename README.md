# Tic-tac-toe Cat

Tic-tac-toe Cat is a Python script which playing a game on a
three-by-three grid by two players. To get a deeper
thorough Wiki [Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe).

## Run the script

```sh
git clone https://github.com/Yidti/tic-tac-toe-cat.git
cd tic-tac-toe-cat
python3.10 main.py
```

## Examples for playing

```console                                                      
  ┌-------( TicTacToe )-------┬-----( Position No. )-------┐
  │    ┌─────┬─────┬─────┐    │     ┌─────┬─────┬─────┐    │
  │    │  X  │     │  ◯  │    │     │ 1,1 │ 1,2 │ 1,3 │    │
  │    ├─────┼─────┼─────┤    │     ├─────┼─────┼─────┤    │
  │    │  ◯  │  ◯  │  X  │    │     │ 2,1 │ 2,2 │ 2,3 │    │
  │    ├─────┼─────┼─────┤    │     ├─────┼─────┼─────┤    │
  │    │     │     │  X  │    │     │ 3,1 │ 3,2 │ 3,3 │    │
  │    └─────┴─────┴─────┘    │     └─────┴─────┴─────┘    │
  └---------------------------┴----------------------------┘
X:(1, 1) -> ◯:(2, 2) -> X:(3, 3) -> ◯:(2, 1) -> X:(2, 3) -> ◯:(1, 3)
Player 'X' - key in position: 3,1
```

## Introduction - [Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe)

1. 是一個兩人遊戲，輪流在三乘三的網格中，用Ｏ或Ｘ來標記空格。
2. 玩家將標記在垂直或水平或對角線方向連成一直線將獲得勝利。
3. 如果雙方都下得正確無誤，棋盤將會被填滿而和局。

## Version History

### V.1.0 - 2022.06.03

1. using two marks which are 'X' and '◯'.
2. judging who is a winner or game is a draw.
3. it shows play order including which position and who.