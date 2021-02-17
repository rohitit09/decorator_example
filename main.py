from myplexer import Myplexer
app = Myplexer()

@app.route('hi')
def hi():
    return "Nice work"

#here the command has arguments, which will be space delimited in the input and
#should be passed in the same order to the function.
# e.g. sayhito santa
# will result in print_hi('santa')
@app.route('sayhito $name')
def print_hi(name):
    return "Hi, {0}".format(name)

#as many extra parameters can be passed in, with out declaring them.
#e.g. count a b c d
#will call count('a', 'b','c', 'd')
#will give 4 as result
@app.route('count')
def count(*items):
    return str(len(items))

#to exit from the run loop
@app.route('exit')
def exit():
    import sys
    sys.exit(0)


if __name__ == '__main__':
    app.run()



