# bbcpod
Downloads epsiodes of bbc radio podcasts. 

usage:

bbcpod.py iot tls

Where iot & tls are the code for 'In Our Time' and 'The Life Scientific' respectively.

Initially recognizes: iot (In Our Time), tls (The Life Scientific), ins (Inside Science), inh (Inside Health)

For each valid podcast code given will download ALL episodes of the podcast series that are not found in the current folder.

Downloaded files are named using snake_case e.g. the_speed_of_light.mp3

Plan to change this so we do not always download all episodes.
