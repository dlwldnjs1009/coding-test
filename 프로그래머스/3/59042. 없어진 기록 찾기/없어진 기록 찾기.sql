
SELECT
    OUTS.ANIMAL_ID,
    OUTS.NAME
FROM ANIMAL_INS AS INS
RIGHT OUTER JOIN ANIMAL_OUTS AS OUTS
ON INS.ANIMAL_ID = OUTS.ANIMAL_ID
WHERE INS.ANIMAL_ID IS NULL AND INS.NAME IS NULL
ORDER BY INS.ANIMAL_ID;