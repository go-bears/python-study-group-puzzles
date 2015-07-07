/* coding challenge for Ada Academy application 

 You have been hired by the eccentric leaders of the National Organization of Farmers Market Enthusiasts (NOFME)* to analyze publicly available data on farmers markets throughout the United States for their annual report.

They have provided to you a CSV data file from Data.gov containing information about farmers markets in the United States. Data for each market includes name, full address (including latitude and longitude), product types sold, seasonal availability, and more (see file's column headers). For all of the questions, exclude all markets that are located within a city with more than one word in its name. Use the data in the file to answer the below questions, giving an explanation of the techniques you used to arrive at each answer.

Questions:

    1. How many markets sell vegetables, but not anything sweet? 
    2. What state has the highest density of famers market per capita? What state has the lowest? 
    3. How many US farmers markets are between the Rocky Mountains and the Mississippi river?
    4. What is one fact or pattern about farmers markets in the United States that you can recognize using the raw data?
*/

/* Method for #3  select Alberquerque and St. Louis as longitude points. Alberquerque visually aligns with midpoint of Rocky Mountains, and St. Louis seems to be Easternmost bend of the Mississippi River*/

 SELECT count(*) FROM fmfiltered2
    WHERE longitude between -106.68393 and -90.185394 

/* this total count needs to be refined because the Missiissipi River veers west and crosses into Minnesota, subtracting for cities in Minnesota and Wisconsin that have farmers markets but like west of St. Louis but do not yet cross the the Mississipi River boundary. For this boundary. I used Osceola, MN's -92.698534 longitude, a city that appears to be the easternmost edge of the Mississipi River within Minnesota,  to select out which markets in Minnesota that operate east of the Mississippi River) Total number of farmers markets that lie east of Osceola = 15 in Minnesota and Wisconsin, as the Mississippi is situated a little more west than St. Louis and the river crosses these states instead of functioning as a state border. */


SELECT count(*) FROM fmfiltered2
WHERE state = "Minnesota" and longitude > -92.698534 

/*for farmers markets in Wisconsin, I ran the following query, filtering for markets that are in Wisconsin, but still lie between the longitude of Osceloa, MN and St. Louis, MO */

SELECT count(* )FROM fmfiltered2
    WHERE state = 'Wisconsin'and  longitude BETWEEN -92.698534 AND -90.185394
