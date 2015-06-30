import sqlite3 as lite
import pandas as pd

con = lite.connect('getting_started.db')

cur = con.cursor()

CREATE TABLE cities (name text, state text);

INSERT INTO cities (name, state, Year, Warm Month, Cold Month, Average) VALUES
    ('New York City', 'NY', '2013', 'July', 'January', '62'),
    ('Boston', 'MA', '2013', 'July', 'January', '59'),
    ('Chicago', 'IL', '2013', 'July', 'January', '59'),
    ('Miami', 'FL', '2013', 'August', 'January', '84'),
    ('Dallas', 'TX', '2013', 'July', 'January', '77'),
    ('Seattle', 'WA', '2013', 'July', 'January', '61'),
    ('Portland', 'OR', '2013', 'July', 'January', '63'),
    ('San Francisco', 'CA', '2013', 'September', 'December', '64'),
    ('Los Angeles', 'CA', '2013', 'September', 'December', '75');

cur.execute("SELECT * FROM cities")
rows = cur.fetchall()
cols = [desc[0] for desc in cur.description]
df = pd.DataFrame(rows, columns=cols)

def highest(n):
	for max(n) in df[Average]:
		print df[name]

print highest

