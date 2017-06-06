-- Calculate the transitive closure of table relation

DROP TABLE IF EXISTS transitive;

CREATE TABLE transitive AS 
WITH RECURSIVE transitive_closure(entry1, entry2, distance) AS
( SELECT id, id, 0 AS distance FROM entry
 
  UNION ALL
 
  SELECT entry1, entry2, 1 AS distance FROM relation
  
  UNION ALL
 
  SELECT tc.entry1, r.entry2, tc.distance + 1 FROM relation AS r
    JOIN transitive_closure AS tc
      ON r.entry1 = tc.entry2
)
SELECT DISTINCT * FROM transitive_closure
ORDER BY entry1, entry2, distance;

-- Calculate the frequency of each entry based on the number of references

UPDATE entry SET freq = 0;

UPDATE entry SET freq =
(SELECT SUM(e2.refs) 
FROM entry e2, transitive t 
WHERE t.entry1 = e2.id AND entry.id=t.entry2
GROUP BY t.entry2);

