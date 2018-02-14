from textblob.classifiers import NaiveBayesClassifier

train = [

    ('switch on the light', 'light-on'),
    ('switch the light on', 'light-on'),
    ('turn on the light', 'light-on'),
    ('turn the light on', 'light-on'),
    ('switch off the light', 'light-off'),
    ('switch the light off', 'light-off'),
    ('turn the light off', 'light-off'),
    ('turn off the light', 'light-off')

]

# Testing data suppose to be here [Untill I know its function]

C = NaiveBayesClassifier(train)

def classify(text):
    return C.classify(text)