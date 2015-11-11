__author__ = 'Naleen'

# from src import classifier
# from src.classifier import validate
from src import classifier

# learner: True/False
classifier.train(zone='lower', start=1, end=30, phase='train', learner=False, n_mid=100, reg_fact=1, max_iter=100, normalize=True, rand=None)
classifier.validate(zone='lower', start=30, end=41, phase='validate')

classifier.train(zone='middle', start=1, end=30, phase='train', learner=False, n_mid=50, reg_fact=5, max_iter=100, normalize=True, rand=None)
classifier.validate(zone='middle', start=30, end=41, phase='validate')

classifier.train(zone='upper', start=1, end=30, phase='train', learner=False, n_mid=100, reg_fact=1, max_iter=1000, normalize=True, rand=None)
classifier.validate(zone='upper', start=30, end=41, phase='validate')
# print char


# n_mid=100, reg_fact=1, max_iter=1000, normalize=True, rand=None)
#
# train(zone='lower', start=1, end=30, phase='train', learner=False)
# validate(zone='lower', start=30, end=41, phase='validate')