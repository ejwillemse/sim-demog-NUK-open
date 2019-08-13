
# change the parameters based on Singapore statistics

input parameters

1. household composition
   - Description: create the initial household structure, i.e. how many adult, school age children, and infant
   - Parameter name(s): hh_composition
   - Source data file: 2000census-Table 9 Resident Households by Household Structure and Household Size.xlsx, 2010census-Table 9 Resident Households by Household Structure and Household Size.xlsx
   - TODO: derive the hh_comp
   - TODO: get alternative data source for 1990 (?)

2. age distribution
   - Description: create the initial population structure
   - Parameter name(s): age_distribution
   - Source data file: ../data/demographic_ethnicity.csv
   - TODO: ~~create age-specific population pattern from age-group~~  check prepare_age_dist.ipynb
   - TODO: ~~calculate the total population~~  check prepare_age_dist.ipynb
   - *Potential extension: add gender-specific*

3. fertility rates by age
   - Description: decide if a women should have new baby
   - Parameter name(s): fertility_age_probs, fertility_age_rates
   - Source data file: ../data/input_birth_fertility_rates_sin_1961-2018.csv
   - TODO: ~~prepare age-specific fertility rates table~~ check prepare_fertility.ipynb
   - TODO: ~~prepare age-specific fertility distribution by age~~ check prepare_fertility.ipynb
   - *Potential extension: add new born child sex (use age distribution data)*

4. death rate by age and gender
   - Description: decide if a person of specific age and sex should die
   - Parameter name(s): death_rates_m, death_rates_f
   - Source data file: ../data/death_rate_agespecific.csv
   - TODO: ~~prepare age-specific death rate table for male~~ check prepare_mortality.ipynb
   - TODO: ~~prepare age-specific death rate table for female~~ check prepare_mortality.ipynb

5. couple prob by age
   - Description: decide if a  person should or should not get married.
   - Parameter name(s): couple_probs, couple_prob, couple_age, couple_age_max
   - Source data file: ../data/input_relationship_status_sin_1980-2018.csv, check input_marriage_rates_sin_1980-2017.csv
   - TODO: ~~calculate the single parameter~~ check prepare_couple_prob
   - *Potential extension: can add age and sex specific*

6. couple age diff
   - Description: decide which age group one should marry with
   - Parameter name(s): partner_age_diff, partner_age_sd, min_partner_age
   - Source data file: ../data/agegroup_grooms_brides.ods
   - TODO: ~~calculate the two parameters to replace the -2 and 2~~ check prepare_marriage_stats_clean.ipynb
   - *Potential extension: can add age and sex specific*

7. divorce probability
   - Description: decide if a couple should divorce
   - Parameter name(s): divorce_prob, divorce_age, divorce_age_max
   - Source data file: ../data/input_relationship_status_sin_1980-2018.csv, M830202 - Divorce Rates, Annual.csv
   - TODO: ~~calculate the single parameter~~ check prepare_divorce_prob.ipynb
   - *Potential extension: can add age and sex specific*

8. leaving probability
   - Description: decide whether a single adult person who lives with parent should leave home and stay by him/her-self 
   - Parameter:leaving_prob, leaving_age
   - Souce data file: 
   - TODO: 

