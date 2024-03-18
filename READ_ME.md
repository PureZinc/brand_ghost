# Djano e-Commerce

Build your own brand with Django!

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)

## Introduction

BrandGhost provides you with almost everything you need for you to sell online: Newsletters, an e-Commerce store, and an API to display it all on a welcoming frontend (not included).

This project uses tools like payments with Stripe, Frontend with Bootstrap, and logic with Django.

This project pretty much boils e-commerce down to Frontend only, especially for smaller e-stores. For bigger, more SEO-friendly e-commerce stores, I recommend using more API.

## Installation

Installing this is simple

```bash
# Get the code from gitHub
github clone https://github.com/PureZinc/django_ecommerce_app.git

# Add an env file in the same location as the manage.py file
## .env should look something like this:
DJANGO_SECRET_KEY = '<your-django-secret-key>'
STRIPE_PUBLIC_KEY = '<your-public-key>'
STRIPE_SECRET_KEY = '<your-secret-key>'
EMAIL_HOST_USER = '<your-brand-email>'
EMAIL_HOST_PASSWORD = '<brand-email-password>'
