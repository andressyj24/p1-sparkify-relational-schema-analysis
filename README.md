# Document Process

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

## Project Description

To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL. 

## Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

The purpose of this database is to facilitate Sparkify the understanding of their user's activity regarding to listening to music. As it is mentioned in the Introduction of this project, currently, Sparkify does not have a proper way to query this kind of data, as its data is spread in files.
With this database, Sparkify is able to execute queries regarding the activities of their users related to what artist, songs they listen to, in a specific point of time.

## State and justify your database schema design and ETL pipeline.

### Schema for Song Play Analysis

#### Fact Table
> **songplays** - records in log data associated with song plays i.e. records with page NextSong
        songplay_id (PK), start_time, user_id (FK), level, song_id (FK), artist_id (FK), session_id, location, user_agent

#### Dimension Tables

> **users** - users in the app
        user_id (PK), first_name, last_name, gender, level

> **songs** - songs in music database
        song_id (PK), title, artist_id, year, duration

> **artists** - artists in music database
        artist_id (PK), name, location, latitude, longitude

> **time** - timestamps of records in songplays broken down into specific units
        start_time (PK), hour, day, week, month, year, weekday

* Having dimensions composed of: Users Songs, Artists, Time, and the fact table centralizes the activity of the user measured with timestamp. Sparkify is able to perform analitycs in order to answer several questions like:
    * What artis is the most listened among its users?
    * What its the day of the week an artist is being played the most?
    * What songs are the most popular on satruday nights?
    
## How to run the scripts?

In order to run the scripts, you must follow these instructions:
### Execute the ETL with Python script:
1. Execute "run create_tables.py"
2. Execute "run etl.py"
3. Execute "run test.ipynb"

### Execute the ETL with Notebook:
1. Execute "run create_tables.py"
2. Run all the cells in  etl.ipynb
3. Execute "run test.ipynb"

Note: If you want to run again, make sure you reset the kernel for the python script and the notebook


