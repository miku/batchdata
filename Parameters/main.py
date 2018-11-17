"""
Using parameters.

Fill in the blanks.

Specify the task name (name of the class) to execute:

    $ python main.py <taskname>

* What happens, if you do not specify `--name`?

Try to run:

    $ python main.py <taskname> --help

* What would need to be changed in order to document a flag?

"""

import luigi

class Hello(luigi.Task):
    
    # 1. Add a parameter 'name' and run the task. Add a default later.
    name = luigi.Parameter()

    def run(self):
        """ XXX: to implement. """

        # 2. Write 'Hello <name>' to the output file.
        with self.output().open('w') as output:
            output.write('Hello %s\n' % self.name)

    def output(self):
        return luigi.LocalTarget(path="output.file")



if __name__ == '__main__':
    luigi.run(local_scheduler=True)

