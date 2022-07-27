# NBA-Betting-Model_2022.py
This program collects and organizes over 6,000 NBA statistics daily. Its purpose is to efficiently gather NBA data for my sports betting models. I run this script daily and use the data for my machine learning models.

# NBA-Injuries.py
In the NBA, injury reports are notoriously unreliable. 

For example, LeBron James may be questionable for an entire month and play every day, but Ben Simmons may be questionable for an entire month and never play. Those two players being "questionable" on the injury report mean entirely different things. Also, certain players being questionable/doubftul impacts betting lines more than others.

This program attempts to measure the impact of injuries to specific players by tracking, measuring, and assigning value to injuries that affected the previous day's games. It learns which players were questionable/doubtful to play the night before, and then confirms whether or not they actually played. Then, my models will have better input on how injuries to certain players impacted team performance (and betting lines).

# NBA-Referee-Script.py
This script gathers data on the referees for each NBA game, each day.

NBA refs have certain biases, and tracking their impact on games is important. Scott Foster earned the nickname "The Extender" for a reason. This program collects data that allows my models to better weight referee impact on a game-by-game basis.

# Team-EFG%-by-Day.py
This script automatically scrapes team Effective Field Goal% (EFG%) data for each team, each day of the 2022 NBA season.

When building predictive models, it is helpful to know how a team has performed leading into each game, not just how they have performed overall. If I am building a model that is trying to predict the score of each NBA game, I would want to use data from each game for the 2022 season to get as large of a recent sample size as possible. However, using just the end-of-season statistics and applying them to each of a team's 82 games is insufficient.

For example, it wouldn't make sense to use the end-of-season Boston Celtics EFG% of 54% (rank: 10) and apply it to every game they played this season as their deFacto measure of EFG% because the Celtics were terrible to start the season, but finished great. It is more accurate to take the Celtics EFG% on January 1st and apply it to the corresponding odds and other statistics for the team on January 1st, January 2nd, 3rd, 4th, and so on. When combined and weighted with hundreds of other statistics utilized in the same way, this method allows for more accurate modeling.

This program does exactly as described above: it scrapes EFG% data for each team, each day, for the 2022 season. The URL or year can easily be changed to scrape hundreds of other statistics.
