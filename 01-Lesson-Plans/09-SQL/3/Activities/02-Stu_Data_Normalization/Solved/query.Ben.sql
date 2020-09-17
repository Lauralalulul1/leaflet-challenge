select p.name as "pet name", o.name as "owner name", pt.name as "pet type",st.name as "service type"
from pets p
inner join pet_types pt on pt.id = p.pet_type_id
inner join service_types st on st.id = pt.service_id 
inner join owners o on p.owner_id = o.id;