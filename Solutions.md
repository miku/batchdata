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

