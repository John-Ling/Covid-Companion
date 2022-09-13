"""
Information about the Coronavirus
"""

def get_info(info):
    global ans

    if (info=='symptoms'):
        ans=('''
The most common symptoms for Covid-19 are
fever, tiredness and dry cough. However some
patients have been reported to have aches, nasal congestion,
sore throat or diarrhea. Symptoms tend to start mild and 
begin to gradually increase in severity.

To see more go to shorturl.at/arCF8''')

    elif (info=='incubation'):
        ans=('''
The current estimated range for Covid-19
is 1-14 days, most commonly around 5 days.

To see more go to shorturl.at/arCF8''')

    elif (info=='transmission'):
        ans=('''
Covid-19 spreads mainly from person to person.
- Between people who are in close physical contact (within about 6 ft)
- Through droplets produced from infected coughs and sneezes
These droplets can land in the mouths, noses or eyes of people.

To see more go to shorturl.at/arCF8''')

    elif (info=='worry'):
        ans=('''
For children and young adults, infection via Covid-19
is generally mild. However it is not harmless as 1 in 5
people who contract the virus require hospital care. People
with weaker immune systems such as the elderly and people with
underlying medical conditions like Diabetes are at a high risk.

To see more go to shorturl.at/arCF8''')

    elif (info=='outside'):
        ans=('''
Given the current circumstances, you should minimise
going outside to protect yourself and your loved ones.
If you plan on going outside, update yourself on your area's
policy on leaving your home.

To see more go to shorturl.at/arCF8''')

    return ans