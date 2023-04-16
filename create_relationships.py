"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
from faker import Faker
from random import randint, choice


# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # TODO: Function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
# SQL query that inserts a row of data in the relationships table.
    add_relationship_query = """
 INSERT INTO relationships
 (
 person1_id,
 person2_id,
 type,
 start_date
 )
 VALUES (?, ?, ?, ?);
"""

    cur.execute(add_relationship_query)
    con.commit()
    con.close()
    return

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    # TODO: Function body
    con = sqlite3.connect('social_network.db')
    cur = con.cursor()
    # SQL query that inserts a row of data in the relationships table.
    add_relationship_query = """
    INSERT INTO relationships
    (
    person1_id,
    person2_id,
    type,
    start_date
    )
    VALUES (?, ?, ?, ?);
    """

    fake = Faker()
    # Randomly select first person in relationship
    person1_id = randint(1, 200)
    # Randomly select second person in relationship
    # Loop ensures person will not be in a relationship with themself
    person2_id = randint(1, 200)
    while person2_id == person1_id:
        person2_id = randint(1, 200)
    # Randomly select a relationship type
    rel_type = choice(('friend', 'spouse', 'partner', 'relative'))
    # Randomly select a relationship start date between now and 50 years ago
    start_date = fake.date_between(start_date='-50y', end_date='today')
    # Create tuple of data for the new relationship
    new_relationship = (person1_id, person2_id, rel_type, start_date)
    # Add the new relationship to the DB
    cur.execute(add_relationship_query, new_relationship)
    con.commit()
    con.close()


if __name__ == '__main__':
   main()