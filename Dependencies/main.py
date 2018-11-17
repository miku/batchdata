"""
Defining dependencies.

Fill in the blanks.

Specify the task name (name of the class) to execute:

    $ python main.py <taskname>

"""

import random
import luigi
import collections

random.seed(0)

class Producer(luigi.Task):
    """
    Produces a random tab-separated file with [song, country, plays].

        call me maybe	me	65
        gangnam style	rs	100
        gangnam style	rs	45
        ...
    """

    def run(self):
        songs = ['call me maybe', 'gangnam style', 'battle scars']
        countries = ['ba', 'hr', 'me', 'rs', 'si']
        with self.output().open('w') as output:
            for i in range(100):
                output.write('%s\t%s\t%s\n' % (
                    random.choice(songs),
                    random.choice(countries), 
                    random.randint(0, 100)))

    def output(self):
        return luigi.LocalTarget(path='plays.tsv')

class TopSongs(luigi.Task):

    # 1. Add a parameters 'tld' to specify a country.
    tld = luigi.Parameter()
    
    # 2. Add a `requires` method to require task `Producer`.

    def run(self):
        """ Basic aggregation. """

        # 3. Open input a count and sum the occurences of each song for the
        #    given country. (Hint: collections.Counter can be helpful).


        # 4. Write an output TSV with two columns [song name, plays] ordered by
        #    plays descending.
    
    def output(self):
        pass
        # 5. Use different outputs for different tlds.



if __name__ == '__main__':
    luigi.run(local_scheduler=True)

