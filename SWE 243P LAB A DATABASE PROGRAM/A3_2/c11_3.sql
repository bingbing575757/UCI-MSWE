USE ex;

INSERT INTO members
VALUES (DEFAULT, 'Emily', 'Johnson', '1234 Elm Street', 'Los Angeles', 'CA', '213-555-7890');
INSERT INTO members
VALUES (DEFAULT, 'Michael', 'Williams', '5678 Oak Avenue', 'Chicago', 'IL', '312-555-1234');

INSERT INTO committees
VALUES (DEFAULT, 'Community Outreach');
INSERT INTO committees
VALUES (DEFAULT, 'Environmental Sustainability');


INSERT INTO members_committees
VALUES (1, 2);
INSERT INTO members_committees
VALUES (2, 1);
INSERT INTO members_committees
VALUES (2, 2);

SELECT c.committee_name, m.last_name, m.first_name
FROM committees c
	JOIN members_committees mc
	ON c.committee_id = mc.committee_id
	JOIN members m
    ON mc.member_id = m.member_id
ORDER BY c.committee_name, m.last_name, m.first_name;