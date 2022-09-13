"""
Myths about the Coronavirus
"""

def debunk_myth(myth):
    global ans

    if (myth=='vaccines'):
        ans=('''
Currently there is no vaccine for Covid-19

The virus is so new and different that it needs
its own vaccine. However researchers are working
to develop one with the support of WHO.

To see more go to shorturl.at/bopDW''')

    elif (myth=='mosquitoes'):
        ans=('''
Covid-19 cannot be transmitted through mosquitoes

The Coronavirus can be spread through droplets
produced from sneezes and coughs of an infected
person.

To see more go to shorturl.at/bopDW''')

    elif (myth=='antibiotics'):
        ans=('''
No, antibiotics don't work against viruses, only bacteria

Covid-19 is a virus therefore antibiotics should
not be used as a means of prevention or treatment.
However if you are hospitalized, you may recieve
antibiotics since bacterial co-infection is possible.

To see more go to shorturl.at/bopDW''')

    elif (myth=='garlic'):
        ans=('''
Eating garlic will not prevent Covid-19

While garlic may have antimicrobial
properties, there is no evidence that eating
garlic has protected people from Covid-19.

To see more go to shorturl.at/bopDW''')

    elif (myth=='pets'):
        ans=('''    
You cannot contract Covid-19 from your pets

Although one dog in Hong Kong caught a "low-level infection",
there is now evidence to suggest you can catch the disease from
your pets dogs, cats or otherwise.

To see more go to shorturl.at/bopDW''')

    elif (myth=='face masks'):
        ans=('''
It depends

While wearing face masks doesn't guarantee immunity
from the virus, since viral particles are small enough
to penetrate masks, they are effective at capturing droplets
which is the main transmission route of Covid-19.

To see more go to shorturl.at/bopDW''')

    elif (myth=='ultraviolet'):
        ans=('''
UV lamps should not be used to
sterilize hands or other area of skin.
Exposure can cause skin irritation.

To see more go to shorturl.at/bopDW''')

    return ans
