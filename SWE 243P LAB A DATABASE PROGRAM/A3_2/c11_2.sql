USE ex;

DROP TABLE IF EXISTS members_committes;
DROP TABLE IF EXISTS members;
DROP TABLE IF EXISTS committees;

CREATE TABLE members 
(
  member_id     INT           PRIMARY KEY   AUTO_INCREMENT, 
  first_name    VARCHAR(50)   NOT NULL, 
  last_name     VARCHAR(50)   NOT NULL, 
  address       VARCHAR(50)   NOT NULL, 
  city          VARCHAR(25)   NOT NULL, 
  state         CHAR(2), 
  phone         VARCHAR(20)
);

CREATE TABLE committees 
(
  committee_id      INT            PRIMARY KEY   AUTO_INCREMENT, 
  committee_name    VARCHAR(50)    NOT NULL
);

CREATE TABLE members_committees
(
  member_id       INT    NOT NULL, 
  committee_id    INT    NOT NULL,
  CONSTRAINT fk_member_id 
	FOREIGN KEY (member_id)
	REFERENCES members (member_id), 
  CONSTRAINT fk_committee_id 
	FOREIGN KEY (committee_id)
	REFERENCES committees (committee_id)
);