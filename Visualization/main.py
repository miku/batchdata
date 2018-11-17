
import luigi
import random
import time

class A(luigi.Task):

    serial = luigi.IntParameter(default=0)

    def run(self):
        """ Just `touch` file. """
        with self.output().open('w') as output:
            pass

        time.sleep(random.randint(5, 15))

    
    def output(self):
        return luigi.LocalTarget(path='throwaway-a-%04d' % self.serial)
    

class B(luigi.Task):

    serial = luigi.IntParameter(default=0)

    def run(self):
        """ Just `touch` file. """
        with self.output().open('w') as output:
            pass

        time.sleep(random.randint(5, 15))
    
    def output(self):
        return luigi.LocalTarget(path='throwaway-b-%04d' % self.serial)


class C(luigi.Task):

    def requires(self):
        return [A(serial=i) for i in range(20)] + [B(serial=i) for i in range(20)]

    def run(self):
        """ Just `touch` file. """
        with self.output().open('w') as output:
            pass

        time.sleep(random.randint(1, 10))
    
    def output(self):
        return luigi.LocalTarget(path='throwaway-c')

if __name__ == '__main__':
    # Start central scheduler with `luigid` in a separate terminal or with
    # `luigid --background`.
    luigi.run()
