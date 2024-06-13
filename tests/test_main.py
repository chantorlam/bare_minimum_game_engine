# tests/test_main.py
import pytest
from main import Ball

def test_ball_initial_position():
    ball = Ball(100, 100, 20)
    assert ball.x == 100
    assert ball.y == 100

def test_ball_move():
    ball = Ball(100, 100, 20)
    ball.move()
    assert ball.y > 100  # Assuming gravity increases y position
