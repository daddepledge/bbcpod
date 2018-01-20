"""bbc radio podcast download module"""
import os
import sys
from requests import get

def main():
    """Downloads iplayer episodes of any radio podcasts given as arguments.
    Files are mp3, filenames like the_speed_of_light.mp3 """
    # The list of known podcasts, please extend...
    pods = {'iot':('http://www.bbc.co.uk/programmes/b006qykl/episodes/player',
                   'In Our Time'),
            'tls':('http://www.bbc.co.uk/programmes/b015sqc7/episodes/player',
                   'The Life Scientific'),
            'ins':('http://www.bbc.co.uk/programmes/b036f7w2/episodes/player',
                   'Inside Science'),
            'inh':('http://www.bbc.co.uk/programmes/b019dl1b/episodes/player',
                   'Inside Health')}

    args = [a.lower() for a in sorted(sys.argv[1:])]

    if not args or any(p not in pods for p in args):
        for key in sorted(pods):
            print key, '-->', pods[key][-1]

    for pod in [p for p in args if p in pods]:
        print pods[pod][-1]
        download(pod, pods[pod][0])

def download(prefix, url):
    """Downloads any episodes not in the current folder"""
    page, pods = 1, True

    while pods:
        html, page = get(url + '?page=' + str(page)).content, page + 1
        pods = html.split('programme__body')[1:]

        for pod in pods:
            #
            name = pod.split('property="name">', 1)[1].split('<', 1)[0]
            name = prefix + ' ' + name.replace("'", '')
            for rem in '/?:;,-"':
                name = name.replace(rem, ' ')
            name = '_'.join(w for w in name.lower().split()) +'.mp3'

            if not os.path.exists(name):
                # Not all episodes can be downloaded
                try:
                    page = get('http://www.bbc.co.uk' + href(pod)).content
                    link = page.content.split(' buttons__download__link', 1)[1]
                    with open(name, "wb") as fil:
                        fil.write(href(link))
                    print name, 'Downloaded'
                except IndexError:
                    print name, 'Cannot download'

def href(html):
    """returns the value of the first href in html"""
    return html.split('href="', 1)[1].split('"')[0]

if __name__ == "__main__":
    main()
