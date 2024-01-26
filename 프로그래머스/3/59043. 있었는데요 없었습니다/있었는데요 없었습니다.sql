SELECT ins.ANIMAL_ID,
        ins.NAME
        # ins.DATETIME,
        # outs.ANIMAL_ID,
        # outs.NAME,
        # outs.DATETIME
from  ANIMAL_INS as ins
    inner join ANIMAL_OUTS as outs 
    on ins.ANIMAL_ID = outs.ANIMAL_ID
where ins.DATETIME > outs.DATETIME
order by ins.DATETIME;