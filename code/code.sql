CREATE TABLE kickstarter_launch
(
	"Unnamed: 0" VARCHAR,
	launched_at VARCHAR,
	launch_to_deadline VARCHAR,
	creation_to_launch VARCHAR,
	launch_day VARCHAR,
	deadline_day VARCHAR,
	launch_month VARCHAR,
	deadline_month VARCHAR,
	launch_time VARCHAR,
	deadline_time VARCHAR
);
CREATE TABLE kickstarter_pledge
(
	"Unnamed: 0" VARCHAR,
	country_displayable_name VARCHAR,
	backers_count VARCHAR,
	category VARCHAR,
	created_at VARCHAR,
	deadline VARCHAR,
	goal VARCHAR,
	pledged VARCHAR,
	staff_pick VARCHAR,
	state VARCHAR,
	usd_pledged VARCHAR,
	sub_category VARCHAR,
	blurb_length VARCHAR
);

SELECT *
INTO kickstarter
FROM kickstarter_pledge
FULL OUTER JOIN kickstarter_launch
USING ("Unnamed: 0");

--check if the join worked
select * from kickstarter limit 5;