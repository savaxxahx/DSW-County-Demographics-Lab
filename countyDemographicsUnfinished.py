import json

def main():
    with open('county_demographics.json') as demographics_data:
        counties = json.load(demographics_data)
    print(alphabetically_first_county(counties))
    print(county_most_under_18(counties))
    print(percent_most_under_18(counties))
    print(most_under_18(counties))
    print(state_with_most_counties(counties))
    print(your_interesting_demographic_function(counties))

def alphabetically_first_county(counties):
    """Return the county with the name that comes first alphabetically."""
    first = counties[0]["County"]
    for c in counties :
        if c["County"] < first:
            first = c["County"]
    return first


def county_most_under_18(counties):
    """Return the name and state of a county ("<county name>, <state>") with the highest percent of under 18 year olds."""
    x = counties[0]["County"]
    y=counties[0]["State"]
    first = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"]> first:
            first = c["Age"]["Percent Under 18 Years"]
            x= c["County"]
            y= c["State"]
            print( first, x, y)
    return x + " " +  y 

    
def percent_most_under_18(counties):
    """Return the highest percent of under 18 year olds."""
    first = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"]> first:
            first = c["Age"]["Percent Under 18 Years"]
    return first

    
def most_under_18(counties):
    """Return a list with the name and state of a county ("<county name>, <state>") and the percent of under 18 year olds for a county with the highest percent of under 18 year olds."""
    x = counties[0]["County"]
    y=counties[0]["State"]
    first = counties[0]["Age"]["Percent Under 18 Years"]
    for c in counties:
        if c["Age"]["Percent Under 18 Years"] >first:
            first = c["Age"]["Percent Under 18 Years"]
            x= c["County"]
            y= c["State"]
    return x + " " +  y +" " +  str(first)


    
def state_with_most_counties(counties):
    """Return a state that has the most counties."""
    #Make a dictionary that has a key for each state and the values keep track of the number of counties in each state
    states = {}
    for c in counties:
        if c["State"] in states:
            states[c["State"]] += 1
        else: 
            states[c["State"]] = 1
        
    
    #Find the state in the dictionary with the most counties
    first = states['AL']
    x = 'Al'
    for s in states:
        if states[s] > first:
            first = states[s]
            x = s
    return x
        
        
    
    
    #Return the state with the most counties
    
    
def your_interesting_demographic_function(counties):
    """Compute and return an interesting fact using the demographic data about the counties in the US."""
    first = counties[0]["Miscellaneous"]["Percent Female"]
    x = counties[0]["County"]
    y=counties[0]["State"]
    for c in counties:
        if c["Miscellaneous"]["Percent Female"]> first:
            first =c["Miscellaneous"]["Percent Female"]
            y = c["State"]
            x = c["County"]
    return x + " " + y + " " + str(first)


if __name__ == '__main__':
    main()
