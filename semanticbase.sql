BEGIN TRANSACTION;
CREATE TABLE `relation` (
	`entry1`	INTEGER,
	`entry2`	INTEGER,
	PRIMARY KEY(`entry1`,`entry2`)
);
INSERT INTO `relation` (entry1,entry2) VALUES (3,1),
 (4,2),
 (5,2),
 (6,2),
 (7,2),
 (6,3),
 (7,3),
 (8,3),
 (2,1);
CREATE TABLE "entry" (
	`id`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`name`	INTEGER UNIQUE,
	`refs`	INTEGER,
	`freq`	INTEGER
);
INSERT INTO `entry` (id,name,refs,freq) VALUES (1,'metal',1,8),
 (2,'precious',1,5),
 (3,'coinage',1,4),
 (4,'palatium',1,1),
 (5,'palladium',1,1),
 (6,'gold',1,1),
 (7,'silver',1,1),
 (8,'copper',1,1);
COMMIT;
