-- c
-- c
SELECT cities.id, cities.name FROM cities, states WHERE cities.state_id = states.id AND states.name = "california";