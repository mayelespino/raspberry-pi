#!/bin/bash
rsstail -zpHd1 -u http://slashdot.org/index.rss
rsstail -zpHd1 -u http://www.nytimes.com/services/xml/rss/nyt/Americas.xml
rsstail -zpHd1 -u http://www.nytimes.com/services/xml/rss/nyt/World.xml
rsstail -zpHd1 -u http://www.npr.org/rss/rss.php?id=1045
rsstail -zpHd1 -u http://www.npr.org/rss/rss.php?id=1016
rsstail -zpHd1 -u http://www.npr.org/rss/rss.php?id=1055
rsstail -zpHd1u http://feeds.feedburner.com/DailyJokes-ACleanJokeEveryday?format=xml
