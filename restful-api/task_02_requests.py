#!/usr/bin/python3
"""This module defines functions to fetch and process API data."""
import requests
import csv


def fetch_and_print_posts():
    """Fetch posts from JSONPlaceholder and print titles."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch posts from JSONPlaceholder and save to CSV."""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = r.json()
        data = [{'id': p['id'], 'title': p['title'], 'body': p['body']}
                for p in posts]
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(data)
