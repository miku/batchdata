# Basics

Single file `main.py`:

```
class Hello(luigi.Task):

    def run(self):
        print("Hello World")
```

----

# Create Output

```
import luigi

class Hello(luigi.Task):

    def run(self):
        pass

        # 1. Local files are named `LocalTarget` and the behave a bit like
        #    files, you can open them and write to them. Write a random string
        #    to the output file. Use a context manager.

        with self.output().open('w') as f:
            f.write("Hello World")

    def output(self):
        return luigi.LocalTarget(path="output.file")



if __name__ == '__main__':
    luigi.run()
```

----

# Parameters

```python
import luigi

class Hello(luigi.Task):
    
    # 1. Add a parameter 'name' and run the task. Add a default.
    name = luigi.Parameter(default='World', description='user name')

    def run(self):
        """ XXX: to implement. """

        # 2. Write 'Hello <name>' to the output file.
        with self.output().open('w') as output:
            output.write('Hello %s\n' % self.name)

    def output(self):
        return luigi.LocalTarget(path="output.file")



if __name__ == '__main__':
    luigi.run(local_scheduler=True)

```
