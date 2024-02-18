# Djano e-Commerce

Build your own e-Commerce brand with Django!

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)

## Introduction

Django e-Commerce provides you with almost everything you need for a simple e-commerce store: Payments with Stripe, Frontend with Bootstrap, and logic with Django.

This project pretty much boils e-commerce down to Frontend only, especially for smaller e-stores. For bigger, more SEO-friendly e-commerce stores, I recommend using the API.

## Installation

Installing this is simple

```bash
# Get the code from gitHub
github clone https://github.com/PureZinc/django_ecommerce_app.git

# Add an env file in the same location as the manage.py file
## .env should look something like this:
STRIPE_PUBLIC_KEY = '<your-public-key>'
STRIPE_SECRET_KEY = '<your-secret-key>'
DJANGO_SECRET_KEY = '<your-django-secret-key>'
