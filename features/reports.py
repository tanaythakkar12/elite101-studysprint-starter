"""Reporting helpers for StudySprint."""

from features.core import count_by_category


def deck_summary(data):
    return data["deck_name"] + ": " + str(len(data["cards"])) + " cards"


def category_report(data):
    # Get all the flashcards from the deck
    cards = data["cards"]

    # Count how many cards belong to each category
    report = count_by_category(cards)

    # Return the category counts
    return report