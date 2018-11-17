"""
Creating an output file.

Fill in the blanks.

Specify the task name (name of the class) to execute:

    $ python main.py <taskname>

* What happens if you run the task again?
* What happens if you delete the file and run the task again?

"""

import luigi

class Hello(luigi.Task):

    def run(self):
        """ XXX: to implement. """

        # 1. Write a some string of your choice to the output file (use a
        #    context manager).

    def output(self):
        return luigi.LocalTarget(path="output.file")



if __name__ == '__main__':
    luigi.run(local_scheduler=True)

