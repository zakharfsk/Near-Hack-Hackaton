from cryptogochi.celery import app
from django.shortcuts import render
import random


@app.task
def update_dates():
    rand = random.randint(20, 30)
    return rand

@app.task
def give_data():
    pass