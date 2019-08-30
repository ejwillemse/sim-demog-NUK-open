## Dummy allocation

This folder contains data for a dummy allocation of a 100'000 population to 380 buildings over a 10-year period. 
The building allocation can be traced via the `Building.ID` key.

The population, with their assigned building id is in:

* `pop_10_years_allocated.csv`

For info on the basic file keys, excluding the new `Building.ID`, see `sim-demog-NUK-open/`

Summary statistics for the allocation can be found in:

* `pop_10_years_allocated_building_summary.csv`

A simple random allocation is done while trying to respect the number of people already allocated to each building. 
The allocation is done for each year, therefore there is significant change in the year to year allocation.
In essence, all residents relocate each year.

The fields for `pop_10_years_allocated.csv` are:

 * `year <int>`: simulation year of population
 * `household_id <id>`: id of household to which person belongs
 * `size <int>`: number of people in household
 * `Building.ID <id>`: id of building to which household is assigned
 * `person_id <id>`: id of person, not unique since person is found over multiple years
 * `age <int>`: age of person
 * `adam_eve <int>`: whether person was part of initial population,
 * `children_id <str>`:	';' separated string of person ids, each being a child of person
 * `divorced <bool>`: True or False
 * `father_id	<id>`: person id of father, if any
 * `mother_id	<id>`: person id of mother, if any
 * `partner_id <id>`: person id of partner, if any
 * `sex	<int>`: gender {0:male, 1:female}
 * `with_parents <bool>`:	True if person still stays with parents, False otherwise
