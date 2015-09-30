'''
Created on 30 Sep 2015

@author: maxz
'''
import matplotlib, matplotlib.pyplot as plt  # @UnresolvedImport
import GPy, numpy as np
from applygpy.prediction import PredictionModelSparse, PredictionModel
import StringIO

import unittest

class Test(unittest.TestCase):

    def setUp(self):
        self.X, self.Y = np.random.normal(0, 1, (10, 1)), np.random.normal(0, 1, (10, 1))
        pass

    def testPlotting(self):
        m = GPy.models.GPRegression(self.X, self.Y) 
        p = PredictionModel(m)
        fig, ax = plt.subplots()
        m.plot(plot_training_data=False, ax=ax)
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i1 = StringIO.StringIO()
        fig.savefig(i1, format='svg')
        i1.seek(0)

        fig, ax = plt.subplots()
        p.plot(plot_training_data=False, ax=ax)        
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i2 = StringIO.StringIO()

        fig.savefig(i2, format='svg')
        i2.seek(0)
        
        self.assertEqual(i1.buf, i2.buf)

    def testPlottingSparse(self):
        m = GPy.models.SparseGPRegression(self.X, self.Y) 
        p = PredictionModelSparse(m)
        fig, ax = plt.subplots()
        m.plot(plot_training_data=False, ax=ax)
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i1 = StringIO.StringIO()
        fig.savefig(i1, format='svg')
        i1.seek(0)

        fig, ax = plt.subplots()
        p.plot(plot_training_data=False, ax=ax)        
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i2 = StringIO.StringIO()

        fig.savefig(i2, format='svg')
        i2.seek(0)
        
        self.assertEqual(i1.buf, i2.buf)

    def testPlottingClass(self):
        m = GPy.models.GPClassification(self.X, self.Y<0) 
        p = PredictionModel(m)
        fig, ax = plt.subplots()
        m.plot(plot_training_data=False, ax=ax)
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i1 = StringIO.StringIO()
        fig.savefig(i1, format='svg')
        i1.seek(0)

        fig, ax = plt.subplots()
        p.plot(plot_training_data=False, ax=ax)        
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i2 = StringIO.StringIO()

        fig.savefig(i2, format='svg')
        i2.seek(0)
        
        self.assertEqual(i1.buf, i2.buf)
        
    def testPlottingSparseClass(self):
        m = GPy.models.SparseGPClassification(self.X, self.Y<0) 
        p = PredictionModelSparse(m)
        fig, ax = plt.subplots()
        m.plot(plot_training_data=False, ax=ax)
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i1 = StringIO.StringIO()
        fig.savefig(i1, format='svg')
        i1.seek(0)

        fig, ax = plt.subplots()
        p.plot(plot_training_data=False, ax=ax)        
        ax.set_ylim(0, 1)
        ax.set_xlim(-2, 2)
        i2 = StringIO.StringIO()

        fig.savefig(i2, format='svg')
        i2.seek(0)
        
        self.assertEqual(i1.buf, i2.buf)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testPlotting']
    unittest.main()